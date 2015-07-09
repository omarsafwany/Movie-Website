import fresh_tomatoes
import media

#created multiple instances of Movie
dark_knight = media.Movie("The Dark Knight",
                          "The one with the Joker",
                         "http://www.dan-dare.org/FreeFun/Images/BatmanDarkKnightWallpaper1024.jpg",
                         "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                         "2008")

fast_furious = media.Movie("Fast and Furious 7",
                           "7th installment of the series",
                           "http://www.filmsy.com/wp-content/uploads/2015/02/Fast-and-Furious-7.jpg",
                           "https://www.youtube.com/watch?v=uA59s-f8WqM",
                           "2015")

the_proposal = media.Movie("The Proposal",
                           "An editor tries to avoid getting deported by marrying her assistant",
                           "https://wallpapers99.com/The_Proposal--w1280x960--77--0--images/wallpaper/1280x960/The_Proposal_10197.jpg",
                           "https://www.youtube.com/watch?v=RFL8b1p1ELY",
                           "2009")

#adding the instances to a movie array
movies = [dark_knight, fast_furious, the_proposal]
#passing movies array as argument to open movies page function
fresh_tomatoes.open_movies_page(movies)