#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.song import Song
from models.artist import Artist

def seed_database():
    # Drop the tables if they exist and create new ones
    Genre.drop_table()
    Genre.create_table()
    Artist.drop_table()
    Artist.create_table()
    Song.drop_table()
    Song.create_table()

    # Create seed data for genres
    genres = [
        "Rock", "Jazz", "Classical", "Hip-Hop", "Electronic",
        "Country", "Reggae", "Pop", "Blues"
    ]
    for genre_name in genres:
        Genre.create(genre_name)

    # Create seed data for artists
    artists = [
        "Led Zeppelin", "Miles Davis", "Ludwig van Beethoven", "Eminem", "Zedd",
        "John Denver", "Bob Marley", "Michael Jackson", "B.B. King"
    ]
    artist_instances = [Artist.create(name) for name in artists]

    # Create seed data for songs
    songs = [
        ("Stairway to Heaven", artist_instances[0].id, 1), 
        ("So What", artist_instances[1].id, 2),
        ("Moonlight Sonata", artist_instances[2].id, 3),
        ("Lose Yourself", artist_instances[3].id, 4),
        ("Clarity", artist_instances[4].id, 5),
        ("Take Me Home, Country Roads", artist_instances[5].id, 6),
        ("One Love", artist_instances[6].id, 7),
        ("Thriller", artist_instances[7].id, 8),
        ("The Thrill Is Gone", artist_instances[8].id, 9)
    ]
    for title, artist_id, genre_id in songs:
        Song.create(title, artist_id, genre_id)

seed_database()
print("Seeded database")
