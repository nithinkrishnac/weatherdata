import requests

def get_weather_data(date):
    url = f"https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching weather data.")
        return None

def get_temperature(date):
    weather_data = get_weather_data(date)
    if weather_data:
        for item in weather_data['list']:
            if date in item['dt_txt']:
                temperature_kelvin = item['main']['temp']
                temperature_celsius = temperature_kelvin - 273.15
                return temperature_celsius
        print(f"Temperature data not available for {date}.")
    return None

def get_wind_speed(date):
    weather_data = get_weather_data(date)
    if weather_data:
        for item in weather_data['list']:
            if date in item['dt_txt']:
                wind_speed = item['wind']['speed']
                return wind_speed
        print(f"Wind speed data not available for {date}.")
    return None

def get_pressure(date):
    weather_data = get_weather_data(date)
    if weather_data:
        for item in weather_data['list']:
            if date in item['dt_txt']:
                pressure = item['main']['pressure']
                return pressure
        print(f"Pressure data not available for {date}.")
    return None

if __name__ == "__main__":
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD): ")
            temperature = get_temperature(date)
            if temperature is not None:
                print(f"Temperature on {date}: {temperature:.2f} °C")

        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD): ")
            wind_speed = get_wind_speed(date)
            if wind_speed is not None:
                print(f"Wind Speed on {date}: {wind_speed} m/s")

        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD): ")
            pressure = get_pressure(date)
            if pressure is not None:
                print(f"Pressure on {date}: {pressure} hPa")

        elif choice == "0":
            break

        else:
            print("Invalid choice. Please try again.")
