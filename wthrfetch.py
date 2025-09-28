import requests
import json

def get_weather(city):
    """
    Fetches and displays the weather for a given city using the wttr.in API.
    
    :param city: The name of the city.
    """
    # Use the JSON format from wttr.in for easy parsing
    api_url = f"https://wttr.in/{city}?format=j1"

    try:
        response = requests.get(api_url)
        response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
        
        weather_data = response.json()
        
        # --- Extract and display information ---
        current_condition = weather_data.get('current_condition', [{}])[0]
        nearest_area = weather_data.get('nearest_area', [{}])[0]
        
        city_name = nearest_area.get('areaName', [{}])[0].get('value', 'Unknown City')
        country = nearest_area.get('country', [{}])[0].get('value', 'Unknown Country')
        
        temp_c = current_condition.get('temp_C', 'N/A')
        feels_like_c = current_condition.get('FeelsLikeC', 'N/A')
        weather_desc = current_condition.get('weatherDesc', [{}])[0].get('value', 'N/A')
        humidity = current_condition.get('humidity', 'N/A')
        
        print("\n--- 🌤️ Current Weather ---")
        print(f"Location: {city_name}, {country}")
        print(f"Condition: {weather_desc}")
        print(f"Temperature: {temp_c}°C")
        print(f"Feels Like: {feels_like_c}°C")
        print(f"Humidity: {humidity}%")
        print("---------------------------\n")

    except requests.exceptions.HTTPError:
        print(f"Error: Could not find weather for '{city}'. Please check the city name.")
    except requests.exceptions.RequestException as e:
        print(f"Error: Could not connect to the weather service. {e}")
    except json.JSONDecodeError:
        print("Error: Failed to parse the response from the weather service.")

# --- Main execution block ---
if __name__ == "__main__":
    print("🌤️ Basic Weather Checker 🌤️")
    city_input = input("Enter the name of a city: ")
    
    if city_input:
        get_weather(city_input)
    else:
        print("No city entered. Exiting.")
