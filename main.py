import requests
import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--oras", required=True, help="Numele orașului.")
    parser.add_argument("--key", required=True, help="API Key")
    return parser.parse_args()


def main():
    args = parse_args()
    api = f"https://api.openweathermap.org/data/2.5/weather?q={args.oras}&appid={args.key}&units=metric"
    info = requests.get(api)
    date = info.json()

    try:
        temp = date["main"]["temp"]
        vitezaVantului = date["wind"]["speed"]
        latitudine = date["coord"]["lat"]
        longitudine = date["coord"]["lon"]
        descriere = date["weather"][0]["description"]
        country = date["sys"]["country"]

        print(f"Temperatură: {int(temp)} grade celsius")
        print(f"Viteza vântului: {vitezaVantului}")
        print(f"Latitudine: {latitudine}")
        print(f"Longitudine: {longitudine}")
        print(f"Descriere: {descriere}")
        print(f"Țara de origine: {country}")
    
    except:
        print("Oraș scris incorect sau inexistent")
    

if __name__ == '__main__':
    main()

