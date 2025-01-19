# repository.py

import sqlite3
from datetime import datetime, date
from domain.book_entity import Book

class BookRepository:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self._init_db()
    
    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS books (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    subtitle TEXT,
                    author TEXT,
                    link TEXT,
                    status TEXT,
                    trigger TEXT,
                    rating INTEGER,
                    completed_date TEXT,
                    book_type TEXT,
                    created_at TEXT NOT NULL,
                    updated_at TEXT NOT NULL,
                    cover_image TEXT,
                    memo TEXT
                )
            ''')
            conn.commit()
    
    def create_book(self, book: Book) -> int:
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO books (
                    title, subtitle, author, link, status,
                    trigger, rating, completed_date, book_type,
                    created_at, updated_at, cover_image, memo
                ) VALUES (
                    ?, ?, ?, ?, ?,
                    ?, ?, ?, ?, 
                    ?, ?, ?, ?
                )
            """, (
                book.title, book.subtitle, book.author, book.link, book.status,
                book.trigger, book.rating, book.completed_date, book.book_type,
                book.created_at, book.updated_at, book.cover_image, book.memo
            ))
            conn.commit()
            return cursor.lastrowid
    
    def get_book(self, book_id: int) -> Book:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    title, subtitle, author, link, status,
                    trigger, rating, completed_date, book_type,
                    created_at, updated_at, cover_image, memo
                FROM
                    books
                WHERE
                    id = ?
            """, (book_id,))
            row = cur.fetchone()
            if not row:
                return None
            return self._row_to_book(row)
    
    def _row_to_book(self, row) -> Book:
        return Book(
            id=row['id'],
            title=row['title'],
            subtitle=row['subtitle'],
            author=row['author'],
            link=row['link'],
            status=row['status'],
            trigger=row['trigger'],
            rating=row['rating'],
            completed_date=date.fromisoformat(row['completed_date']) if row['completed_date'] else None,
            book_type=row['book_type'],
            created_at=datetime.fromisoformat(row['created_at']),
            updated_at=datetime.fromisoformat(row['updated_at']),
            cover_image=row['cover_image'],
            memo=row['memo']
        )
    
    def list_books(self) -> list[Book]:
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = sqlite3.Row
            cur = conn.cursor()
            cur.execute("""
                SELECT 
                    id, title, subtitle, author, link, status,
                    trigger, rating, completed_date, book_type,
                    created_at, updated_at, cover_image, memo
                FROM
                    books
            """)
            rows = cur.fetchall()
            return [self._row_to_book(r) for r in rows]
    
    def update_book(self, book: Book):
        book.updated_at = datetime.now()
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                UPDATE books
                SET
                    title = ?, subtitle = ?, author = ?, link = ?, status = ?,
                    trigger = ?, rating = ?, completed_date = ?, book_type = ?,
                    updated_at = ?, cover_image = ?, memo = ?
                WHERE
                    id = ?
            """, (
                book.title, book.subtitle, book.author, book.link, book.status,
                book.trigger, book.rating, book.completed_date, book.book_type,
                book.updated_at, book.cover_image, book.memo,
                book.id
            ))
            conn.commit()
            return cur.rowcount > 0
    
    def delete_book(self, book_id: int) -> bool:
        with sqlite3.connect(self.db_path) as conn:
            cur = conn.cursor()
            cur.execute("""
                DELETE FROM books
                WHERE
                    id = ?
            """, (book_id,))
            conn.commit()
            return cur.rowcount > 0
