function calculatePremium() {
    var basePrice = 2500;
    var title = document.getElementsByName('title').value;
    var fname = document.getElementsByName('fname').value;
    var dob = document.getElementById('bday').value;
    var bday = +new Date(dob);
    var age = ~~((Date.now() - bday) / (31557600000));
    var ages = { 21: 1, 22: 1.0168, 23: 1.0173, 24: 0.9728, 25: 1.1973, 26: 1.1826, 27: 1.1709, 28: 1.158, 29: 1.158 };
    var ageBasePrice = ages[age] * basePrice;

    var occ = document.getElementsByName('occupation')[0];
    var occPc = occ.options[occ.selectedIndex].value;
    var occSubVal = basePrice - basePrice * occPc;

    var hh = document.getElementsByName('household')[0];
    var hhPc = hh.options[hh.selectedIndex].value;
    var hhSubVal = basePrice - basePrice * hhPc;

    var car = document.getElementsByName('car')[0];
    var carPc = car.options[car.selectedIndex].value;
    var carSubVal = basePrice - basePrice * carPc;

    var loc = document.getElementsByName('location')[0];
    var locPc = loc.options[loc.selectedIndex].value;
    var locSubVal = basePrice - basePrice * locPc;

    var bon = document.getElementsByName('ncb')[0];
    var bonPc = bon.options[bon.selectedIndex].value;
    var bonSubVal = basePrice - basePrice * bonPc;

    var lic = document.getElementsByName('licence')[0];
    var licPc = lic.options[lic.selectedIndex].value;
    var licSubVal = basePrice - basePrice * licPc;

    var exp = document.getElementsByName('namedexp')[0];
    var expPc = exp.options[exp.selectedIndex].value;
    var expSubVal = basePrice - basePrice * expPc;

    var pen = document.getElementsByName('penalty')[0];
    var penPc = pen.options[pen.selectedIndex].value;
    var penSubVal = basePrice - basePrice * penPc;

    var add = document.getElementsByName('addDrivers')[0];
    var addPc = add.options[add.selectedIndex].value;
    var addSubVal = basePrice - basePrice * addPc;

    var claims = document.getElementsByName('claims')[0];
    var claimsPc = claims.options[claims.selectedIndex].value;
    var claimsSubVal = basePrice - basePrice * claimsPc;

    var vehicleProcurement = 1500;
    var telematicsDevice = 150;
    var telematicsInstall = 50;
    var vehicleMaintenance = 100;
    var motorTax = 200;
    var excess = 300;

    var finalInsurancePrice = ageBasePrice - occSubVal - hhSubVal - carSubVal - bonSubVal - locSubVal - licSubVal - expSubVal - penSubVal - addSubVal - claimsSubVal;
    

    //Minimum insurance price fix
    if (finalInsurancePrice < 300) {
        finalInsurancePrice = 300;
    }

    var otherCosts = vehicleProcurement + telematicsDevice + telematicsInstall + vehicleMaintenance + motorTax;
    var totalCost = finalInsurancePrice + otherCosts;
    var monthlyFinalInsurancePrice = totalCost/12;
    var roundedMonthlyFinalInsurancePrice = monthlyFinalInsurancePrice.toFixed(2);

    console.log("The base price is €" + basePrice);
    console.log("The final insurance cost is €" + finalInsurancePrice);

    //gets the first name input 
    var title = document.getElementById("title").value;
    var fname = document.getElementById("fname").value;
    var lname = document.getElementById("lname").value;
    var occupation = document.getElementById("occupation").value;
    var household = document.getElementById("household").value;
    var car = document.getElementById("car").value;
    var address_l1 = document.getElementById("address_l1").value;
    var address_l2 = document.getElementById("address_l2").value;
    var area = document.getElementById("location").value;
    var licence = document.getElementById("licence").text;
    var ncb = document.getElementById("ncb").value;
    var namedexp = document.getElementById("namedexp").value;
    var penalty = document.getElementById("penalty").value;
    var addDrivers = document.getElementById("addDrivers").value;
    var claims = document.getElementById("claims").value;

    // GET THE TEXT VALUE FOR LOCATION/AREA
    var locationSelect = document.getElementById("location");
    var area = locationSelect.options[locationSelect.selectedIndex].text;

    var carSelect = document.getElementById("car");
    var model = carSelect.options[carSelect.selectedIndex].text;

    var licenceSelect = document.getElementById("licence");
    var licenceType = licenceSelect.options[licenceSelect.selectedIndex].text;

    var ncbSelect = document.getElementById("ncb");
    var ncbYears = ncbSelect.options[ncbSelect.selectedIndex].text;

    var namedSelect = document.getElementById("namedexp");
    var namedExperience = namedSelect.options[namedSelect.selectedIndex].text;

    var penSelect = document.getElementById("penalty");
    var penPoints = penSelect.options[penSelect.selectedIndex].text;

    var addSelect = document.getElementById("addDrivers");
    var additionalDrivers = addSelect.options[addSelect.selectedIndex].text;

    var claimSelect = document.getElementById("claims");
    var numberOfClaims = claimSelect.options[claimSelect.selectedIndex].text;

    var dataIsValid = true;

    if (title == "") {
        // alert("You must be aged 21-29 in order to use TourGo");
        document.forms["calculator"]["title"].style.border = "1px solid red";
        document.getElementById("titlemsg").innerHTML = "Please enter your title";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["title"].style.border = "";
        document.getElementById("titlemsg").innerHTML = "";
    }

    if (fname == "") {
        document.forms["calculator"]["fname"].style.border = "1px solid red";
        document.getElementById("fnamemsg").innerHTML = "Please enter your first name";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["fname"].style.border = "";
        document.getElementById("fnamemsg").innerHTML = "";
    }

    if (lname == "") {
        document.forms["calculator"]["lname"].style.border = "1px solid red";
        document.getElementById("lnamemsg").innerHTML = "Please enter your last name";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["lname"].style.border = "";
        document.getElementById("lnamemsg").innerHTML = "";
    }

    if (!(age > 20 && age < 30)) {
        document.forms["calculator"]["bday"].style.border = "1px solid red";
        document.getElementById("bdaymsg").innerHTML = "TourGo members must be aged 21-29";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["bday"].style.border = "";
        document.getElementById("bdaymsg").innerHTML = "";
    }

    if (occupation == "") {
        document.forms["calculator"]["occupation"].style.border = "1px solid red";
        document.getElementById("emplmsg").innerHTML = "Please enter your employment status";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["occupation"].style.border = "";
        document.getElementById("emplmsg").innerHTML = "";
    }

    if (household == "") {
        document.forms["calculator"]["household"].style.border = "1px solid red";
        document.getElementById("homemsg").innerHTML = "Please enter your home type";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["household"].style.border = "";
        document.getElementById("homemsg").innerHTML = "";
    }

    if (car == "") {
        document.forms["calculator"]["car"].style.border = "1px solid red";
        document.getElementById("carmsg").innerHTML = "Please enter your preferred vehicle";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["car"].style.border = "";
        document.getElementById("carmsg").innerHTML = "";
    }


    if (address_l1 == "") {
        document.forms["calculator"]["address_l1"].style.border = "1px solid red";
        document.getElementById("adrmsg").innerHTML = "Please enter your address";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["address_l1"].style.border = "";
        document.getElementById("adrmsg").innerHTML = "";
    }

    if (location == "") {
        document.forms["calculator"]["location"].style.border = "1px solid red";
        document.getElementById("locmsg").innerHTML = "Please enter the area you live";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["location"].style.border = "";
        document.getElementById("locmsg").innerHTML = "";
    }

    if (licence == "") {
        document.forms["calculator"]["licence"].style.border = "1px solid red";
        document.getElementById("licmsg").innerHTML = "Please enter your licence type";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["licence"].style.border = "";
        document.getElementById("licmsg").innerHTML = "";
    }

    if (ncb == "") {
        document.forms["calculator"]["ncb"].style.border = "1px solid red";
        document.getElementById("ncbmsg").innerHTML = "Please enter your claims-free own driving experience";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["ncb"].style.border = "";
        document.getElementById("ncbmsg").innerHTML = "";
    }

    if (namedexp == "") {
        document.forms["calculator"]["namedexp"].style.border = "1px solid red";
        document.getElementById("nxpmsg").innerHTML = "Please enter your named driving experience";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["namedexp"].style.border = "";
        document.getElementById("nxpmsg").innerHTML = "";
    }

    if (penalty == "") {
        document.forms["calculator"]["penalty"].style.border = "1px solid red";
        document.getElementById("penmsg").innerHTML = "Please enter the number of penalty points you have";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["penalty"].style.border = "";
        document.getElementById("penmsg").innerHTML = "";
    }

    if (addDrivers == "") {
        document.forms["calculator"]["addDrivers"].style.border = "1px solid red";
        document.getElementById("addmsg").innerHTML = "Please enter the number of additional drivers you want on your policy";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["addDrivers"].style.border = "";
        document.getElementById("addmsg").innerHTML = "";
    }

    if (claims == "") {
        document.forms["calculator"]["claims"].style.border = "1px solid red";
        document.getElementById("clmmsg").innerHTML = "Please enter the number of claims you've made in the past 5 years";
        // scroll(0, 0)
        dataIsValid = false;
    } else {
        document.forms["calculator"]["claims"].style.border = "";
        document.getElementById("clmmsg").innerHTML = "";
    }

    if (dataIsValid) { } else {
        // alert("You didn't fill out all the fields or filled something in wrong");
        window.scrollTo(0, 0)
        return false;
    }

    document.getElementById("personal").innerHTML = "Personal Details";
    document.getElementById("nameTitle").innerHTML = "Name";
    document.getElementById("name").innerHTML = title + " " + fname + " " + lname;
    document.getElementById("addressTitle").innerHTML = "Address";
    document.getElementById("address").innerHTML = address_l1 + ", " + address_l2 + ", " + area;
    document.getElementById("ageTitle").innerHTML = "Age";
    document.getElementById("age").innerHTML = age;

    document.getElementById("Vehicle").innerHTML = "Vehicle";
    document.getElementById("brandTitle").innerHTML = "Brand and Model";
    document.getElementById("brand").innerHTML = model;
    document.getElementById("engTitle").innerHTML = "Engine";
    document.getElementById("eng").innerHTML = "1L Petrol; Manual Transmission"
    document.getElementById("yearTitle").innerHTML = "Year Registered";
    document.getElementById("year").innerHTML = "2019";

    document.getElementById("member").innerHTML = "Membership";
    document.getElementById("premTitle").innerHTML = "Annual Premium";
    document.getElementById("prem").innerHTML = "€" + totalCost;
    document.getElementById("premMonthTitle").innerHTML = "Monthly Cost";
    document.getElementById("premMonth").innerHTML = "€" + roundedMonthlyFinalInsurancePrice;
    document.getElementById("excessTitle").innerHTML = "Policy Excess";
    document.getElementById("excess").innerHTML = "€" + excess;
    document.getElementById("useClassTitle").innerHTML = "Class of use";
    document.getElementById("useClass").innerHTML = "Social, domestic and pleasure; up to 15,000km per year";

    document.getElementById("driver").innerHTML = "Driver Details";
    document.getElementById("licenceTitle").innerHTML = "Licence Type";
    document.getElementById("licenceType").innerHTML = licenceType;
    document.getElementById("ncbTitle").innerHTML = "No Claims Bonus";
    document.getElementById("ncbYears").innerHTML = ncbYears;
    document.getElementById("nexpTitle").innerHTML = "Named Experience";
    document.getElementById("namedExp").innerHTML = namedExperience;
    document.getElementById("penTitle").innerHTML = "Penalty Points";
    document.getElementById("penPoints").innerHTML = penPoints;
    document.getElementById("addDriveTitle").innerHTML = "Additional Drivers";
    document.getElementById("addDrive").innerHTML = additionalDrivers;
    document.getElementById("claimTitle").innerHTML = "Number of Recent Claims";
    document.getElementById("claim").innerHTML = numberOfClaims;

    // document.getElementById("output1").innerHTML = "The base price is €" + basePrice;
    // //prints to the html 
    // document.getElementById("output2").innerHTML = "Hey " + fname + "! Your total premium cost is €" + finalInsurancePrice;


}
