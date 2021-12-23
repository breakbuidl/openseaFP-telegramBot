# importing all required libraries
import telegram
import requests
import json

baseUrl = "https://api.opensea.io/api/v1/collection/"
collections = ["cryptocoven", "infinite-grid", "tenacioustigers", "the-flower-girls", "expansionpunks"]
headers = {"Accept": "application/json"}
message = ""

for collection in collections:
	url = baseUrl + collection + "/stats"
	response = requests.request("GET", url, headers=headers)

	if response:
		r = response.json()
		m = collection + " - " + str(r['stats']['floor_price']) + "\n"
		message = "".join((message, m))
	else:
		m = "Error(" + str(response.status_code) + ") for " + collection + "\n"
		message = "".join((message, m))

message.rstrip()

bot = telegram.Bot(token='5023930853:AAEbQA6r1P_R11N87YkPV8TzRnP0EawNG4M')
bot.send_message(text= message, chat_id = 2063701906)
