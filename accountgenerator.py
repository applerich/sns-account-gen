# generate SNS accounts
# [@theRealChefUK]

import requests
from bs4 import BeautifulSoup as bs
from random import randint
import cfscrape

def generate(prefix, password, num):
	print("")
	accounts = []
	for i in range(int(num)):
		scraper = cfscrape.create_scraper()
		headers = {
		'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
		'origin': 'https://www.sneakersnstuff.com'
		}
		r = scraper.get("https://www.sneakersnstuff.com/en/customer/register")
		soup = bs(r.content, "html.parser")
		csrf = soup.find('input', {'name': '_AntiCsrfToken'})['value']
		number = randint(111,9999999)
		email = '{}+{}@gmail.com'.format(prefix, number)
		data = {
		'firstName': 'John',
		'lastName': 'Smith',
		'emailAddress': email,
		'password': password,
		'passwordRepeat': password,
		'gender': 'm',
		'phoneNumber': '',
		'addressLine2': '',
		'addressLine3': '',
		'postalCode': '',
		'city': '',
		'country': 'GB',
		'termsaccepted': 'true',
		'_AntiCsrfToken': csrf
		}
		r = scraper.post("https://www.sneakersnstuff.com/en/customer/register", data=data)
		if r.status_code == 200:
			accounts.append("{}:{}".format(email, password))
			print("Generated account | {}".format(email))
		else:
			print("Failed to generate account!")
	with open('accounts.txt') as file:
		for account in accounts:
			file.write("{}\n".format(account))
	return

	if __name__ == '__main__':
		print("SNS Account Generator")
		print("[@theRealChefUK]")
		prefix = input("EMAIL PREFIX: ")
		password = input("PASSWORD: ")
		num = input("# OF ACCOUNTS: ")
		generate(prefix, password, num)
