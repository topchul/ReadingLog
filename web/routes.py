# routes.py

from flask import Blueprint, request, render_template, redirect, url_for
from usecase.book_service import BookService

book_bp = Blueprint('book_bp', __name__, template_folder='templates')

# BookService 인스턴스 주입
service: BookService = None

@book_bp.route('/books', methods=['GET'])
def list_books():
    books = service.list_all_books()
    return render_template('books.html', books=books)

@book_bp.route('/books/new', methods=['GET', 'POST'])
def create_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        service.create_book(
            title=title,
            author=author,
            subtitle=request.form.get('subtitle'),
            link=request.form.get('link'),
            status=request.form.get('status', '시작전'),
            trigger=request.form.get('trigger'),
            rating=int(request.form.get('rating')) if request.form.get('rating') else None,
            # completed_date 처리 생략 (필요시 request.form.get('completed_date'))
            book_type=request.form.get('book_type'),
            cover_image=None,
            memo=request.form.get('memo'),
        )
        return redirect(url_for('book_bp.list_books'))
    return render_template('new_book.html')

@book_bp.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = service.get_book_info(book_id)
    return render_template('book.html', book=book)

@book_bp.route('/books/<int:book_id>/edit', methods=['GET', 'POST'])
def edit_book(book_id):
    book = service.get_book_info(book_id)
    if request.method == 'POST':
        service.edit_book(
            book_id,
            title=request.form.get('title'),
            author=request.form.get('author'),
            subtitle=request.form.get('subtitle'),
            link=request.form.get('link'),
            status=request.form.get('status'),
            trigger=request.form.get('trigger'),
            rating=int(request.form.get('rating')) if request.form.get('rating') else None,
            # completed_date 처리 생략 (필요시 request.form.get('completed_date'))
            book_type=request.form.get('book_type'),
            cover_image=request.form.get('cover_image'),
            memo=request.form.get('memo'),
        )
        return redirect(url_for('book_bp.get_book', book_id=book_id))
    return render_template('book_form.html', book=book)

@book_bp.route('/books/<int:book_id>/delete', methods=['POST'])
def delete_book(book_id):
    service.remove_book(book_id)
    return redirect(url_for('book_bp.list_books'))