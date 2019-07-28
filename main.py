import requests, math
from colorama import Fore, init

myApiKey = 'Add your openweathermap.org apy key here';
api_address = 'http://api.openweathermap.org/data/2.5/weather?APPID=' + myApiKey + '&q=';

def Hi():
    print(Fore.CYAN + ',,,'.center(40))
    print('(o o)'.center(40))
    print('----oOO--( )--OOo----'.center(40))
    print(Fore.YELLOW + "Weather app (Console)".center(40))
    print(Fore.CYAN + '---------------------'.center(40),end="")
    print(Fore.YELLOW + '''
         Author   Saul Lara
         Date     27/07/2019
         Github   github.com/saul-lara
        ''')

def main():
    print(" Name of city " + Fore.CYAN ,end=">> " + Fore.YELLOW)
    city = input()
    url = api_address + city
    try:
        json_data = requests.get(url).json()
        description = json_data['weather'][0]['description']
        temp = json_data['main']['temp'] - 273.15
        humidity = json_data['main']['humidity']
        print()
        print(" " + Fore.CYAN + "City: " + Fore.YELLOW + json_data['name'] + " , " + json_data['sys']['country'])
        print(" " + Fore.CYAN + "Weather: " + Fore.YELLOW + description)
        print(" " + Fore.CYAN + "Temperature: " + Fore.YELLOW + str(math.ceil(temp)) + "°C")
        print(" " + Fore.CYAN + "Humidity: " + Fore.YELLOW + str(humidity) + "%")
        print()
        input(" Press any key to exit :) ")
    except:
        print(' An error occurred requesting information. :( ')

init()
Hi()
main()