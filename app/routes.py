import requests
import hashlib

def check_password(password):
	#get the hash of the input
	sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
	#due to k anonimity, we grab the first 5 characters of our hashed password in one variable
	#and the rest in another variable
	head,tail = sha1_password[:5], sha1_password[5:]
	#print(head)
	try:
		api = 'https://api.pwnedpasswords.com/range/' + head
		response = requests.get(api)
		#print(response.text)
		if response.status_code != 200:
			raise Exception
	except:
		return {'success': 'Failed'}

	#we define our success message to display if our password has been hasned and its count to show how many times it has been breached
	status = {
							'success': True,
							'count': 0
						}

	#we split the hashes at each line break
	for i in response.text.split("\n"):
		#we further split the hashes at the ":", giving us the count as the 1th item
		j= i.split(":")
		#we compare the first part of the split done above with the tail of our hashed password
		if j[0] == tail:
			#if the value of j[0] matches the tail of our hashed password, we update our status
			status["count"] = int(j[1])
	print(status)
check_password(input('enter a test password: '))
