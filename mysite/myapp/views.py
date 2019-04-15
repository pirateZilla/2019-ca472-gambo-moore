from django.shortcuts import render, render_to_response, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
# imports the  driver model so we can save the data to it
from .models import Driver, Car, Maintenance, Journeys, Speed, Fatigue, Smoothness, TimeOfDay, Month_journey, Week_journey, Day_journey, Real_user
import pprint
import json
from django.core.serializers.json import DjangoJSONEncoder

# Create your views here.


def index(request):

    return render_to_response("index.html")


def quote(request, ):
    # print (request.user)

    name1 = request.GET.get('name1')
    fname = request.GET.get('fname')

    print(name1)
    print(fname)
    context = {}

    return render(request, "quote.html", context)


def about(request):
    return render_to_response("about.html")


def faq(request):
    return render_to_response("faq.html")


def contact(request):
    return render_to_response("contact.html")


def user_dash(request):

    # google maps funtionality

    # collects the driver ID from the dropdown
    user_id = request.GET.get('user_id')

    # SQL QUERIES for diffent drivers
    average_JS = Driver.objects.raw('''select myapp_driver.id,  ROUND(AVG(journey_score)) AS avg_journey_score, myapp_driver.f_name, myapp_driver.l_name
											from myapp_driver
											join myapp_journeys on myapp_driver.id = myapp_journeys.Driver_id
											where myapp_driver.id = %s;
											''', [user_id])

    num_journeys_this_week = Journeys.objects.raw('''select myapp_journeys.id, count(myapp_journeys.id) as trips
													from myapp_journeys
													where Driver_id = %s;
	 												''', [user_id])
    km_driven = Journeys.objects.raw('''select myapp_journeys.id,  sum(myapp_journeys.distance) AS km_driven
										from myapp_journeys
										where Driver_id = %s;
								 	''', [user_id])

    avg_smoothness = Smoothness.objects.raw('''select myapp_journeys.id,  cast(Round (avg(myapp_smoothness.Smoothness_level)) as int)AS avg_smoothness,
												myapp_car.car_type,  myapp_car.car_mileage, myapp_car.car_reg, myapp_car.engine_size
												from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
												inner join myapp_smoothness on
 												myapp_smoothness.Journeys_id = myapp_journeys.id
												where myapp_car.Driver_id = %s;
											''', [user_id])

    avg_fatigue = Fatigue.objects.raw('''select myapp_journeys.id,   cast(Round (avg(myapp_fatigue.fatigue_level)) as int)AS avg_fatigue
										from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
										inner join myapp_fatigue on
 										myapp_fatigue.Journeys_id = myapp_journeys.id
										where myapp_car.Driver_id = %s;
									 ''', [user_id])

    avg_speed = Speed.objects.raw('''select myapp_journeys.id,   cast(Round (avg(myapp_speed.speed_level)) as int)AS avg_speed
									from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
									inner join myapp_speed on
 									myapp_speed.Journeys_id = myapp_journeys.id
									where myapp_car.Driver_id = %s;
	 							''', [user_id])

    TimeOfDay_level = TimeOfDay.objects.raw('''select myapp_journeys.id, cast(Round (avg(myapp_timeofday.time_of_day_level)) as int)AS avg_timeofday
											from myapp_car inner join myapp_journeys on myapp_car.Driver_id = myapp_journeys.Driver_id
											inner join myapp_timeofday on
 											myapp_timeofday.Journeys_id = myapp_journeys.id
											where myapp_car.Driver_id = %s;
	 									''', [user_id])

    #sql queries used to create the data needed for a dynamic view of trends 

    month_journey_score = Month_journey.objects.raw('''SELECT myapp_month_journey.id, myapp_month_journey.month, myapp_month_journey.monthly_journey_score
		                                            from myapp_month_journey 
                                                    WHERE myapp_month_journey.Driver_id = %s;
                                                    ''', [user_id])

    week_journey_score = Week_journey.objects.raw('''SELECT myapp_week_journey.id, myapp_week_journey.week, myapp_week_journey.weekly_journey_score
		                                            from myapp_week_journey 
                                                    WHERE myapp_week_journey.Driver_id = %s;
                                                    ''', [user_id])

    day_journey_score = Day_journey.objects.raw('''SELECT myapp_day_journey.id, myapp_day_journey.day, myapp_day_journey.daily_journey_score
		                                            from myapp_day_journey 
                                                    WHERE myapp_day_journey.Driver_id = %s;
                                                    ''', [user_id])

    # collects the start and end location of a driver journey n.b it only looks at the last journey
    start_location = Journeys.objects.raw('''select myapp_journeys.id, myapp_journeys.distance, myapp_journeys.journey_score, myapp_journeys.end_time, myapp_journeys.start_time, myapp_journeys.start_location, myapp_journeys.end_location
		from myapp_journeys where myapp_journeys.Driver_id= %s''', [user_id])

    # has to have a defult figure or map functionality wont work
    month_score_array = []
    month_score = "0"
    for x in month_journey_score:
        month_score = x.monthly_journey_score
        month_score_array.append(month_score)

    week_score_array = []
    week_score = "0"
    for x in week_journey_score:
        week_score = x.weekly_journey_score
        week_score_array.append(week_score)

    day_score_array = []
    day_score = "0"
    for x in day_journey_score:
        day_score = x.daily_journey_score
        day_score_array.append(day_score)


