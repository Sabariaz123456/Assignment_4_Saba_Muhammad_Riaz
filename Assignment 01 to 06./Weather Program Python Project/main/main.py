import requests

# Function to get weather data
def get_weather(city, api_key):
    # Base URL for OpenWeatherMap API
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # Complete URL to request weather data for the city
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"  # Using 'metric' for Celsius units
    
    # Send HTTP GET request to fetch the data
    response = requests.get(complete_url)
    
    # Check if the response status code is OK
    if response.status_code == 200:
        # Get data from the response
        data = response.json()
        
        # Check if the city was found
        if data['cod'] == '404':
            print(f"Error: City '{city}' not found.")
        else:
            # Extracting weather data
            main_data = data['main']
            weather_data = data['weather'][0]
            
            # Extract relevant information
            temperature = main_data['temp']
            pressure = main_data['pressure']
            humidity = main_data['humidity']
            description = weather_data['description']
            
            # Display the weather information
            print(f"Weather for {city.capitalize()}:")
            print(f"Temperature: {temperature}°C")
            print(f"Pressure: {pressure} hPa")
            print(f"Humidity: {humidity}%")
            print(f"Description: {description.capitalize()}")
    else:
        print("Error: Unable to fetch weather data.")

def main():
    # Get API Key from OpenWeatherMap (replace this with your own API key)
    api_key = input("Enter your OpenWeatherMap API key: ").strip()
    
    # Ask the user for the city name
    city = input("Enter the city name: ").strip()
    
    # Fetch and display weather information
    get_weather(city, api_key)

if __name__ == "__main__":
    main()
