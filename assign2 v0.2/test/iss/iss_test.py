import unittest
from unittest.mock import Mock, MagicMock, call
from src.iss.iss import *
import requests

class ISS(unittest.TestCase):

  def test_Canary(self):
    self.assertTrue(True)
  
  def test_convert_0_to_time_stamp_for(self):
    self.assertEqual('01/01/1970, 00:00:00', convert_timestamp_to_utc(0))

  def test_convert_2_to_time_stamp(self):
    self.assertEqual('01/01/1970, 00:00:02', convert_timestamp_to_utc(2))
  
  def test_convert_60_to_time_stamp(self):
    self.assertEqual('01/01/1970, 00:01:00', convert_timestamp_to_utc(60))
  
  def test_convert_1569130749_to_time_stamp(self):
    self.assertEqual('09/22/2019, 05:39:09',\
      convert_timestamp_to_utc(1569130749))

  def test_time_for_timestamp_at_lat_lng_Houston_1(self):
    self.assertEqual('12/31/1969, 18:00:01',\
      convert_timestamp_to_time_at_latlong(1, 29.749907, -95.358421)) #Feedback: a blank line after this line, please
  def test_time_for_timestamp_at_lat_lng_Houston_2(self):
    self.assertEqual('12/31/1969, 18:00:02',\
      convert_timestamp_to_time_at_latlong(2, 29.749907, -95.358421))

  def test_time_for_timestamp_at_lat_lng_Houston_60(self):
    self.assertEqual('12/31/1969, 18:01:00', \
      convert_timestamp_to_time_at_latlong(60, 29.749907, -95.358421))
  
  def test_time_for_timestamp_at_lat_lng_Houston_1569130749(self):
    self.assertEqual('09/22/2019, 00:39:09', \
      convert_timestamp_to_time_at_latlong(1569130749, 29.749907, -95.358421))

  def test_time_for_timestamp_at_lat_lng_New_York_1(self):
    self.assertEqual('12/31/1969, 19:00:01', \
      convert_timestamp_to_time_at_latlong(1, 40.730610, -73.935242))

  def test_time_for_timestamp_at_lat_lng_New_York_2(self):
    self.assertEqual('12/31/1969, 19:00:02', \
      convert_timestamp_to_time_at_latlong(2, 40.730610, -73.935242))

  def test_time_for_timestamp_at_lat_lng_New_York_60(self):
    self.assertEqual('12/31/1969, 19:01:00', \
      convert_timestamp_to_time_at_latlong(60, 40.730610, -73.935242))

  def test_time_for_timestamp_at_lat_lng_New_York_1569130749(self):
    self.assertEqual('09/22/2019, 01:39:09', \
      convert_timestamp_to_time_at_latlong(1569130749, 40.730610, -73.935242))

  def test_time_for_timestamp_at_lat_lng_Singapore_1(self):
    self.assertEqual('01/01/1970, 07:30:01', \
      convert_timestamp_to_time_at_latlong(1, 1.290270, 103.851959))

  def test_time_for_timestamp_at_lat_lng_Singapore_2(self):
    self.assertEqual('01/01/1970, 07:30:02', \
      convert_timestamp_to_time_at_latlong(2, 1.290270, 103.851959))

  def test_time_for_timestamp_at_lat_lng_Singapore_60(self):
    self.assertEqual('01/01/1970, 07:31:00', \
      convert_timestamp_to_time_at_latlong(60, 1.290270, 103.851959))

  def test_time_for_timestamp_at_lat_lng_Singapore_1569130749(self):
    self.assertEqual('09/22/2019, 13:39:09', \
      convert_timestamp_to_time_at_latlong(1569130749, 1.290270, 103.851959))

  def test_compute_time_of_fly_over_passes_lat_long_to_iss_fly_over_function(self):
    #Feedback:
    # lat_given, lon_given = 0, 0
    #
    #def iss_fly_over_function_mock(lat, lon):
    #  nonlocal lat_given, lon_given
    #  lat_given, lon_given = lat, lon
    #
    #  compute_time_of_fly_over(34.0522, -118.2437,\
    # iss_fly_over_function_mock)
    #
    # self.assertEqual(34.0522, lat_given)
    # self.assertEqual(-118.2437, lon_given)
    
    iss_fly_over_function_mock = lambda x, y: 3600
    self.assertEqual('12/31/1969, 17:00:00', compute_time_of_fly_over(34.0522, -118.2437, iss_fly_over_function_mock))
    
  def test_compute_time_of_fly_over_returns_time_based_on_timestamp_returned_by_iss_fly_over_function(self):
    iss_fly_over_function_mock = lambda x, y: 60
    self.assertEqual('12/31/1969, 18:01:00', compute_time_of_fly_over(29.749907, -95.358421, iss_fly_over_function_mock))

  def test_compute_time_of_fly_over_reports_error_due_to_error_from_webservice(self):
    def fly_over_raise_connection_error_mock(x, y):
      raise Exception('Latitude must be number between -90.0 and 90.0') #Feedback: a blank line after this line, please
    self.assertEqual('Latitude must be number between -90.0 and 90.0', compute_time_of_fly_over(29.749907, -95.358421, lambda x,y: fly_over_raise_connection_error_mock(x, y)))

  def test_compute_time_of_fly_over_reports_network_failure_error(self):
    def fly_over_raise_http_error_mock(x, y):
      raise requests.exceptions.HTTPError #Feedback: raise ValueError("Network Error")
    self.assertEqual('Network Error',
                     compute_time_of_fly_over(29.749907, -95.358421, lambda x,y: fly_over_raise_http_error_mock(x, y)))

