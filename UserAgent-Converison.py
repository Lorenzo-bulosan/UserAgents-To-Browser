# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 18:37:16 2020
@author: loren

"""

# Important Libraries used
import requests
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# Function to find OS and Browser of an user agent
def ExploreUserAgent (User_Agent, YOUR_ACCESS_KEY):
	
	# Set up Parameters
	params = {
	  'access_key': YOUR_ACCESS_KEY,
	  'ua': User_Agent
	}
	
	# Call API
	api_result = requests.get('http://api.userstack.com/detect', params)
	
	# Format Data Results
	OS = api_result.json()['os']['name']
	Browser_Name = api_result.json()['browser']['name']
	Browser_Version = api_result.json()['browser']['version']
	  
	result = Browser_Name + ' ' + Browser_Version  + ' ' + OS
	print(result)
	
	return result

# Read CSV file
User_Agent = ''
YOUR_ACCESS_KEY = '15411849927d19358edcdaa2e34a07d4' #Signed up and obtained key for their API

# Write to CSV file