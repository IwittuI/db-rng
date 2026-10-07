import requests
import os
from dotenv import load_dotenv

load_dotenv()

ENDPOINT = "https://apis.deutschebahn.com/db-api-marketplace/apis/timetables/v1/plan/8000105/261007/08"
CLIENT_ID = os.getenv("DB_CLIENT_ID")
API_KEY = os.getenv("DB_API_KEY")


headers = {
    "DB-Client-Id": CLIENT_ID,
    "DB-Api-Key": API_KEY,
    "accept": "application/xml"
}


response = requests.get(ENDPOINT, headers=headers)

if response.status_code != 200:
    print(f"Fehler bei der API-Abfrage: Statuscode {response.status_code}")

print(response.text)