# TODO:
# Potrebno je implementirati konstruktor za razred Movie.
# Konstruktor prima dva argumenta, ime filma i godinu.
# Razred sadrzi dvije varijable instance (atribute): ime filma i godinu.
# Razred ⁠ Movie ⁠ morate iskoristiti u drugim podzadacima u ovom projektu.

import sqlite3
from datamodel.movie import Movie

class View:

    def __init__(self, name):
        self.name = name

    def movies(self):
        # TODO:
        # Potrebno je implementirati metodu `movies`.
        # Zadatak metode je spojiti se na bazu podataka imena `self.name`.
        # Metoda zatim mora iz baze dohvatiti sve filmove iz tablice `movies`.
        # Stupci u tablici se zovu `title` i `year`.
        # Metoda mora vratiti listu objekata klase `Movies`.
        # Primjer baze podataka nalazi se u `test_data/movies.db`
        # Baza podataka je Sqlite.
        movies = []
        conn = sqlite3.connect(self.name)
        cursor = conn.cursor()

        cursor.execute("SELECT title, year FROM movies")

        rows = cursor.fetchall()
        for row in rows:
            title, year = row
            movies.append(Movie(title, year))

        conn.close()

        return movies
class Movie:
    def _init_(self, title, year):
        self.title = title
        self.year = year
from datamodel.movie import Movie
import json


class Parser:

    def parse(self, file_name):
        # Parse JSON from file with file_name
        # Returns list of Movie objects
        movies = []
        with open(file_name, 'r') as file:
            # TODO:
            # Parsirajte JSON datoteku, pomocu ⁠ json ⁠ paketa.
            # Potrebno je iz liste filmova izvuci ime filma i godinu filma.
            # Primjer datoteke nalazi se u ⁠ test_data/movies.json ⁠
            # Metoda mora vracati listu objekata razreda ⁠ Movie ⁠.
            return movies