# Phase 3 CLI+ORM Project Template
## Learning Goals
- Discuss the basic directory structure of a CLI.
- Outline the first steps in building a CLI.
## Introduction
This project is a Command Line Interface (CLI) application designed to manage a music database, incorporating an Object-Relational Mapping (ORM) to handle data persistence. The application allows users to manage artists, songs, and genres, providing a comprehensive tool for organizing and accessing music-related data. Users can perform a variety of operations, including creating, reading, updating, and deleting records in the database. The CLI guides the user through these tasks with a menu-driven interface, making it straightforward to interact with the underlying data.

The application is structured to ensure a clear separation of concerns, with distinct modules for the user interface, data persistence, and business logic. This modular design facilitates easy maintenance and scalability, allowing for future enhancements and modifications. By leveraging SQLite for database management and Python for the CLI and ORM, this project provides a robust and efficient solution for managing music data.

## module and directory structure
```console
.
├── Pipfile
├── Pipfile.lock
├── README.md
└── lib
    ├── models
    │   ├── __init__.py
    │   ├── genre.py
    │   ├── song.py
    │   └── artist.py
    ├── cli.py
    ├── debug.py
    └── helpers.py
```
 ---
## Generating Your Environment
You might have noticed in the file structure- there's already a Pipfile!

Install any additional dependencies you know you'll need for your project by adding them to the Pipfile. Then run the commands:

```console
Copy code
pipenv install
pipenv shell
```
 ## You can run the CLI with python lib/cli.py. The CLI will ask for input, do some work, and accomplish some sort of task.

## This project has a CLI in lib/cli.py that looks like this:

```py
# lib/cli.py

from helpers import exit_program, list_genres, find_genre_by_name, find_genre_by_id
from helpers import create_genre, update_genre, delete_genre, create_song, update_song
from helpers import delete_song, list_songs, find_song_by_id, find_song_by_title
from helpers import list_artists, find_artist_by_name, find_artist_by_id
from helpers import create_artist, update_artist, delete_artist, find_artist_by_song_id

def main_menu():
    while True:
        print("\nMain Menu:")
        print("1. List Genres")
        print("2. Find Genre by Name")
        print("3. Find Genre by ID")
        print("4. Create Genre")
        print("5. Update Genre")
        print("6. Delete Genre")
        print("7. List Songs")
        print("8. Find Song by Title")
        print("9. Find Song by ID")
        print("10. Create Song")
        print("11. Update Song")
        print("12. Delete Song")
        print("13. List Artists")
        print("14. Find Artist by Name")
        print("15. Find Artist by ID")
        print("16. Create Artist")
        print("17. Update Artist")
        print("18. Delete Artist")
        print("19. Find Artist by Song ID")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            list_genres()
        elif choice == '2':
            find_genre_by_name()
        elif choice == '3':
            find_genre_by_id()
        elif choice == '4':
            create_genre()
        elif choice == '5':
            update_genre()
        elif choice == '6':
            delete_genre()
        elif choice == '7':
            list_songs()
        elif choice == '8':
            find_song_by_title()
        elif choice == '9':
            find_song_by_id()
        elif choice == '10':
            create_song()
        elif choice == '11':
            update_song()
        elif choice == '12':
            delete_song()
        elif choice == '13':
            list_artists()
        elif choice == '14':
            find_artist_by_name()
        elif choice == '15':
            find_artist_by_id()
        elif choice == '16':
            create_artist()
        elif choice == '17':
            update_artist()
        elif choice == '18':
            delete_artist()
        elif choice == '19':
            find_artist_by_song_id()
        elif choice == '0':
            exit_program()
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main_menu()


```
### The helper functions are located in lib/helpers.py:

```py

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

def create_song():
    title = input("Enter the song's title: ")
    artist_id = int(input("Enter the artist's id: "))
    genre_id = int(input("Enter the genre's id for the song: "))
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
            genre_id = int(input("Enter the genre's new id for the song: "))
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

```

## Installation
- Clone the repository.
-  Navigate to the project directory.
-  Run pipenv install to install the dependencies.
-  Run pipenv shell to activate the virtual environment.
-  Running the CLI
-  To start the CLI, run:

```
console :
python lib/cli.py
CLI Commands
The CLI offers the following options:

1  List all artists
2  Find artist by name
3  Find artist by id
4  Find artist by song id
5  Create artist
6  Update artist
7  Delete artist
8  List all genres
9  Find genre by name
10 Find genre by id
11  Create genre
12  Update genre
13  Delete genre
14  List all songs
15  Find song by title
16  Find song by id
17  Create song
18  Update song
19  Delete song
0  Exit the program
```
 ## Models

## Genre
The Genre class represents a music genre. It includes methods for creating, retrieving, updating, and deleting genre records in the database.

## Song
The Song class represents a song. It includes methods for creating, retrieving, updating, and deleting song records in the database.

## Artist
The Artist class represents an artist. It includes methods for creating, retrieving, updating, and deleting artist records in the database.

## Helpers
The helpers.py file contains functions that are called by the CLI to perform various operations on the database, such as listing all artists, finding an artist by name, creating a new song, etc.

## Debug
The debug.py file can be used to interactively test the models and functions without going through the CLI. This is helpful for development and debugging.

## Conclusion
This project provides a foundational structure for building a CLI application with an ORM in Python. It demonstrates how to organize code for user interaction, data persistence, and business logic in a clean and modular way.

Happy coding !!!!!