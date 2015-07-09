import webbrowser

class Movie():
    def __init__(self, movie_title, movie_story, poster_image_url, trailer_youtube_url, movie_release_date):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.release_date = movie_release_date
        
    
    def show_trailer(self):
        webbrowser.open(self.trailer)