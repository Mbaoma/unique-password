import requests
import hashlib
import sys

def check_password(hashed_password):
	api = 'https://api.pwnedpasswords.com/range/' + hashed_password #'D869D'
	response = requests.get(api)
	if response.status_code != 200:
		print(f'Error {response.status_code}: Kindly check your work!')
	return response

def breached_passwords(matching_hashes, our_hash):
	matching_hashes = (line.split(':') for line in matching_hashes.text.splitlines())
	#we get the hashed values and the number of times they appear in the database of breached passwords
	for i, count in matching_hashes:
		#comparing the tail of our hashed password against hashes with same tail as ours in the database
		#our hashed tail is not on any server
		if i == our_hash:
			print('password appeared', count, 'times')
	print('secure password')

def pwned_api_validator(password):
	#to check if our password exists in the database of pawned passwords
	#using the SHA1 hashing method
	sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	#due to k anonimity, we grab the first 5 characters of our hashed password in one variable
	#and the rest in another variable
	head,tail = sha1_password[:5], sha1_password[5:]
	status = check_password(head)
	#refer to the function which checks if our password has been breached
	return breached_passwords(status, tail)

pwned_api_validator(input('enter password: '))

