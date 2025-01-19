# book_service.py

from datetime import datetime
from domain.book_entity import Book
from interfaces.repository import BookRepository

class BookService:
    def __init__(self, repository: BookRepository):
        self.repository = repository
    
    def create_book(self, title: str, author: str, **kwargs) -> int:
        """새로운 책을 생성합니다."""
        book = Book(
            id=None,
            title=title,
            subtitle=kwargs.get('subtitle'),
            author=author,
            link=kwargs.get('link'),
            status=kwargs.get('status', '시작전'),
            trigger=kwargs.get('trigger'),
            rating=kwargs.get('rating'),
            completed_date=kwargs.get('completed_date'),
            book_type=kwargs.get('book_type'),
            created_at=datetime.now(),
            updated_at=datetime.now(),
            cover_image=kwargs.get('cover_image'),
            memo=kwargs.get('memo')
        )
        return self.repository.create_book(book)

    def get_book_info(self, book_id: int) -> Book:
        """책 정보를 조회합니다."""
        return self.repository.get_book(book_id)
    
    def list_all_books(self) -> list[Book]:
        """모든 책을 조회합니다."""
        return self.repository.list_books()
    
    def edit_book(self, book_id: int, **kwargs) -> None:
        """책 정보를 수정합니다."""
        book = self.repository.get_book(book_id)
        if not book:
            return False

        # 필요한 경우에만 수정
        for key, value in kwargs.items():
            if hasattr(book, key):
                setattr(book, key, value)
        return self.repository.update_book(book)
    
    def remove_book(self, book_id: int) -> None:
        """책을 삭제합니다."""
        return self.repository.delete_book(book_id)
    