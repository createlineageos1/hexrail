import requests

def get_weather(city):
    url = f"http://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Weather info for {city}: {response.text}")
        else:
            print("Could not fetch weather data.")
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    city = input("Enter city name: ")
    get_weather(city)
