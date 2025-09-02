# 🌤️ Weather Advisor

The **Weather Advisor** is a smart application that uses the [Weather App](https://github.com/sidharthvijayakumar/weather-app) API to provide **personalized suggestions** based on the current weather conditions of any city.  

Instead of just showing the weather, it tells you what to do with it.  
For example:  
- ☀️ "The temperature is too high! Stay hydrated"  
- 🌧️ "Its raining take an umbrella or raincoat"  
- ❄️ "Its snowing take a jacket 🧥"  

---

## 🚀 Features
- 🔗 Integrates with the [Weather App](https://github.com/sidharthvijayakumar/weather-app) API  
- 📍 Get weather-based **advice & suggestions**  
- 🌡️ Provides clear recommendations for **hot, cold, rainy, or stormy** weather  
- 📱 Simple, clean, and mobile-friendly design  

---

## 🛠️ Tech Stack
- **Frontend**: HTML, CSS, JavaScript  
- **Backend/API**: Uses [`weather-app`](https://github.com/sidharthvijayakumar/weather-app) as the data source  
- **API**: [OpenWeatherMap](https://openweathermap.org/api) (via weather-app)  

---

## 📦 Installation & Usage

1. **Clone the repository**
   ```bash
   git clone https://github.com/sidharthvijayakumar/weather-advisor.git
   cd weather-advisor
   
## Check which Port Weather app is running on and the IP address

1. ***Update the values.yaml file
```commandline
configmap:
  data:
    #service ip of weather app(main app)
    WEATHER_SERVICE_HOST: "10.96.143.133"
    #service  port of weather app(main app)
    WEATHER_SERVICE_PORT: "8080"
```
2. *** Run bash automation.sh***
```commandline
bash automation.sh
```
