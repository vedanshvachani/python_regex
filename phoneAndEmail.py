import re
def CheckPhoneNumber(number):
	phoneRegex = re.compile(r'''
	(\+91|0) #country code
	-
	(\d{10}) #number of digits
	''',re.VERBOSE)
	return(phoneRegex.findall(number))
def CheckEmailId(email):
	emailRegex = re.compile(r'''
	[a-z0-9_.+]+
	@
	[a-z]+
	.com
	''',re.VERBOSE|re.IGNORECASE)
	return(emailRegex.findall(email))
def CheckUsername(name):
	usernameRegex = re.compile(r'\w+')
	return (usernameRegex.findall(name))
username = raw_input("enter the username : ")
email = raw_input("enter the email id : ")
phoneNumber = raw_input("enter the phone number : ")
if(CheckUsername(username) and CheckEmailId(email) and CheckPhoneNumber(phoneNumber)):
	print ("Success")




