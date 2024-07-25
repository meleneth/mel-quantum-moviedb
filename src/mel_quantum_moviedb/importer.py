import json
import copy

from mel_quantum_moviedb.tables import MovieDB, Movie, Rating

def import_row(row):
  if 'id' not in row : return
  if row['id'] in (14372, 415, 27318) : return
  print(row['title'])
  row = copy.deepcopy(row)
  # we should handle these things, but since we haven't yet, remove them
  row.pop('genre_ids', None)
  row.pop('year', None)
  # row.pop('ratings', None)

  ratings = row.pop('ratings', None)
  movie = Movie.find_or_create(**row)

  for rating in ratings :
    rating = copy.deepcopy(rating)
    rating['movie_id'] = movie.id
    Rating.find_or_create(**rating)


def import_files():
  filename = "tmdbList.json"

  with open(filename) as f:
    d = json.load(f)
  print("JSON parsed!")
  print("creating DB")
  MovieDB().connect("moviesdb")
  for row in d:
    import_row(row)
