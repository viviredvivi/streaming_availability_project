import requests
import os
from tkinter import messagebox


RAPID_API_KEY = os.environ.get("RAPID_API_KEY")


def get_imdb_id(user_input, selection):

	mdblist_url = "https://mdblist.p.rapidapi.com/"

	try:
		mdblist_query = {"s": user_input}

		headers = {
			"X-RapidAPI-Host":
				"mdblist.p.rapidapi.com",
			"X-RapidAPI-Key":
			RAPID_API_KEY
		}

		response = requests.get(
			mdblist_url,
			headers=headers,
			params=mdblist_query)

		movie_data = response.json()
		imdb_id = movie_data["search"][0]["id"]

		streaming_sites = get_streaming_info(imdb_id, selection)
		streaming_info = ", "

		if selection is None:
			selection = "US"

		streaming_info = streaming_info.join(streaming_sites).title()

		if streaming_info == "Hbo":
			streaming_info = "HBO"

		if len(streaming_info) > 0:
			messagebox.showinfo(
				title="Results of your query",
				message=f"You can watch {user_input.title()}"
						f" in {selection} on: "
						f"{streaming_info}")
		elif streaming_info == "":
			messagebox.showinfo(
				title="Oops",
				message=f"Sorry, but you can't watch {user_input.title()}"
						f" in {selection}.")

	except IndexError:
		messagebox.showinfo(
			title="Something's wrong!",
			message=f"Ooops, something doesn't work properly. "
					f"Maybe you made a typo or your query "
					f"was not recognized by a database. Please try again. ")


def get_streaming_info(imdb_id, selection):

	url = "https://streaming-availability.p.rapidapi.com/get/basic"

	country = ""
	if selection == "US":
		country = "us"
	elif selection == "UK":
		country = "en"
	elif selection == "Poland":
		country = "pl"
	elif selection == "Germany":
		country = "de"
	elif selection == "Japan":
		country = "jp"
	else:
		country = "us"

	try:
		streaming_query = {
			"country": country, "imdb_id": imdb_id, "output_language": "en"
		}

		headers = {
			"X-RapidAPI-Host":
				"streaming-availability.p.rapidapi.com",
			"X-RapidAPI-Key":
			RAPID_API_KEY
		}

		response = requests.get(
			url=url,
			headers=headers,
			params=streaming_query)

		movie_data = response.json()
		streaming_info = movie_data["streamingInfo"]
		streaming_sites = []
		for key, value in list(streaming_info.items()):
			streaming_sites.append(key)

		return streaming_sites
	except IndexError:
		messagebox.showinfo(
			title="Something's wrong!",
			message=f"Ooops, something doesn't work properly."
					f"Maybe you made a typo or your query"
					f"was not recognized by a database. Please try again.")
