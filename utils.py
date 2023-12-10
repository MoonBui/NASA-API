import json
import pandas as pd


# Parsing information from response
def parse_info(resp: str, date:str) -> list:
    data = json.loads(resp)['near_earth_objects'][date]
    asteroids = []

    for i in range(len(data)):

        result = {
            'name': data[i]['name'],
            'id' : data[i]['id'],
            'date': date,
            'estimated_diameter_max':data[i]['estimated_diameter']['miles']['estimated_diameter_max'],
            'estimated_diameter_min': data[i]['estimated_diameter']['miles']['estimated_diameter_min'],
            'absolute_magnitude_h': data[i]['absolute_magnitude_h'],
            'is_potentially_hazardous_asteroid': data[i]['is_potentially_hazardous_asteroid'],
            'relative_velocity': data[i]['close_approach_data'][0]['relative_velocity']['miles_per_hour'],
            'miss_distance': data[i]['close_approach_data'][0]['miss_distance']['miles']
        }
    
        asteroids.append(result)

    return asteroids


# Getting date range for user input
# For this case, assume start and end date to be the same
def date_input() -> tuple[str, str]:
    start = input("Enter a start date in YYYY-MM-DD: ")
    end = input("Enter an end date in YYYY-MM-DD: ")

    return (start.strip(), end.strip())

# Convert list of objects into csv file
def convert_csv(asteroids: list):
    df = pd.DataFrame(asteroids)
    df.to_csv('asteroids.csv', index=False, header=True)