from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY="37159ac3bf9020ccfb53ad70a17732dd"

@app.route("/", methods = ["GET" , "POST"])
def home():
    weather_data = None
    error_data = None
    if request.method == "POST":
        city = request.form.get("city")
        if city :
            url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
            response = requests.get(url)
            data = response.json()

            if response.status_code == 200:
                weather_data = {
                    "city": data["name"],
                    "temp": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "wind": data["wind"]["speed"],
                    "desc": data["weather"][0]["description"].title(),
                    "icon": data["weather"][0]["icon"]
                }
            else:
                error_data = "City not found! Please enter a valid city name."
        else:
            error_data = "Please enter a city name."
    return render_template("index.html", weather=weather_data, error=error_data)

if __name__ == "__main__":
    app.run(debug = True)