# Author class, with name and surname attributes, a list of book 
# titles and a function/method that returns the full name of the author
from typing import List
from unicodedata import name

class Author:

    def __init__(self, name: str, surname: str) -> None:
        self.name: str = name
        self.surname: str = surname
        self.books: List[str] = []

    @classmethod
    def from_dict(cls, author_dict: dict) -> None:
        return cls(
            name=author_dict["name"],
            surname=author_dict["surname"]
        )

    @property
    def full_name(self) -> str:
        return f"{self.name} {self.surname}"

    @full_name.setter
    def full_name(self, full_name: str) -> None:
        name, surname = full_name.split(" ")
        self.name = name
        self.surname = surname

    def add_book(self, book_title: str) -> None:
        if book_title not in self.books:
            self.books.append(book_title)

    def __eq__(self, other: "Author") -> bool:
        """equality check (==)"""
        return isinstance(other, Author) \
            and self.name == other.name \
            and self.surname == other.surname \
            and set(self.books) == set(other.books)

    def __ne__(self, other: "Author") -> bool:
        "inequality check (!=)"
        return not self == other

    def __repr__(self) -> str:
        """get a string representation of the author"""
        return f"Author(name={self.name}, surname={self.surname}, " \
            f"books= {', '.join(sorted(self.books))})"