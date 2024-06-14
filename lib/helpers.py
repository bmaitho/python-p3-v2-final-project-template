# lib/helpers.py
from models.song import Song
def exit_program():
    print("Goodbye!")
def add_song():
    
    name = input("Enter song name: ")
    artist=input("Enter artist name: ")
    genre = input("Enter genre: ")
    

    try:
        Song.create_song(name, artist, genre)
        print("Song added successfully!")
    except Exception as e:
        print("An error occurred:", e)


    