#functionality for dynamic pie chart --> will beark the application so 2user_dash url" must be "/user_dash/?user_id=1"
    last_month_avg = "0"
    last_month_avg = (
        week_score_array[3]+week_score_array[4]+week_score_array[5]+week_score_array[6])/4
    print(last_month_avg)

    total_avg = "0"
    total_avg = sum(day_score_array)/len(day_score_array)

    maps_start = "0"
    maps_end = "0"
    distance = "0"
    score = "0"
    time_end = "0"
    time_start = "0"
    for x in start_location:
        maps_start = x.start_location
        maps_end = x.end_location
        distance = x.distance
        score = x.journey_score
        time_end = x.end_time
        time_start = x.start_time

#DEC do not change this without telling me as this till break the leaning task links 
    speedScoreWeekAvg = "0"
    for x in avg_speed:
        speedScoreWeekAvg = x.avg_speed

    fatigueScoreWeekAvg = "0"
    for x in avg_fatigue:
        fatigueScoreWeekAvg = x.avg_fatigue

    smoothScoreWeekAvg = "0"
    for x in avg_smoothness:
        smoothScoreWeekAvg = x.avg_smoothness

    todScoreWeekAvg = "0"
    for x in TimeOfDay_level:
        todScoreWeekAvg = x.avg_timeofday

    # google maps link with API key for journey locations
    src = "https://www.google.com/maps/embed/v1/directions?origin=" + maps_start + \
        "&" + "destination="+maps_end + "&key=AIzaSyAEIIVLTLc_JfDkoF_j3lv8Y5j6qpf5NoI"

    #funtion is to redirect a user to specfic  learning task based on the users lowest of the 4 catigories of their score breakdown 

   



    #this finds the lowest value of the 4 catigories of driving behaviours 
    list_of_socre_breakdown = [speedScoreWeekAvg,fatigueScoreWeekAvg, smoothScoreWeekAvg, todScoreWeekAvg]
    lowest_score = min(list_of_socre_breakdown)
   
   
    # this sends a specific learning url based on the users lowest score in their score breakdown
    learning_url = 0
    if lowest_score == speedScoreWeekAvg:
        learning_url = "/speed_learn/"

    elif lowest_score == smoothScoreWeekAvg:
        print("yes")
        learning_url = "/smoothness_learn/"

    elif lowest_score == fatigueScoreWeekAvg:
        print("no")
        learning_url = "/fatigue_learn/"

    elif lowest_score == todScoreWeekAvg:
        learning_url = "/tod_learn/"
    else:
        learning_url = "/learning_platform/"

    context = {

        "journey_score": average_JS,
        "num_trips": num_journeys_this_week,
        "km_driven": km_driven,
        "smoothness": avg_smoothness,
        "fatigue": avg_fatigue,
        "speed": avg_speed,
        "TimeOfDay": TimeOfDay_level,
        "start_location": start_location,
        "src": src,
        "start": maps_start,
        "end": maps_end,
        "distance": distance,
        "score": score,
        "time_start": time_start,
        "time_end": time_end,
        "speedScoreWeekAvg": speedScoreWeekAvg,
        "fatigueScoreWeekAvg": fatigueScoreWeekAvg,
        "smoothScoreWeekAvg": smoothScoreWeekAvg,
        "todScoreWeekAvg": todScoreWeekAvg,
        "dayArray": day_score_array,
        "weekArray": week_score_array,
        "monthArray": month_score_array,
        "last_month_avg": last_month_avg,
        "total_avg": total_avg,
        "learning_url": learning_url
    }
    return render_to_response("user_dash.html", context)


