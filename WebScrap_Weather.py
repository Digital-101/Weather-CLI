# -*- coding: utf-8 -*-
"""
Created on Fri Aug 26 06:03:00 2022

@author: User
"""

from bs4 import BeautifulSoup
import requests

headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 

def GetWeather(city):

    city = city.replace(" ", "+")

    # get city from google search
    response = requests.get(f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)

    print("Retrieving...\n")

    webscrap = BeautifulSoup(response.text, 'html.parser')
    
    # select div/span class from html :-)
    location = webscrap.select('#wob_loc')[0].getText().strip()
    time = webscrap.select('#wob_dts')[0].getText().strip()
    desc = webscrap.select('#wob_dc')[0].getText().strip()
    weather = webscrap.select('#wob_tm')[0].getText().strip()
    
    # print results
    print(location)
    print("Today: ", time)
    print("Condition " ,desc)
    print("Temperature:",weather+"°C")
 
 
print("=========== GET WEATHER ===========")
city = input("Enter Name of City: ")
city = city +" weather"

GetWeather(city)

print("\n======= Have a Blessed Day =======")