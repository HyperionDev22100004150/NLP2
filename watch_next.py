import spacy
nlp = spacy.load('en_core_web_md')

# Read in the movies.txt file. Each separate line is a description of a different movie.

movies = {}
with open('movies.txt', 'r') as file:
  for line in file:
    movie_title, movie_description = line.split(' :')
    movies[movie_title] = movie_desciption

# Your task is to create a function to return which movies a user would watch next if they have watched Planet Hulk with the description
# “Will he save their world or destroy it? 
#  When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle 
#  and launch him into space to a planet where the Hulk can live in peace. 
#  Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”

planet_hulk = “Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator.”

# The function should take in the description as a parameter and return the title of the most similar movie.


def similar_to(movie):
    watch_next = ''
    similarity = 0

    for movie_title, movie_description in movies.items():  
        for token in movie:
            token = nlp(token)
            for token_ in movie_description:
                token_ = nlp(token_)
                if token.similarity(token_) > similarity:
                  similarity = token.similarity(token_)
                  watch_next = movie_title
                else:
                  continue
              
    print(f'We suggest you to watch {watch_next} it has {similarity} similarity with {movie}. Here is the description of the movie: {movies[movie_title]}')
   

similar_to(planet_hulk)
