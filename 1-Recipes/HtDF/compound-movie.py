# Design a data definition to represent a movie, including
# title, budget, year released ,and visited or not.
# To help you to create some examples, find some interesting movie facts below:
# "Titanic" - budget: 200000000 released: 1997
# Design a function that consumes unvisited Movie then mark it as visited and print its info.

# 1- Define possible Structure
class Movie(object):
    title = ''
    budget = ''
    year = 1950
    watched = False
    def __init__(self, title, budget, year ):
        self.id = title[0:2] + year [year.length-2 :year.length]
        self.title = title
        self.budget = budget
        self.year = year

# 2- Type Comment
# Movie is a Movie(String, Number, Integer)

# 3- INTERPRETATION: a movie with title, budget in USD, and year released in respective

# 4- Data Examples
movie1 = Movie('Titanic', 200000000, 1997)
movie2 = Movie('Avatar', 237000000, 2009)
movie3 = Movie('The Avengers', 220000000, 2012)

# 5- Data Driven Template
def fn_for_Movie(movie):
    return (... movie.title
                movie.budget
                movie.year
                movie.watched)

# Movie -> None

# Purpose: consumes un-Watched Movie then mark it as watched

#
# def mark_watched(m):
#     return True


# Unit Tests and Examples:
# < Tests are done on Testing Files >


#
def mark_watched(m):
    m.watched = True
    return m.watched

# i watched vedio by id: Ti97
ids = [Ti97]
movies = [movie1, movie2, movie3]
for movie in movies:
    if (movie.id == ids[0])
        mark_watched(movie)

for movie in movies:
    if (movie.watched == True ):
        print(movie.title, movie.budget, movie.year)
