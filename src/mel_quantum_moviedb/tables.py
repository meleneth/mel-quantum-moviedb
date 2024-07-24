import os
import os.path

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Text, Boolean, Float
from sqlalchemy.orm import relationship

from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy import create_engine

class MovieDB(object):
  session = False
  db_existed = None

  @classmethod
  def connect(cls, sqlite_name, echo=False):
    db_filename = "%s.sqlite" % (sqlite_name)
    cls.db_existed = os.path.exists(db_filename)
    engine = create_engine("sqlite:///%s" % db_filename, echo=echo)
    if not cls.db_existed:
      Base.metadata.create_all(engine)
    cls.session = Session(engine)
  @classmethod
  def commit(cls):
    cls.session.commit()
  @classmethod
  def delete(cls, obj):
    cls.session.delete(obj)


class FindOrCreateMixin(object):
  @classmethod
  def find(cls, **kwargs):
    return MovieDB.session.query(cls).filter_by(**kwargs).first()
  @classmethod
  def find_or_create(cls, **kwargs):
    '''

    Creates an object or returns the object if exists
    credit to Kevin @ StackOverflow
    from: http://stackoverflow.com/questions/2546207/does-sqlalchemy-have-an-equivalent-of-djangos-get-or-create

    '''
    instance = MovieDB.session.query(cls).filter_by(**kwargs).first()
    if instance:
        return instance
    instance = cls(**kwargs)
    MovieDB.session.add(instance)
    MovieDB.commit()
    return instance

Base = declarative_base(cls=FindOrCreateMixin)

class Country(Base):
  __tablename__ = "countries"

  id = Column(Integer, primary_key=True)
  name = Column(String)

class Rating(Base):
  __tablename__ = "ratings"

  id = Column(Integer, primary_key=True)
  name = Column(String)

class Genre(Base):
  __tablename__ = "genres"

  id = Column(Integer, primary_key=True)
  name = Column(String)

class Movie(Base):
  __tablename__ = "movies"

  id = Column(Integer, primary_key=True)
  name = Column(String)
  adult = Column(Boolean)
  backdrop_path = Column(String)
  # TODO genres
  original_language = Column(String)
  original_title = Column(String)
  overview = Column(Text)
  popularity = Column(Float)
  poster_path = Column(String)
  release_date = Column(String)
  title = Column(String)
  video = Column(Boolean)
  vote_average = Column(Float)
  vote_count = Column(Integer)
  tagline = Column(String)
  runtime = Column(Integer)
  runtime_hm = Column(String)
  collection = Column(String)
  # TODO ratings
  poster = Column(String)
  bg = Column(String)
  found = Column(Boolean)

class MovieGenres(Base):
  __tablename__ = "movie_genres"

  id = Column(Integer, primary_key=True)
  movie_id = Column(Integer, ForeignKey('movies.id'))
  genre_id = Column(Integer, ForeignKey('genres.id'))

class MovieRatings(Base):
  __tablename__ = "movie_ratings"

  id = Column(Integer, primary_key=True)
  movie_id = Column(Integer, ForeignKey('movies.id'))
  rating_id = Column(Integer, ForeignKey('ratings.id'))

