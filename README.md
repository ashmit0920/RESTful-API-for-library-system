# RESTful-API-for-library-system

A simple RESTful API for a library system that allows users to manage books. The API will support the following functionalities:

1. Add a new book.
2. Get a list of all books.
3. Get details of a specific book.
4. Update details of a specific book.
5. Delete a book.

## Dependencies:

Flask
Flask-RESTful
Flask-SQLAlchemy
Marshmallow (for serialization and validation)

## Running the API
```
python init_db.py
```
```
python run.py
```
> You may need to use ``` flask --app init_db run ``` on a local environment, in case of dependency conflicts in the venv.

## Testing the API

1. Add a new book (POST /books):
```
curl -X POST -H "Content-Type: application/json" -d '{"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "published_date": "1925", "isbn": "9780743273565"}' http://127.0.0.1:5000/books
```

3. Get all books (GET /books):
```
curl http://127.0.0.1:5000/books
```

5. Get a specific book (GET /books/<book_id>):
```
curl http://127.0.0.1:5000/books/1
```

7. Update a book (PUT /books/<book_id>):
```
curl -X PUT -H "Content-Type: application/json" -d '{"author": "Francis Scott Fitzgerald"}' http://127.0.0.1:5000/books/1
```

9. Delete a book (DELETE /books/<book_id>):
```
curl -X DELETE http://127.0.0.1:5000/books/1
```
