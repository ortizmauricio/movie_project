
class Movie():
    """This movie class allows storage for
        movie titles, storylines, poster images, and trailers.
        The instances are found in the entertainment_center.py file"""
    
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        
        
        def show_trailer(self):
            """Opens movie trailer for instance"""
            webbrowser.open(self.trailer_youtube_url)
