# lib/helpers.py
from models.genre import Genre
from models.song import Song

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

def create_song():
    title = input("Enter the song's title: ")
    artist = input("Enter the song's artist: ")
    genre_id = int(input("Enter the genre's id for the song: "))
    try:
        song = Song.create(title, artist, genre_id)
        print(f'Success: {song}')
    except Exception as exc:
        print("Error creating song: ", exc)

def update_song():
    id_ = input("Enter the song's id: ")
    song = Song.find_by_id(id_)
    if song:
        try:
            title = input("Enter the song's new title: ")
            artist = input("Enter the song's new artist: ")
            genre_id = int(input("Enter the genre's new id for the song: "))
            song.title = title
            song.artist = artist
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
