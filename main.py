import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="Obține date meteo despre un anume oraș.")
    parser.add_argument("--oras", required=True, help="Numele orașului.")
    parser.add_argument("--key", required=True, help="API Key")
    return parser.parse_args()

def get_weather_data(oras, api_key):
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={oras}&appid={api_key}&units=metric"
    response = requests.get(api_url)
    response.raise_for_status()
    return response.json()

def print_weather_info(data):
    temp = data["main"]["temp"]
    wind_speed = data["wind"]["speed"]
    latitude = data["coord"]["lat"]
    longitude = data["coord"]["lon"]
    description = data["weather"][0]["description"]
    country = data["sys"]["country"]

    print(f"Temperatură: {int(temp)} grade celsius")
    print(f"Viteza vântului: {wind_speed}")
    print(f"Latitudine: {latitude}")
    print(f"Longitudine: {longitude}")
    print(f"Descriere: {description}")
    print(f"Țara de origine: {country}")

def main():
    args = parse_args()

    try:
        weather_data = get_weather_data(args.oras, args.key)
        print_weather_info(weather_data)
    except requests.exceptions.RequestException as e:
        print(f"A apărut o eroare: {e}")
    except KeyError:
        print("Numele orașului este incorect")

if __name__ == '__main__':
    main()
