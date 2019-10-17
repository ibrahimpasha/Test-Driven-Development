import requests

def parse_json_data(json_data):
  if json_data['message']=='success':
    return json_data['response'][0]['risetime']
  else:
    raise Exception(json_data['reason'])

def get_data_from_url(url):
    return requests.get(url).json()

def fetch_iss_fly_over_data(lat, long):
  try:
    url = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}&n=1'.format(lat, long)
    json_data = get_data_from_url(url)
    return parse_json_data(json_data)
  except requests.exceptions.HTTPError:
    raise requests.exceptions.HTTPError