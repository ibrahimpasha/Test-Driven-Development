from datetime import datetime, timezone
import requests
from timezonefinder import TimezoneFinder
import pytz


def convert_timestamp_to_utc(epochs):
  return datetime.fromtimestamp(epochs, timezone.utc).strftime("%m/%d/%Y, %H:%M:%S")


def convert_timestamp_to_time_at_latlong(timestmp, lat, long):
  utc_time = datetime.strptime(convert_timestamp_to_utc(timestmp), "%m/%d/%Y, %H:%M:%S")
  return utc_time.replace(tzinfo=timezone.utc)\
      .astimezone(tz=pytz.timezone(TimezoneFinder()\
      .timezone_at(lat=lat, lng=long))).strftime("%m/%d/%Y, %H:%M:%S")


def compute_time_of_fly_over(lat, long, iss_fly_over_function):
  try:
   return convert_timestamp_to_time_at_latlong(iss_fly_over_function(lat, long), lat, long)
  #Feedback: except Exception as e:
  # return str(e)  
  except requests.exceptions.HTTPError: #Feedback: please remove
    return "Network Error"              #Feedback: please remove
  except Exception as e:                #Feedback: please remove
    return e.args[0]                    #Feedback: please remove

#This file has convertTimeStamp.. functions. That's pretty stable and a good 
#responsibility. Now, adding parse to this file has two problems.

#1. parse is an extra responsibility not related to converting the time - 
#violation of Single Responsibility Principle

#2. parse depends on format that can change if we use a different web service 
#or there is a newer version of the webservice. Thus, this file has to change 
#when an external service changes. Violation of Open Closed Principle.

#How to proceed:
#One file with functions related to convertTimeStamp... and compute time of fly over.

#Another new file with parseJSONData function.

#Also, let the test class honor SRP also: New file, new test class.

#Feedback: parse function first as that is being designed first in the tests      

def fetch_iss_fly_over_data(lat, long, parse):
  url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n=1'.format(lat, long)
  try:
    return parse(requests.get(url).json())
  except requests.exceptions.HTTPError:
    raise requests.exceptions.HTTPError
  
def parse(json_data):
  if json_data['message']=='success':
    return json_data['response'][0]['risetime']
  else:
    raise Exception(json_data['reason'])
