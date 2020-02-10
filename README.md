# UserAgents-To-Browser
Reads Excel file which contain User Agents and finds the Browser and OS Associated with them in a new Excel file

# 1) Install Dependencies (if needed)
	pandas,
	requests
# 2) Sign up and obtain the API key
API used is from https://userstack.com/. A free key can be obtained by signing up to the free plan

# 3) Modify the following parameters inside 'UserAgent-Converison.py'
filename = 'FileToBeRead.xlsx'    
ColumnToRead = 'ColumnContaining_UserAgents'   
fileToCreate = 'FileToBeCreated.xlsx'	
YOUR_ACCESS_KEY = 'INSERT_KEY_OBTAINED_FROM_ABOVE' # Sign up for API key on https://userstack.com/	

# Expected Output 
An Excel file named "fileToCreate" defined above with two columns 'User Agent' and 'Browser'
