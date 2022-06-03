# streaming_availability_project
GUI app that allows user to check if movie/series is available on streaming sites (like Netflix, HBO and others) in chosen country (4 to choose from – US, Poland, Germany, Japan). 
Uses two APIs in the process.

This app has a simple GUI made with tkinter module. 
User can enter the title of a movie or series. After clicking search, messagebox with information about streaming services (eg. "You can watch Breaking Bad in US on: Netflix") will appear. If movie/series is not streaming in given country, the message will tell it (I've also implemented a few other cases that handles user-generated errors). User can also change the country of query. I've implemented four possibilities (it can be of course easily increased).

How does it all started? 
So I've been learning to handle APIs for some time now and I wanted to do a project that will help to solve a real problem (because in the world of streaming wars it will be easier and quicker to use app like this than to search all of the services for desired show) and will also show my new skills. I found a problem, than I've made a solution – with a little help of two APIs. These are MDBList and Streaming Availability – both reached in freemium mode with RapidAPI.

How does it all work?
I've divided my project into two separate files – main.py, where you can find the UI and the trigger function (get_movie_title – it fetches entered title and country selection) and functions.py, where the two main functions are. Each of the functions requests data from different API. The first one, get_imdb_id, uses MDBlist API and it not only gets imdb ID from user input (it works like this: user input -> request to API with the title -> dictionary comprehension to get imdb ID) but it also calls the second function, after passing into it imdb ID. Then get_streaming_info, second function, returns to the first a list of streaming sites (after a request to Streaming Availability API). The first function combine it with selection of country (also used by get_streaming_info) to show results using tkinter messagebox. 

So that's basically it for the moment. In the past few weeks I've learnt not only how to handle APIs but also how to use environment variables (and I've implemented this here to hide my Rapid API key). This is also my first project uploaded using Git (not only uploading files to GitHub like before), so I can easily modify this repository in the future if I want to.

Feel free to use this app, have fun with it, modify if you want to and contact me if you have any questions or suggestions.

I hope that this app will help you find where your favourite shows and movies are shown! Have a nice day:)


