from utils import database

USER_CHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def menu():
    choice = input(USER_CHOICE)
    while choice != "q":
        if choice == "a":
            database.prompt_add_book()
        elif choice == "l":
            database.list_books()
        elif choice == "r":
            database.prompt_read_book()
        elif choice == "d":
            database.prompt_delete_book()
        else:
            print("Unknown command. Please try again.")

        menu()


menu()
