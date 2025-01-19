# main.py

from flask import Flask
from interfaces.repository import BookRepository
from usecase.book_service import BookService
from web.routes import book_bp, service as book_service_global

def create_app():
    app = Flask(__name__)

    # Repository, Service 인스턴스 생성
    repo = BookRepository(db_path='books.db')
    svc = BookService(repository=repo)

    # Blueprint에 Service 인스턴스 주입
    book_service_global = svc # 모듈 전역 변수에 BookService 인스턴스를 할수
    book_bp.service = svc     # Blueprint 객체에 BookService 인스턴스를 할당

    # 블루프린트 등록
    app.register_blueprint(book_bp, url_prefix='')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
