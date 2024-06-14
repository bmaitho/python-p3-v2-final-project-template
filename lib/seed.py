#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.song import Song

def seed_database():
    # Drop the tables if they exist and create new ones
    Genre.drop_table()
    Genre.create_table()
    Song.drop_table()
    Song.create_table()

    # Create seed data for genres
    genres = [
        "Rock",
        "Jazz",
        "Classical",
        "Hip-Hop",
        "Electronic",
        "Country",
        "Reggae",
        "Pop",
        "Blues"
    ]
    for genre_name in genres:
        Genre.create(genre_name)

    # Create seed data for songs
    songs = [
        ("Stairway to Heaven", "Led Zeppelin", 1), 
        ("So What", "Miles Davis", 2),                       # Jazz
        ("Moonlight Sonata", "Ludwig van Beethoven", 3),      # Classical
        ("Lose Yourself", "Eminem", 4),                       # Hip-Hop
        ("Clarity", "Zedd", 5),                                #   Electronic
        ("Take Me Home, Country Roads", "John Denver", 6),    # Country
        ("One Love", "Bob Marley", 7),                        # Reggae
        ("Thriller", "Michael Jackson", 8),                   #  Pop
        ("The Thrill Is Gone", "B.B. King", 9)                # Blues
    ]
    for title, artist, genre_id in songs:
        Song.create(title, artist, genre_id)

seed_database()
print("Seeded database")
