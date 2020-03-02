from random import choice
from tmdbv3api import TMDb, Movie

def search_movie(query):
    tmdb = TMDb()
    tmdb.api_key = 'be9603d000eacf54e7993c25318325d4'
    movie = Movie()

    result = movie.search(query)
    number_of_movies = len(result)
    
    if number_of_movies == 0:
        print("SORRY, I CAN'T FIND ANYTHING, PLEASE TRY ANOTHER PHRASE")
    else:
        random_movie_title = choice(result).title
        print(f'I have found {number_of_movies} movies, here is a random choice for you:')
        print(f'Title: {random_movie_title}')
        for res in result:
            if res.title == random_movie_title:
                if res.overview == "":
                    print('Sorry, no plot available :c')
                else:
                    print(f'Movie id: {res.id}')
                    print(f'Plot: {res.overview}')
                    print(f'Released in {res.release_date}')

                    similar = movie.similar(res.id)
                    for sim in similar:
                        print(f'Similar movie: {sim} (movie id: {sim.id}), released in {sim.release_date}')
                        break
                break

def main():
    print('WELCOME TO MOVIE GENERATOR')

    while True:
        movie_title = input('PLEASE ENTER THE TITLE: ')

        if movie_title == "" or movie_title == " ":
            print("Please enter a query")
        elif len(movie_title) <= 1:
            print('Query must be longer than 2 letters long')
        else:
            search_movie(movie_title)

main()
