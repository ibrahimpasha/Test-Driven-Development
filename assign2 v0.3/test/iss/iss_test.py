import unittest
from src.iss.iss import *


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
      convert_timestamp_to_time_at_latlong(1, 29.749907, -95.358421))

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
    lat_given, lon_given = 0, 0

    def iss_fly_over_function_mock(lat, lon):
      nonlocal lat_given, lon_given
      lat_given, lon_given = lat, lon

    compute_time_of_fly_over(34.0522, -118.2437, iss_fly_over_function_mock)

    self.assertEqual(34.0522, lat_given)
    self.assertEqual(-118.2437, lon_given)

  def test_compute_time_of_fly_over_returns_time_based_on_timestamp_returned_by_iss_fly_over_function(self):
    iss_fly_over_function_mock = lambda x, y: 60
    self.assertEqual('12/31/1969, 18:01:00',\
                     compute_time_of_fly_over(29.749907, -95.358421, iss_fly_over_function_mock))

  def test_compute_time_of_fly_over_reports_error_due_to_error_from_webservice(self):
    def fly_over_raise_connection_error_mock(x, y):
      raise Exception('Latitude must be number between -90.0 and 90.0')

    self.assertEqual('Latitude must be number between -90.0 and 90.0',
                     compute_time_of_fly_over(29.749907, -95.358421,\
                                              lambda x,y: fly_over_raise_connection_error_mock(x, y)))

  def test_compute_time_of_fly_over_reports_network_failure_error(self):
    def fly_over_raise_http_error_mock(x, y):
      raise ValueError("Network Error")

    self.assertEqual('Network Error',
                     compute_time_of_fly_over(29.749907, -95.358421,\
                                              lambda x,y: fly_over_raise_http_error_mock(x, y)))


if __name__ == '__main__':
  unittest.main()
