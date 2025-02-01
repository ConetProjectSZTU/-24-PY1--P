class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    def __str__(self):
        return f"Книга {self._name}. Автор {self._author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()} Количество страниц: {self.pages}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value):
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть больше 0")
        self._pages = value


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()} Продолжительность: {self.duration} мин."

    def __repr__(self):
         return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть больше 0")
        self._duration = value

if __name__ == '__main__':
    book = Book("Мастер и Маргарита", "Булгаков")
    print(book)
    print(repr(book))
    # book.name = "Собачье Сердце" # AttributeError: can't set attribute
    paper_book = PaperBook("Мертвые Души", "Гоголь", 350)
    print(paper_book)
    print(repr(paper_book))
    #paper_book.pages = "строка" # TypeError: Количество страниц должно быть целым числом
    #paper_book.pages = -10 # ValueError: Количество страниц должно быть больше 0
    paper_book.pages = 500
    print(paper_book.pages)
    audio_book = AudioBook("Преступление и наказание", "Достоевский", 12.5)
    print(audio_book)
    print(repr(audio_book))
    #audio_book.duration = "строка" # TypeError: Продолжительность должна быть числом
    #audio_book.duration = 0 # ValueError: Продолжительность должна быть больше 0
    audio_book.duration = 15.7
    print(audio_book.duration)
