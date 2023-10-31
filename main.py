import requests
import datetime
import config

GENDER = "male"
WEIGHT_KG = int(input("Your weight in kg: "))
HEIGHT_CM = int(input("Your height in cm: "))
AGE = int(input("Your age: "))

API_ID = config.APP_ID

API_KEY = config.API_KEY

exercise_text = input("Tell me which exercises you done: ")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

post_content = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}

connection_exercise = requests.post(
    url=exercise_endpoint, json=post_content, headers=headers
)
result = connection_exercise.json()
exercises = result["exercises"]

SHEETY_ENDPOINT = config.SHEETY_ENDPOINT

now = datetime.datetime.now()
date_now_str = now.strftime("%d/%m/%Y")
time_now_str = now.strftime("%H:%M")

USER = config.USER
PASSWORD = config.PASSWORD
TOKEN = config.TOKEN

TOKEN_header = {"Authorization": f"Bearer {config.TOKEN}"}

for exercise in exercises:
    sheety_content = {
        "workout": {
            "date": date_now_str,
            "time": time_now_str,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }

    connection_sheety = requests.post(
        url=SHEETY_ENDPOINT, json=sheety_content, headers=TOKEN_header
    )
    print(connection_sheety.json())
