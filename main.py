import requests
import pandas as pd
from datetime import datetime, timedelta

# Getting weather data
today = datetime.now()
week_ago = today - timedelta(days=7)
start_date = week_ago.strftime("%Y-%m-%d")
end_date = today.strftime("%Y-%m-%d")
latitude = 25.59
longitude = 85.14

# making the API call
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"
response = requests.get(url)
data = response.json()

# Processing the data with pandas
df = pd.DataFrame({
    "date" :  pd.to_datetime(data["daily"]["time"]),
    "max_temp" : data["daily"]["temperature_2m_max"],
    "min_temp" : data["daily"]["temperature_2m_min"]
})

# calculating average
df["avg_temp"] = df["max_temp"] - df["min_temp"]