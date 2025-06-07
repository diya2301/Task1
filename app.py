import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

API_KEY = "df23d88e5b858293ef360bc1cf3ee643"
CITY = "Mumbai"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Extract temperature and time
forecast_data = []
for entry in data['list']:
    forecast_data.append({
        "datetime": entry["dt_txt"],
        "temperature": entry["main"]["temp"],
        "humidity": entry["main"]["humidity"]
    })

df = pd.DataFrame(forecast_data)

# Plotting
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x="datetime", y="temperature", label="Temperature (°C)")
sns.lineplot(data=df, x="datetime", y="humidity", label="Humidity (%)")
plt.xticks(rotation=45)
plt.title(f"5-Day Weather Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Values")
plt.legend()
plt.tight_layout()
plt.show()
