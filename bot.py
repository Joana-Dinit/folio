#PULSE: DAILY SUMMARY BOT

import requests
from datetime import date

def get_weather(city="Thiruvananthapuram"):
    url = f"https://wttr.in/{city}?format=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text.strip()

    except Exception as e:
        return f"Weather unavailable ({e})"
  
def get_quote():
    return "Quote placeholder"
  
def build_summary():
    weather = get_weather()
    quote = get_quote()

    summary = f"""
Pulse Daily Summary
Weather:
{weather}
Today's Quote:
{quote}
"""
    return summary

def run():
    summary = build_summary()

    print(summary)

    with open("daily_summary.txt", "w") as f:
        f.write(summary)


if __name__ == "__main__":
    run()
