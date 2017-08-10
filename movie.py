
import webbrowser

class Movie():

    """This class defines a movie object that contains its title, storyline,
    poster image, and youtube trailer. The method show_trailer() plays the
    youtube trailer for the movie in the default web browser. """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube


    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
