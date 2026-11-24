import requests
import smtplib
import os

# API gives weather forecast every 3 hours # city = Siliguri


OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("API_KEY")

# smtplib
email = "deysaurya@gmail.com"
app_password = os.environ.get("APP_PASSWORD")


sil_lat = 26.7271
sil_long = 88.3953

weather_params = {
    "lat":13.0827,
    "lon": 80.2707,
    "appid": api_key,
    "cnt": 4,
}

response = requests.get(OWN_Endpoint, params = weather_params)
response.raise_for_status()
weather_data = response.json()
# Challenge to check weather forecast rain or snow or not
# my trying almost same as Angela Yu

will_rain = False
for hour_data in weather_data["list"]:
    condition_code =  hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True


if will_rain:
    # Using smtplib to send email alert
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user = email, password = app_password)
        connection.sendmail(from_addr = email,
                                to_addrs = "sauryadey@yahoo.com",
                                msg = f"Subject:Its going to be rain today, Remember to bring an umbrella.\nAnd by the way you tried a lot fault is with twilio and telegram so move on\n You are doing good")

    print("Message Sent")










