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
