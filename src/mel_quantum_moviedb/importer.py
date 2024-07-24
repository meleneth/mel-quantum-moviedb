import json
import copy

from mel_quantum_moviedb.tables import MovieDB, Movie

def import_row(row):
  print(row)
  row = copy.deepcopy(row)
  # we should handle these things, but since we haven't yet, remove them
  row.pop('genre_ids', None)
  row.pop('ratings', None)
  row.pop('year', None)
  Movie.find_or_create(**row)

def import_files():
  filename = "tmdbList.json"

  with open(filename) as f:
    d = json.load(f)
  print("JSON parsed!")
  print("creating DB")
  MovieDB().connect("moviesdb")
  for row in d:
    import_row(row)
