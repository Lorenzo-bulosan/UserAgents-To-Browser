"""
Created on Mon Feb 10 18:37:16 2020
@author: lorenzo
API used: https://userstack.com/

"""
# Important Libraries used
import requests
import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

#%% Update with your own parameters
filename = 'FileToBeRead.xlsx'                     # File to read
ColumnToRead = 'ColumnContaining_UserAgents'       # Column to Read
YOUR_ACCESS_KEY = 'INSERT_KEY_OBTAINED_FROM_ABOVE' # Sign up for API key on https://userstack.com/
fileToCreate = 'FileToBeCreated.xlsx'              # Name of file to be created
 
#%% Function to find OS and Browser of an user agent
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
	  
	# Return result
	result = Browser_Name + ' ' + Browser_Version  + ' ' + OS
	return result

#%% Read CSV file
print('Reading the file: ' + filename)
Alldata = pd.read_excel(filename, sheetname='Sheet1') 
UserAgentColumn = Alldata[ColumnToRead]

#%% Converting UserAgent data into OS
Results_Browser = []
sizeOfdata = str(len(Alldata))

print('Obtaining OS and Browser from User Agent')
for i in Alldata.index:
	User_Agent = UserAgentColumn[i] # each user agent in the excel file
	result = ExploreUserAgent(User_Agent, YOUR_ACCESS_KEY) # Calling main function above
	Results_Browser.append(result)
	print('In progress: ' + str(i) + ' of ' + sizeOfdata)

#%% Write to CSV file
print('Creating Excel File')
df = pd.DataFrame({'User Agent':UserAgentColumn,
                   'Browser':Results_Browser})

writer = ExcelWriter(fileToCreate) # Name of file to create
df.to_excel(writer,'Sheet1',index=False)
writer.save()

print('DONE')
	

#%% Sample data from api result
#{
#'ua': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Safari/605.1.15', 'type': 'browser', 'brand': 'Apple', 'name': 'Mac', 'url': 'https://www.apple.com/', 
#'os': {'name': 'macOS 10.15 Catalina', 'code': 'macos_10_15', 'url': 'https://en.wikipedia.org/wiki/MacOS_Catalina', 'family': 'macOS', 'family_code': 'macos', 'family_vendor': 'Apple Inc.', 'icon': 'https://assets.userstack.com/icon/os/macosx.png', 'icon_large': 'https://assets.userstack.com/icon/os/macosx_big.png'}, 
#'device': {'is_mobile_device': False, 'type': 'desktop', 'brand': 'Apple', 'brand_code': 'apple', 'brand_url': 'https://www.apple.com/', 'name': 'Mac'}, 
#'browser': {'name': 'Safari', 'version': '13.0.3', 'version_major': '13', 'engine': 'WebKit'}, 
#'crawler': {'is_crawler': False, 'category': None, 'last_seen': None}
#}