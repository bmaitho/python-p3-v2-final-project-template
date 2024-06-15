# lib/helpers.py
from models.artist import Artist
from models.song import Song
from models.genre import Genre
def exit_program():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    for genre in genres:
        print(genre)

def find_genre_by_name():
    name = input("Enter the genre's name: ")
    genre = Genre.find_by_name(name)
    print(genre) if genre else print(f'Genre {name} not found')

def find_genre_by_id():
    id_ = input("Enter the genre's id: ")
    genre = Genre.find_by_id(id_)
    print(genre) if genre else print(f'Genre {id_} not found')

def create_genre():
    name = input("Enter the genre's name: ")
    try:
        genre = Genre.create(name)
        print(f'Success: {genre}')
    except Exception as exc:
        print("Error creating genre: ", exc)

def update_genre():
    id_ = input("Enter the genre's id: ")
    genre = Genre.find_by_id(id_)
    if genre:
        try:
            name = input("Enter the genre's new name: ")
            genre.name = name
            genre.update()
            print(f'Success: {genre}')
        except Exception as exc:
            print("Error updating genre: ", exc)
    else:
        print(f'Genre {id_} not found')

def delete_genre():
    id_ = input("Enter the genre's id: ")
    genre = Genre.find_by_id(id_)
    if genre:
        genre.delete()
        print(f'Genre {id_} deleted')
    else:
        print(f'Genre {id_} not found')

def list_artists():
    artists = Artist.get_all()
    for artist in artists:
        print(artist)

def find_artist_by_name():
    name = input("Enter the artist's name: ")
    artist = Artist.find_by_name(name)
    print(artist) if artist else print(f'Artist {name} not found')

def find_artist_by_id():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    print(artist) if artist else print(f'Artist {id_} not found')

def create_artist():
    name = input("Enter the artist's name: ")
    try:
        artist = Artist.create(name)
        print(f'Success: {artist}')
    except Exception as exc:
        print("Error creating artist: ", exc)

def update_artist():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        try:
            name = input("Enter the artist's new name: ")
            artist.name = name
            artist.update()
            print(f'Success: {artist}')
        except Exception as exc:
            print("Error updating artist: ", exc)
    else:
        print(f'Artist {id_} not found')

def delete_artist():
    id_ = input("Enter the artist's id: ")
    artist = Artist.find_by_id(id_)
    if artist:
        artist.delete()
        print(f'Artist {id_} deleted')
    else:
        print(f'Artist {id_} not found')

# Song functions with artist_id integration
def create_song():
    title = input("Enter the song's title: ")
    artist_id = int(input("Enter the artist's id: "))
    genre_id = int(input("Enter the genre's id: "))
    try:
        song = Song.create(title, artist_id, genre_id)
        print(f'Success: {song}')
    except Exception as exc:
        print("Error creating song: ", exc)

def update_song():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    if song:
        try:
            title = input("Enter the song's new title: ")
            artist_id = int(input("Enter the artist's new id: "))
            genre_id = int(input("Enter the genre's new id: "))
            song.title = title
            song.artist_id = artist_id
            song.genre_id = genre_id
            song.update()
            print(f'Success: {song}')
        except Exception as exc:
            print("Error updating song: ", exc)
    else:
        print(f'Song {id_} not found')


def delete_song():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    if song:
        song.delete()
        print(f'Song {id_} deleted')
    else:
        print(f'Song {id_} not found')

def list_songs():
    songs = Song.get_all()
    for song in songs:
        print(song)

def find_song_by_title():
    title = input("Enter the song's title: ")
    song = Song.find_by_title(title)
    print(song) if song else print(f'Song {title} not found')

def find_song_by_id():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    print(song) if song else print(f'Song {id_} not found')

def find_artist_by_song_id():
    id_ = input("Enter the song's id: ")
    artist = Song.find_artist_by_song_id(id_)
    print(artist) if artist else print(f'Artist for song {id_} not found')