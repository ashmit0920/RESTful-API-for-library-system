from flask import request, jsonify
from flask_restful import Resource
from app import db
from app.models import Book
from app.schemas import BookSchema
from marshmallow import ValidationError

book_schema = BookSchema()
books_schema = BookSchema(many=True)

class BookListResource(Resource):
    def get(self):
        books = Book.query.all()
        return books_schema.dump(books), 200

    def post(self):
        try:
            book_data = request.get_json()
            book = book_schema.load(book_data)
        except ValidationError as err:
            return jsonify(err.messages), 400

        new_book = Book(
            title=book['title'],
            author=book['author'],
            published_date=book['published_date'],
            isbn=book['isbn']
        )

        db.session.add(new_book)
        db.session.commit()
        return book_schema.dump(new_book), 201

class BookResource(Resource):
    def get(self, book_id):
        book = Book.query.get_or_404(book_id)
        return book_schema.dump(book), 200

    def put(self, book_id):
        book = Book.query.get_or_404(book_id)
        try:
            book_data = request.get_json()
            book_data = book_schema.load(book_data, partial=True)
        except ValidationError as err:
            return jsonify(err.messages), 400

        book.title = book_data.get('title', book.title)
        book.author = book_data.get('author', book.author)
        book.published_date = book_data.get('published_date', book.published_date)
        book.isbn = book_data.get('isbn', book.isbn)

        db.session.commit()
        return book_schema.dump(book), 200

    def delete(self, book_id):
        book = Book.query.get_or_404(book_id)
        db.session.delete(book)
        db.session.commit()
        return '', 204
