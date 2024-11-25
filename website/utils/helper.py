
import datetime as dt
from datetime import datetime, timedelta, date

from flask import jsonify
import geocoder

from website.database import encrypt
from website.utils import id_generator
from ..database.db import dbORM


def isFound(model, column, value):
	if dbORM.find_one(model, column, value)['status'][0] == "not found":
		result = None
	else:
		# print(isFound(model, column, value))
		result = dbORM.find_one(model, column, value)['status'][1]

	# print(">>>>>>><><><><><>>>>>>>>>>>>> ", result, " ", isFound(model, column, value))
	return result

def returnJSONData(title, content):
	return jsonify({
		"message": {title: content}
	})
 

 
def getDepartmentFaculty(department):
    return department

def isFoundAll(model, column, value):
	if dbORM.find_all(model, column, value)['status'][0] == "not found":
		result = []
	else:
		# print(isFound(model, column, value))
		result = dbORM.find_all(model, column, value)['status'][1]

	# print(">>>>>>><><><><><>>>>>>>>>>>>> ", result, " ", isFound(model, column, value))
	return result



def getDateTime():
	# Getting Date-Time Info
	current_date = dt.date.today()
	current_time = dt.datetime.now().strftime("%H:%M:%S")

	# Date Format: "YYYY-MM-DD"
	formatted_date = current_date.strftime("%Y-%m-%d")
	date = formatted_date
	time = current_time

	return [date, time]

def template_payload()-> dict:
    return {}



def checkLoginAndLogin(ip) -> dict | None:
    user = isFound("USERCSCAnonymousCHAT", "ip_address", ip)
    if user != None:
        return dbORM.get_all("USERCSCAnonymousCHAT")[f'{isFound("USERCSCAnonymousCHAT", "ip_address", ip)}']
    else:
        new_user = {
            "ip_address": geocoder.ip('me').ip,
            "uid": id_generator.generate_id(16),
            "datestamp": getDateTime()[0],
            "timestamp": getDateTime()[1],
            "temp": "&co;&cc;"
            # "location": f"{geocoder.ip('me').city}, {geocoder.ip('me').country}",
            # "latitude": f"{geocoder.ip('me').lat}",
            # "longitude": f"{geocoder.ip('me').lng}"
        }
        dbORM.add_entry("USERCSCAnonymousCHAT", encrypt.encrypter(str(new_user)))
        
        return dbORM.get_all("USERCSCAnonymousCHAT")[f'{isFound("USERCSCAnonymousCHAT", "ip_address", ip)}']
