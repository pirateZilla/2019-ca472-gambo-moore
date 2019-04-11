import gspread
from oauth2client.service_account import ServiceAccountCredentials
import sqlite3
import csv 


# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("20190409.csv").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_values()

#print(list_of_hashes)
count = -2
for i in list_of_hashes:

	count = count + 1
	
	
	#print (list_of_hashes[count])
"""
with open("real_user.csv", 'w') as real_user:
	wr = csv.writer(real_user)
	wr.writerows(list_of_hashes[1])
"""
"""
    with open('real_user', 'wb') as f:  
        writer = csv.writer(f)  
        writer.writerows(list_of_hashes.row_values(1)) 
"""

"""
with open ('real_user.csv', 'w') as writeFile:
	writer = csv.writer(writeFile)
	writer.writerows(lines)	

con = sqlite3.Connection('real_user.sqlite')
cur = con.cursor()
cur.excute(CREATE TABLE "real_user" (
			"id" INT(10) AUTO_INCREMENT,
			"time" varchar(12),
			"lat"	varchar(12),
			"lon"	varchar(12),
			"elevation"	varchar(12),
			"accuracy"	varchar(12),
			"bearing" varchar(12),
			"speed"	 varchar(12),
			"satellites"  varchar(12),
			"provider"	 varchar(12),
			"hdop"	 varchar(12),
			"vdop"	 varchar(12),
			"pdop"	 varchar(12),
			"geoidheight"	 varchar(12),
			"ageofdgpsdata"	 varchar(12),
			"dgpsid" varchar(12),
			"activity"	 varchar(12),
			"battery"	 varchar(12),
			"annotation" varchar(12),						


	))

"""