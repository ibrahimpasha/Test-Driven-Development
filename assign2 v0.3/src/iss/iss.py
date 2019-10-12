from datetime import datetime, timezone
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
  except Exception as e:
    return str(e)

