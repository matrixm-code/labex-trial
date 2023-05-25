import sqlite3


def add_book(cursor: sqlite3.Cursor, title: str, author: str, price: float) -> None:
    """Add a new book to the 'books' table.

    Args:
        cursor (sqlite3.Cursor): The cursor to execute the SQL command.
        title (str): The title of the book.
        author (str): The author of the book.
        price (float): The price of the book.

    Returns:
        None
    """
    query = f"INSERT INTO books (title, author, price) VALUES (?, ?, ?)"
    cursor.execute(query, (title, author, price))
