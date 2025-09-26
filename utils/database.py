import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database.db")

connection = sqlite3.connect(db_path)
cursor = connection.cursor()

create_table = """
        CREATE TABLE IF NOT EXISTS BOOKS (
        ID INTEGER PRIMARY KEY,
        NAME VARCHAR(25) NOT NULL,
        AUTHOR VARCHAR(25) NOT NULL,
        ISREAD VARCHAR(1) NOT NULL
        );
        """

cursor.execute(create_table)


def prompt_add_book():

    newbook_name = input("Book's name ")
    newbook_author = input("Book's Author ")
    newbook_isread = input("Read? Y/N ").upper()

    if newbook_isread != "Y" and newbook_isread != "N":
        print("Only Y or N are accepted to define if a book is read or not.")
    else:
        cursor.execute(f"""INSERT INTO BOOKS (NAME, AUTHOR, ISREAD) 
        VALUES (?, ?, ?)""", (newbook_name,newbook_author, newbook_isread))

        connection.commit()
        connection.close()


def list_books():
    cursor.execute("SELECT * FROM BOOKS")
    for row in cursor.fetchall():
        print(row)
    connection.close()


def prompt_read_book():
    book_to_change = input("What book do you want to mark as read? ")
    cursor.execute(f"""
    UPDATE BOOKS 
    SET ISREAD = ? 
    WHERE NAME = ?""", ("Y", book_to_change))
    connection.commit()
    connection.close()


def prompt_delete_book():
    book_to_delete = input("Which book do you want to delete? ")
    cursor.execute(f"""
    DELETE FROM BOOKS
    WHERE NAME = ?""", (book_to_delete,))
    connection.commit()
    connection.close()

