import movie
import fresh_tomatoes


'''6 of my favorite movies have been instantiated
 below as Movie objects, with their
titles, storylines, poster images, and youtube trailers'''

lotr1 = movie.Movie(
    "Lord of the Rings: The Fellowship of the Ring",
    "In a small village in the Shire, a young Hobbit named Frodo \
    (Elijah Wood) has been entrusted with an ancient Ring.",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/The_Lord_of_the_Rings_The_Fellowship_of_the_Ring_%282001%29_theatrical_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=aStYWD25fAQ")


lotr2 = movie.Movie(
    "Lord of the Rings: The Two Towers",
    "While Frodo and Sam edge closer to Mordor with the help of \
    the shifty Gollum, the divided fellowship makes a stand against \
    Sauron's new ally, Saruman, and his hordes of Isengard.",
    "https://upload.wikimedia.org/wikipedia/en/a/ad/Lord_of_the_Rings_-_The_Two_Towers.jpg", # noqa
    "https://www.youtube.com/watch?v=LbfMDwc4azU")

lotr3 = movie.Movie(
    "Lord of the Rings: The Return of the King",
    "The former Fellowship of the Ring prepare for the final \
    battle for Middle Earth, while Frodo (Elijah Wood) & Sam \
    (Sean Astin) approach Mount Doom to destroy the One Ring.",
    "https://upload.wikimedia.org/wikipedia/en/9/9d/Lord_of_the_Rings_-_The_Return_of_the_King.jpg", # noqa
    "https://www.youtube.com/watch?v=r5X-hFf6Bwo")

interstellar = movie.Movie("Interstellar",
    "Interstellar chronicles the adventures of a group of explorers who make \
    use of a newly discovered wormhole to surpass the limitations on human \
    space travel and conquer the vast distances involved in an interstellar \
    voyage.",
    "https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=2LqzF5WauAw")

inception = movie.Movie(
    "Inception",
    "A skilled extractor is offered a chance to regain his old life as payment \
    for a task considered to be impossible.",
    "https://upload.wikimedia.org/wikipedia/en/2/2e/Inception_%282010%29_theatrical_poster.jpg", # noqa
    "https://www.youtube.com/watch?v=YoHD9XEInc0")

the_dark_knight = movie.Movie(
    "The Dark Knight",
    "Bruce Wayne/Batman (Bale), James Gordon (Oldman) and Harvey Dent \
    (Eckhart) form an alliance to dismantle organized crime in Gotham City, \
    but are menaced by a criminal mastermind known as the Joker (Ledger) \
    who seeks to undermine Batman's influence and create chaos.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=r94bLJi3P2c")

'''these movies are added to a list and displayed on a web page with the
open_movies_page method from fresh_tomatoes.py'''

movies_list = [lotr1, lotr2, lotr3, interstellar, inception, the_dark_knight]
fresh_tomatoes.open_movies_page(movies_list)
