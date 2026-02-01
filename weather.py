import requests
import matplotlib.pyplot as plt

API_KEY = "67d392e1a3cef891e5cf8dc721aa9da1"  
CITY = "Hyderabad"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"
response = requests.get(URL)
data = response.json()
temperature = data["main"]["temp"]
humidity = data["main"]["humidity"]
pressure = data["main"]["pressure"]
labels = ["Temperature (°C)", "Humidity (%)", "Pressure (hPa)"]
values = [temperature, humidity, pressure]

plt.figure(figsize=(8, 5))
plt.bar(labels, values)
plt.title(f"Weather Dashboard (Bar Graph) - {CITY}")
plt.ylabel("Values")
plt.xlabel("Weather Parameters")
plt.grid(axis="y")
plt.show()
