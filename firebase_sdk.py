import json

from firebase_admin import credentials, initialize_app, db

url = "https://activefire-2e9a0-default-rtdb.europe-west1.firebasedatabase.app"
cred = credentials.Certificate(
    "activefire-2e9a0-firebase-adminsdk-93vo8-d7087b5c37.json"
)
app = initialize_app(
    cred,
    {
        "databaseURL": url,
    },
)

ref = db.reference("/fire_weather")

with open("fire_weather_UK_int.json", "r") as f:
    file_contents = json.load(f)
ref.set(file_contents)
