import requests


def parse_json_data(json_data):
  if json_data['message']=='success':
    return json_data['response'][0]['risetime']
  else:
    raise Exception(json_data['reason'])

def fetch_iss_fly_over_data(lat, long, parse_json_data):
  url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n=1'.format(lat, long)
  try:
    return parse_json_data(requests.get(url).json())
  except requests.exceptions.HTTPError:
    raise requests.exceptions.HTTPError