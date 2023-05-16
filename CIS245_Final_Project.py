import json, requests
import cred

while True:
  city = input("Please enter a city or zip code (type 'quit' to exit): ")
  if city.lower() == 'quit':
    break

  def request_information(city):
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    complete_url = f"{base_url}?q={city}&units=imperial&APPID={cred.appid}"
    return complete_url

  print("We are attempting to make connection to our weather resources...")
  
  complete_url = request_information(city)
  weather_data = requests.get(complete_url)
  
  weather_data.status_code
  
  if weather_data.json()['cod'] == '404':
    print("The city or zip code entered was not found please try entering in another city name.")
  elif weather_data.status_code != 200:
    print("There was an issue connecting to our resources. Please try again shortly.") 
  else: print("We have successfully connected!")
  
    
  def weather_for_today(weather_data):
    weather = (weather_data.json()['weather'][0]['main'])
    temperature = weather_data.json()['main']['temp']
    return weather, temperature
  
  results = weather_for_today(weather_data)
  
  city2 = str.isnumeric(city)
  if city2 == True:
    print(f'The forecast in the following zip code: {city} is {results[0]} and the current temperature is {round(results[1])}.')
  else:
    print(f'The forecast today in {city} is {results[0]} and the current temperature is {results[1]}.')