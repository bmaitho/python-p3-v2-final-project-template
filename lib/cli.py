# cli.py
from helpers import exit_program, list_genres, find_genre_by_name, find_genre_by_id
from helpers import create_genre, update_genre, delete_genre, create_song, update_song
from helpers import delete_song, list_songs, find_song_by_id, find_song_by_title

def main_menu():
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
    elif choice == '0':
        exit_program()
    else:
        print("Invalid choice, please try again.")
        main_menu()

if __name__ == "__main__":
    main_menu()
