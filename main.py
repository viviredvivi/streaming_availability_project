from functions import get_imdb_id
from tkinter import *
from tkinter import messagebox


def get_movie_title():
    title_data = movie_entry.get()
    title_data.lower()
    if len(title_data) == 0:
        messagebox.showinfo(title="Oops",
                            message="Please don't leave "
                                    "the field for a title empty!")
    else:
        try:
            selection = country_listbox.get(country_listbox.curselection())
            get_imdb_id(title_data, selection)
        except TclError:
            selection = country_listbox.select_set(0)
            get_imdb_id(title_data, selection)


user_interface = Tk()
user_interface.title("Movie/series finder")
user_interface.config(padx=35, pady=35, bg="white")

movie_streaming_us = Label(text="Find out if and where it's streaming!",
                           font=("Courier", 25, "bold"),
                           bg="white", fg="black")
movie_streaming_us.grid(column=0, row=0, padx=35, pady=35, columnspan=3)

movie_title = Label(text="Enter the title of a movie or series "
                    "that you want to search for:",
                    bg="white", fg="black")
movie_title.grid(column=0, row=1, sticky="E")

movie_entry = Entry(width=20, highlightthickness=0, bg="white", fg="black")
movie_entry.grid(column=1, row=1)
movie_entry.focus()

search = Button(text="Search",
                width=12, pady=5, highlightthickness=0,
                bg="white", fg="black", command=get_movie_title)
search.grid(column=2, row=1)

country_listbox = Listbox(height=4)
countries = ["US", "Poland", "Germany", "Japan"]
for country in countries:
    country_listbox.insert(countries.index(country), country)
country_listbox.select_set(0)
country_listbox.grid(column=1, row=2)

country_label_title = Label(text="Currently chosen country is highlighted. \n"
                                 "Click to change your choice "
                                 "and search in a different area:",
                            bg="white", fg="black")
country_label_title.grid(column=0, row=2, sticky="E")

user_interface.mainloop()
