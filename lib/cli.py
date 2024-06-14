# lib/cli.py

from helpers import (
    exit_program,
    add_song
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_song()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new song")


if __name__ == "__main__":
    main()
