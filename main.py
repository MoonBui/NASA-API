from api_requests import get_asteroid
from utils import *

def main():
    # Get date input from user and make api call
    dates = date_input()
    resp = get_asteroid(dates[0], dates[1])

    # Parse information from api call and convert to csv
    asteroids = parse_info(resp, dates[0])
    convert_csv(asteroids)

if __name__ == "__main__":
    main()