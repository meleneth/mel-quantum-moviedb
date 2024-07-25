from mel_quantum_moviedb.tables import Movie, MovieDB

def query_data():
  MovieDB().connect("moviesdb")
  movie = Movie.find(id=2907)
  print(movie.ratings)
