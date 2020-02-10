# UserAgents-To-Browser
Reads Excel file which contain User Agents and finds the Browser and OS Associated with them in a new Excel file

# Dependencies
	pandas,
	requests
# API
API used is from https://userstack.com/. A free key can be obtained by signing up to the free plan

# Parameters Needed
filename = 'FileToBeRead.xlsx'    
ColumnToRead = 'ColumnContaining_UserAgents'                      
YOUR_ACCESS_KEY = 'INSERT_KEY_OBTAINED_FROM_ABOVE' # Sign up for API key on https://userstack.com/
fileToCreate = 'FileToBeCreated.xlsx'

# Output 
An Excel file named "fileToCreate" defined above with two columns 'User Agent' and 'Browser'