def registration(request):
    driver = Driver()

    f_name = request.GET.get('fname')
    l_name = request.GET.get('lname')
    dob = request.GET.get('bday')
    address1 = request.GET.get('address_l1')
    address2 = request.GET.get('address_l2')
    print("the quote details are", f_name, l_name, dob, address1, address2)
    # sends input data to the model
    """
	driver.f_name = f_name
	driver.l_name = l_name
	driver.address1 = address1
	driver.address2 = address2
	driver.save()
	"""
    # print(f_name, eircode, drive_exp)

    context = {}
    return render(request, "registration.html", context)


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        # checks if data passed to the form is valid
        if form.is_valid():
            form.save()  # saves info to the DB --> creating a new user
            # get data passed from the form
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # authenticate is a hash funtion in djnago
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('login')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(request, "registration/register.html", context)


def login(request, user):

    context = {}
    return redirect('quote', context)


def maintenance_checklist(request):
    maintenance = Maintenance()

    oil_level = request.GET.get('oil_level')
    battery_level = request.GET.get('battery_level')
    coolent_level = request.GET.get('coolent_level')
    tyre_depth = request.GET.get('tyre_depth')
    windscreen_washer_level = request.GET.get('windscreen_washer_level')
    print("the maintenance results are", oil_level, battery_level,
          coolent_level, tyre_depth, windscreen_washer_level)
    # sends input data to the model
    """
	driver.f_name = f_name
	driver.l_name = l_name
	driver.address1 = address1
	driver.address2 = address2
	driver.save()
	"""
    # print(f_name, eircode, drive_exp)

    return render(request, "maintenance_checklist.html")


def coming_soon(request):

    return render(request, "coming_soon.html")


def learning_platform(request):
    start_location = Real_user.objects.raw('''select id, time, lat, lon 
from  myapp_real_user
where id = 1;
''')
    end_location = Real_user.objects.raw('''select id, time, lat, lon 
from  myapp_real_user
where id = 47;
''')
    start_lat =0
    start_lon = 0
    for x in start_location:
        start_lat = x.lat
        start_lon = x.lon

    end_lat =0
    end_lon = 0
    for x in end_location:
        end_lat = x.lat
        end_lon = x.lon
       

    

     # google maps link with API key for real journeys collected 
    src2 = "https://www.google.com/maps/embed/v1/directions?origin=" + start_lat+ "," + start_lon + "&" + "destination="+ end_lat+ "," + end_lon + "&key=AIzaSyAEIIVLTLc_JfDkoF_j3lv8Y5j6qpf5NoI"
    context = {
    "src2": src2
    }

    return render(request, "learning_platform.html", context)


def speed_learn(request):
    return render_to_response("speed_learn.html")


def fatigue_learn(request):
    return render_to_response("fatigue_learn.html")


def smoothness_learn(request):
    return render_to_response("smoothness_learn.html")


def tod_learn(request):
    return render_to_response("tod_learn.html")
