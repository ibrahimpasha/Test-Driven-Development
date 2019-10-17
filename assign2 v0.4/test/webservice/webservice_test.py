import unittest
from src.webservice.webservice import *
import requests
from unittest import mock

class Webservice(unittest.TestCase):
  

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
    }

    self.assertEqual(1569911133, parse_json_data(sample_data))

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
    }

    self.assertEqual(1569953945, parse_json_data(sample_data))

  def test_parse_data_with_error_msg_lat_being_too_long(self):
    sample_json = {"message": "failure",
      "reason": "Latitude must be number between -90.0 and 90.0"}

    with self.assertRaisesRegexp(Exception,\
      "Latitude must be number between -90.0 and 90.0"):
      parse_json_data(sample_json)

  def test_parse_data_with_error_msg_longitude_being_too_long(self):
    sample_json = {"message": "failure",\
      "reason": "Longitude must be number between -180.0 and 180.0"}

    with self.assertRaisesRegexp(Exception,\
      "Longitude must be number between -180.0 and 180.0"):
      parse_json_data(sample_json)

  @mock.patch('src.webservice.webservice.get_data_from_url')
  @mock.patch('src.webservice.webservice.parse_json_data')
  def test_fetch_iss_fly_over_data_and_calls_service_and_parse_response_to_parse_json_data(self, mock_get_url, mock_parse):
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
    }

    mock_get_url.return_value = sample_data
    mock_parse.return_value = 1569953945
    
    fetch_iss_fly_over_data(40.73061, -73.935242)
    self.assertTrue(mock_get_url.called)

  @mock.patch('src.webservice.webservice.get_data_from_url')
  @mock.patch('src.webservice.webservice.parse_json_data')
  def test_fetch_iss_fly_over_data_and_returns_time_stamp_returned_by_parse_json_data(self, mock_parse, mock_get_url):
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
          "risetime": 1569954053
        }
      ]
    }

    mock_get_url.return_value = sample_data
    mock_parse.return_value = 1569954053
    self.assertEqual(1569954053, fetch_iss_fly_over_data(45.73061, -73.935242))


  @mock.patch('src.webservice.webservice.parse_json_data')
  def test_fetch_iss_fly_over_data_and_returns_error_returned_by_parse_json_data(self, mock_parse):
    mock_parse.side_effect=Exception('Latitude must be number between -90.0 and 90.0')

    with self.assertRaisesRegexp(Exception,\
      "Latitude must be number between -90.0 and 90.0"):
      fetch_iss_fly_over_data(455555.73061, -73.935242)

  @mock.patch('src.webservice.webservice.get_data_from_url')
  def test_fetch_iss_fly_over_data_and_returns_network_error_from_call_to_service(self, mock_get_url):
    mock_get_url.side_effect = requests.exceptions.HTTPError
    
    with self.assertRaises(requests.exceptions.HTTPError):
      fetch_iss_fly_over_data(45.73061, -73.935242)

  def test_fetch_iss_fly_over_data_returns_some_timestamp_returned_for_lat_long(self):
    self.assertTrue(fetch_iss_fly_over_data(45.73061, -73.935242)>0)

if __name__ == '__main__':
  unittest.main()
