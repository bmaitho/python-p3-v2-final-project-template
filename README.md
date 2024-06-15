
#### NGOMA

# Date 2024 - 06 - 14

## BY BRIAN MAITHO

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
## Installation
To run NGOMA  on your local machine, follow these steps:

1. Clone the repository to your local machine:

git clone https://github.com/bmaitho/python-p3-v2-final-project-template
2. Navigate to the project directory in your terminal.

3. Install the dependencies:

4.  NGOMA uses Python Standard Libraries. No additional dependecies required.
5. Set up the database:

-  Ensure you have a compatible database (e.g., SQLite, PostgreSQL).
-  Update the database configuration in the application code (models.py or similar) as per your database setup.
6. Running the application:

- Activate the virtual environment:
```
pipenv shell
```
- Seed the database with some initial data:
```
python lib/seed.py
```
- Run the CLI application:
```
python lib/cli.py
```

 
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
## Helpers
The helpers.py file contains functions that are called by the CLI to perform various operations on the database, such as listing all artists, finding an artist by name, creating a new song, etc.



## Installation
- Clone the repository.
-  Navigate to the project directory.
-  Run pipenv install to install the dependencies.
-  Run pipenv shell to activate the virtual environment.
-  Running the CLI
-  To start the CLI, run: python lib/cli.py


## The CLI offers the following options:
```
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
 ## Models folder contains:

## Genre
The Genre class represents a music genre. It includes methods for creating, retrieving, updating, and deleting genre records in the database.

## Song
The Song class represents a song. It includes methods for creating, retrieving, updating, and deleting song records in the database.

## Artist
The Artist class represents an artist. It includes methods for creating, retrieving, updating, and deleting artist records in the database.

## Debug
The debug.py file can be used to interactively test the models and functions without going through the CLI. This is helpful for development and debugging.
## Helpers
The helpers.py file contains functions that are called by the CLI to perform various operations on the database, such as listing all artists, finding an artist by name, creating a new song, etc.

## Conclusion
This project showcases a CLI application with an ORM in Python.Demonstarting how to organize code for user interaction, data persistence, and business logic in a clean and modular way.


## Dependency
* Python Standard Libraries: Used for CLI interface, datetime handling, and basic input/output operations.
## Technologies Used
* Python: The app is built using the Python library.
## Contributing
Contributions to NGOMA are welcome! If you'd like to contribute:

 * Fork the repository.
 * Create your feature branch (git checkout -b feature/YourFeature)
 * Commit your changes (git commit -am 'Add some feature').
 * Push to the branch (git push origin feature/YourFeature).
 * Create a new Pull Request.
Please ensure your code follows the project's coding style and includes appropriate documentation.

## Contact
For any support or inquiries, please contact Brian Maitho at bmaitho@gmail.com
## License
This project is licensed under the MIT License.

## Feedback
If you have any feedback or suggestions for improvement, please feel free to contact me. I'd love to hear from you!

Happy coding !!!!!