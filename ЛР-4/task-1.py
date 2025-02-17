from abc import ABC, abstractmethod
from typing import List, Tuple, Optional


class Publication(ABC):
    """
    Абстрактный базовый класс для всех видов публикаций.
    Определяет общие атрибуты и методы для всех публикаций,
    таких как статьи, книги, посты в социальных сетях и т.д.
    """

    def __init__(self, title: str, author: str, publication_date: str):
        """
        Конструктор для создания объекта публикации.
        Args:
            title (str): Название публикации.
            author (str): Автор публикации.
            publication_date (str): Дата публикации.
        """
        self._title = title  # Защищённый атрибут, доступен в подклассах
        self._author = author  # Защищённый атрибут, доступен в подклассах
        self._publication_date = publication_date  # Защищённый атрибут, доступен в подклассах

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def publication_date(self) -> str:
        return self._publication_date

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта публикации.

        Returns:
            str: Строковое представление объекта публикации.
        """
        return f"Название: {self._title}, Автор: {self._author}, Дата публикации: {self._publication_date}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта для отладки.

        Returns:
            str: Строковое представление объекта для отладки.
        """
        return f"{self.__class__.__name__}(title={self._title!r}, author={self._author!r}, publication_date={self._publication_date!r})"

    @abstractmethod
    def display(self) -> None:
        """
        Абстрактный метод для отображения публикации.
        Должен быть реализован в подклассах.
        """
        pass


class BlogPost(Publication):
    """
    Класс для представления постов в блоге.
    Наследуется от Publication и расширяет её, добавляя специфические атрибуты и методы для блогов.
    """

    def __init__(self, title: str, author: str, publication_date: str, content: str, tags: Optional[List[str]] = None):
        """
        Конструктор для создания объекта блог-поста.

        Args:
            title (str): Название поста.
            author (str): Автор поста.
            publication_date (str): Дата публикации поста.
            content (str): Содержание поста.
             tags (list, optional): Список тегов, связанных с публикацией.
        """
        super().__init__(title, author, publication_date)
        self._content = content
        self._tags = tags if tags is not None else []

    def __str__(self) -> str:
        """
        Переопределённый метод, добавляет к строке родителя информацию о контенте и тегах.

        Returns:
            str: Строковое представление объекта блог-поста.
        """
        return f"{super().__str__()}, Содержание: {self._content[:50]}..., Теги: {', '.join(self._tags)}"

    def __repr__(self) -> str:
        """
        Переопределённый метод, добавляет к представлению объекта родителя информацию о контенте и тегах.

        Returns:
            str: Строковое представление объекта для отладки.
        """
        return f"{self.__class__.__name__}(title={self.title!r}, author={self.author!r}, publication_date={self.publication_date!r}, content={self._content!r}, tags={self._tags!r})"

    def display(self) -> None:
        """
        Метод отображения полного поста в блоге.
        Выводит на печать заголовок, автора, дату публикации и содержание поста.
        """
        print(f"Заголовок: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Дата публикации: {self.publication_date}")
        print(f"Содержание:\n{self._content}")
        print(f"Теги: {', '.join(self._tags)}")

    def add_tag(self, tag: str) -> None:
        """
        Метод для добавления тега к посту.
        """
        self._tags.append(tag)

    def get_short_content(self, length: int = 50) -> str:
        """
        Метод для получения короткого содержания поста.
        Args:
            length (int): Максимальная длина возвращаемого текста.

        Returns:
           str: Короткое содержание поста.
        """
        return self._content[:length]

    def _get_publication_info(self) -> Tuple[str, str]:
        """
       Защищённый метод для получения информации о публикации.
       Используется только внутри класса, инкапсулируя способ получения необходимой информации.
       Args:
         None
       Returns:
           Tuple[str, str]: Кортеж, содержащий имя автора и название статьи
       """
        return self.author, self.title


class ResearchPaper(Publication):
    """
    Класс для представления научных статей.
    Наследуется от Publication и расширяет её, добавляя специфические атрибуты и методы для научных статей.
    """

    def __init__(self, title: str, author: str, publication_date: str, journal: str, doi: str,
                 authors: Optional[List[str]] = None):
        """
        Конструктор для создания объекта научной статьи.

        Args:
            title (str): Название статьи.
            author (str): Автор статьи.
            publication_date (str): Дата публикации статьи.
            journal (str): Название научного журнала.
            doi (str): Цифровой идентификатор объекта (DOI).
            authors (list, optional): Список соавторов статьи.
        """
        super().__init__(title, author, publication_date)
        self._journal = journal
        self._doi = doi
        self._authors = authors if authors is not None else [author]

    def __str__(self) -> str:
        """
        Переопределенный метод, добавляет к строке родителя информацию о журнале, doi и соавторах.

         Returns:
            str: Строковое представление объекта научной статьи.
        """
        return f"{super().__str__()}, Журнал: {self._journal}, DOI: {self._doi}, Соавторы: {', '.join(self._authors)}"

    def __repr__(self) -> str:
        """
        Переопределенный метод, добавляет к представлению объекта родителя информацию о журнале, doi и соавторах.
        Returns:
            str: Строковое представление объекта для отладки.
        """
        return f"{self.__class__.__name__}(title={self.title!r}, author={self.author!r}, publication_date={self.publication_date!r}, journal={self._journal!r}, doi={self._doi!r}, authors={self._authors!r})"

    def display(self) -> None:
        """
         Метод отображения научной статьи.
        Выводит на печать название, автора, дату публикации, журнал, doi и соавторов.
        """
        print(f"Название: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Соавторы: {', '.join(self._authors)}")
        print(f"Дата публикации: {self.publication_date}")
        print(f"Журнал: {self._journal}")
        print(f"DOI: {self._doi}")

    def add_author(self, author: str) -> None:
        """
        Метод для добавления соавтора.
        """
        self._authors.append(author)

    def get_authors(self) -> List[str]:
        """
        Метод для получения списка авторов.

        Returns:
            List[str]: Список авторов статьи.
        """
        return self._authors

    def get_publication_journal(self) -> str:
        """
        Метод для получения названия журнала.

        Returns:
            str: Название научного журнала.
        """
        return self._journal


if __name__ == "__main__":
    blog_post = BlogPost(
        title="Мой первый пост",
        author="Иван Иванов",
        publication_date="2024-01-28",
        content="Это текст моего первого поста в блоге. Он очень короткий.",
        tags=["блог", "первый пост"],
    )
    print(blog_post)
    print(repr(blog_post))
    blog_post.display()
    print(f"Короткое содержание: {blog_post.get_short_content()}")
    blog_post.add_tag("новый_тег")
    print(blog_post)
    author, title = blog_post._get_publication_info()
    print(f"Информация: Автор - {author}, Название - {title}")

    research_paper = ResearchPaper(
        title="Исследование темной материи",
        author="Мария Склодовская-Кюри",
        publication_date="1903-07-01",
        journal="Nature",
        doi="10.1038/nature12345",
        authors=["Мария Склодовская-Кюри", "Пьер Кюри"]
    )
    print(research_paper)
    print(repr(research_paper))
    research_paper.display()
    research_paper.add_author("Анри Беккерель")
    print(f"Авторы: {research_paper.get_authors()}")
    print(f"Журнал: {research_paper.get_publication_journal()}")