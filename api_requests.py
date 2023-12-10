from dotenv import load_dotenv
import requests
import os

load_dotenv()
URL_ENDPOINT = "https://api.nasa.gov/neo/rest/v1/feed?"
API_KEY= os.environ['KEY']


# Input start and end date to get asteroid of that day
def get_asteroid(start:str, end:str) -> str:
    response = requests.get(URL_ENDPOINT, params={'start_date': start, 'end_date': end, 'api_key': API_KEY})
    return response.text

