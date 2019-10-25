from argparse import ArgumentParser
from src.webservice.webservice import *
from src.iss.iss import *

def main():
  parser = ArgumentParser()

  parser.add_argument("latitude", help="specify the latitude",\
    metavar="LATITUDE", type=float)
  parser.add_argument("longitude", help="specify the longitude",\
    metavar="LONGITUDE", type=float)

  args = parser.parse_args()
  print(compute_time_of_fly_over(\
    args.latitude, args.longitude, fetch_iss_fly_over_data))

if __name__ == "__main__":
    main()
