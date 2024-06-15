#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.genre import Genre
from models.song import Song
from models.artist import Artist

def seed_database():
   
    Genre.drop_table()
    Genre.create_table()
    Artist.drop_table()
    Artist.create_table()
    Song.drop_table()
    Song.create_table()

  
    genres = [
        "Afro", "Hip-Hop", "Afro-pop", "Indie rock", "Classical",
        "Country", "Reggae", "Pop", "Rap"
    ]
    for genre_name in genres:
        Genre.create(genre_name)

    artists = [
        "Tems", "Drake", "Sauti Sol", "Arctic Monkeys", "Ludwig van Beethoven",
        "John Denver", "Bob Marley", "Michael Jackson", "Kendrick Lamar"
    ]
    artist_instances = [Artist.create(name) for name in artists]

    songs = [
        ("WAIT FOR U", artist_instances[0].id, 1), 
        ("Search and Rescue", artist_instances[1].id, 2),
        ("Suzanna", artist_instances[2].id, 3),
        ("I Wanna Be Yours", artist_instances[3].id, 4),
        ("Piano Sonata", artist_instances[4].id, 5),
        ("Take Me Home, Country Roads", artist_instances[5].id, 6),
        ("One Love", artist_instances[6].id, 7),
        ("Thriller", artist_instances[7].id, 8),
        ("Rich Spirit", artist_instances[8].id, 9)
    ]
    for title, artist_id, genre_id in songs:
        Song.create(title, artist_id, genre_id)

seed_database()
print("Seeded database")