#Feedback: SRP: The following should go into a new file
  def test_parse_data_returns_timestamp_one_sample_data(self):
    sample_data = {
      "message": "success",
      "request": {
        "altitude": 100,
        "datetime": 1569907497,
        "latitude": 29.72167,
        "longitude": -95.343631,
        "passes": 1
      },
      "response": [
        {
          "duration": 420,
          "risetime": 1569911133
        }
      ]
    } #Feedback: a blank line after this line, please
    self.assertEqual(1569911133, parse(sample_data))

  def test_parse_data_returns_timestamp_another_sample_data(self):
    sample_data = {
      "message": "success",
      "request": {
        "altitude": 100,
        "datetime": 1569910381,
        "latitude": 40.73061,
        "longitude": -73.935242,
        "passes": 1
      },
      "response": [
        {
          "duration": 523,
          "risetime": 1569953945
        }
      ]
    }  #Feedback: a blank line after this line, please
    self.assertEqual(1569953945, parse(sample_data))


  def test_parse_data_with_error_msg_lat_being_too_long(self):
    sample_json = {"message": "failure","reason": "Latitude must be number between -90.0 and 90.0"} #Feedback: a blank line after this line, please
    try:
      parse(sample_json)
    except Exception as e:
      self.assertEqual('Latitude must be number between -90.0 and 90.0', e.args[0])             
    
    #Feedback: instead of the above, let's do  
    with self.assertRaisesRegexp(Exception, "Latitude must be number between -90.0 and 90.0"):
      parse(sample_json)
    

  def test_parse_data_with_error_msg_longitude_being_too_long(self):
    sample_json = {"message": "failure","reason": "Longitue must be number between -180.0 and 180.0"}
    try:
      parse(sample_json)
    except Exception as e:
      self.assertEqual('Longitue must be number between -180.0 and 180.0', e.args[0])

  def test_fetch_iss_fly_over_data_and_calls_service_and_parse_response_to_parse(self):
    parse_mock = lambda x: 1569953945
    self.assertEqual(1569953945, fetch_iss_fly_over_data(40.73061, -73.935242, parse_mock))
    
  def test_fetch_iss_fly_over_data_and_returns_time_stamp_returned_by_parse(self):
    parse_mock = lambda x: 1569954053
    self.assertEqual(1569954053, fetch_iss_fly_over_data(45.73061, -73.935242, parse_mock))

  def test_fetch_iss_fly_over_data_and_returns_error_returned_by_parse(self):
    #Feedback: let's simply this test (see suggestions above to simply)
    try:
      def raise_parse_exception_mock(x):
        raise Exception('Latitude must be number between -90.0 and 90.0')
      fetch_iss_fly_over_data(455555.73061, -73.935242, raise_parse_exception_mock)
    except Exception as e:
      if e.args[0]=='Latitude must be number between -90.0 and 90.0':
        self.assertTrue(True)
  
  def test_fetch_iss_fly_over_data_and_returns_network_error_from_call_to_service(self):
    #Feedback:  the service should blow up and not parse. This test is not doing what it says it should be checking for
    try:
      def raise_parse_exception_mock(x):
        raise requests.exceptions.HTTPError
      fetch_iss_fly_over_data(455555.73061, -73.935242, raise_parse_exception_mock)
    except requests.exceptions.HTTPError:
      self.assertTrue(True)
  

if __name__ == '__main__':
  unittest.main()
