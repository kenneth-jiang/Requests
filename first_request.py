import pyfiglet
import termcolor
import requests
import random

def start():
	print(termcolor.colored(pyfiglet.figlet_format("Dad Jokes 3000"), color="red"))
	user_input = input("What would you like to search for? ")
	request(user_input)

def request(user_input):
	url = "https://icanhazdadjoke.com/search"
	response = requests.get(
		url, 
		headers={"Accept": "application/json"},
		params={"term": user_input}
	).json()
	api_response(response)

def api_response(response):
	if response["total_jokes"] > 1:
		print(f"There are {len(response['results'])} jokes with {response['search_term']}, here's a funny one!")
		print(random.choice(response['results'])['joke'])
	else:
		print(f"Sorry, there are no jokes with {response['search_term']}.. =(")

start()