import pytest
from fastapi.testclient import TestClient

from app.main import app
from app.services.database import MigrationType, run_migration
from app.services.database import Session
from app.gutendex.schemas import HTTPResponse


@pytest.fixture
def web_client():
    client = TestClient(app)
    yield client


@pytest.fixture
def db_client():
    run_migration(MigrationType.downgrade, 'base')
    run_migration(MigrationType.upgrade, 'head')
    session = Session()
    yield session
    session.close()


@pytest.fixture
def post_book_review():
    return {
        "bookId": 84,
        "rating": 3,
        "review": "nota 5"
    }


@pytest.fixture
def book_not_found():
    return HTTPResponse(
        status=200,
        body={
            'count': 0,
            'next': None,
            'previous': None,
            'results': []
        }
    )


@pytest.fixture
def book_not_found_response():
    return {
        'message': 'Book not found.'
    }


@pytest.fixture
def sucess_find_book():
    return {
        "books": [
            {
                "id": 84,
                "title": "Frankenstein; Or, The Modern Prometheus",
                "authors": [
                    {
                        "name": "Shelley, Mary Wollstonecraft",
                        "birth_year": 1797,
                        "death_year": 1851
                    }
                ],
                "languages": [
                    "en"
                ],
                "download_count": 45117
            },
            {
                "id": 42324,
                "title": "Frankenstein; Or, The Modern Prometheus",
                "authors": [
                    {
                        "name": "Shelley, Mary Wollstonecraft",
                        "birth_year": 1797,
                        "death_year": 1851
                    }
                ],
                "languages": [
                    "en"
                ],
                "download_count": 1598
            },
            {
                "id": 41445,
                "title": "Frankenstein; Or, The Modern Prometheus",
                "authors": [
                    {
                        "name": "Shelley, Mary Wollstonecraft",
                        "birth_year": 1797,
                        "death_year": 1851
                    }
                ],
                "languages": [
                    "en"
                ],
                "download_count": 1095
            },
            {
                "id": 20038,
                "title": "Frankenstein; Or, The Modern Prometheus",
                "authors": [
                    {
                        "name": "Shelley, Mary Wollstonecraft",
                        "birth_year": 1797,
                        "death_year": 1851
                    }
                ],
                "languages": [
                    "en"
                ],
                "download_count": 310
            }
        ]
    }


@pytest.fixture
def find_book():
    return HTTPResponse(
        status=200,
        body={
            "count": 4,
            "next": "None",
            "previous": "None",
            "results": [
                {
                    "id": 84,
                    "title": "Frankenstein; Or, The Modern Prometheus",
                    "authors": [
                        {
                            "name": "Shelley, Mary Wollstonecraft",
                            "birth_year": 1797,
                            "death_year": 1851
                        }
                    ],
                    "translators": [

                    ],
                    "subjects": [
                        "Frankenstein's monster (Fictitious character) -- Fiction",
                        "Frankenstein, Victor (Fictitious character) -- Fiction",
                        "Gothic fiction",
                        "Horror tales",
                        "Monsters -- Fiction",
                        "Science fiction",
                        "Scientists -- Fiction"
                    ],
                    "bookshelves": [
                        "Gothic Fiction",
                        "Movie Books",
                        "Precursors of Science Fiction",
                        "Science Fiction by Women"
                    ],
                    "languages": [
                        "en"
                    ],
                    "copyright": False,
                    "media_type": "Text",
                    "formats": {
                        "text/plain; charset=utf-8": "https://www.gutenberg.org/files/84/84-0.txt",
                        "application/epub+zip": "https://www.gutenberg.org/ebooks/84.epub.images",
                        "application/rdf+xml": "https://www.gutenberg.org/ebooks/84.rdf",
                        "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/84.kindle.images",
                        "text/html; charset=utf-8": "https://www.gutenberg.org/files/84/84-h/84-h.htm",
                        "text/html": "https://www.gutenberg.org/ebooks/84.html.images",
                        "image/jpeg": "https://www.gutenberg.org/cache/epub/84/pg84.cover.medium.jpg"
                    },
                    "download_count": 45117
                },
                {
                    "id": 42324,
                    "title": "Frankenstein; Or, The Modern Prometheus",
                    "authors": [
                        {
                            "name": "Shelley, Mary Wollstonecraft",
                            "birth_year": 1797,
                            "death_year": 1851
                        }
                    ],
                    "translators": [

                    ],
                    "subjects": [
                        "Frankenstein's monster (Fictitious character) -- Fiction",
                        "Frankenstein, Victor (Fictitious character) -- Fiction",
                        "Gothic fiction",
                        "Horror tales",
                        "Monsters -- Fiction",
                        "Science fiction",
                        "Scientists -- Fiction"
                    ],
                    "bookshelves": [
                        "Precursors of Science Fiction",
                        "Science Fiction by Women"
                    ],
                    "languages": [
                        "en"
                    ],
                    "copyright": False,
                    "media_type": "Text",
                    "formats": {
                        "application/epub+zip": "https://www.gutenberg.org/ebooks/42324.epub.images",
                        "text/plain": "https://www.gutenberg.org/ebooks/42324.txt.utf-8",
                        "application/rdf+xml": "https://www.gutenberg.org/ebooks/42324.rdf",
                        "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/42324.kindle.images",
                        "text/plain; charset=iso-8859-1": "https://www.gutenberg.org/files/42324/42324-8.zip",
                        "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/42324/42324.txt",
                        "image/jpeg": "https://www.gutenberg.org/cache/epub/42324/pg42324.cover.medium.jpg",
                        "text/html": "https://www.gutenberg.org/ebooks/42324.html.images",
                        "text/html; charset=iso-8859-1": "https://www.gutenberg.org/files/42324/42324-h/42324-h.htm",
                        "application/zip": "https://www.gutenberg.org/files/42324/42324-h.zip"
                    },
                    "download_count": 1598
                },
                {
                    "id": 41445,
                    "title": "Frankenstein; Or, The Modern Prometheus",
                    "authors": [
                        {
                            "name": "Shelley, Mary Wollstonecraft",
                            "birth_year": 1797,
                            "death_year": 1851
                        }
                    ],
                    "translators": [

                    ],
                    "subjects": [
                        "Frankenstein's monster (Fictitious character) -- Fiction",
                        "Frankenstein, Victor (Fictitious character) -- Fiction",
                        "Gothic fiction",
                        "Horror tales",
                        "Monsters -- Fiction",
                        "Science fiction",
                        "Scientists -- Fiction"
                    ],
                    "bookshelves": [
                        "Precursors of Science Fiction",
                        "Science Fiction by Women"
                    ],
                    "languages": [
                        "en"
                    ],
                    "copyright": False,
                    "media_type": "Text",
                    "formats": {
                        "application/epub+zip": "https://www.gutenberg.org/ebooks/41445.epub.images",
                        "application/rdf+xml": "https://www.gutenberg.org/ebooks/41445.rdf",
                        "application/x-mobipocket-ebook": "https://www.gutenberg.org/ebooks/41445.kindle.images",
                        "text/plain": "https://www.gutenberg.org/ebooks/41445.txt.utf-8",
                        "image/jpeg": "https://www.gutenberg.org/cache/epub/41445/pg41445.cover.small.jpg",
                        "text/html": "https://www.gutenberg.org/files/41445/41445-h/41445-h.htm",
                        "text/plain; charset=us-ascii": "https://www.gutenberg.org/files/41445/41445-0.txt",
                        "application/zip": "https://www.gutenberg.org/files/41445/41445-0.zip"
                    },
                    "download_count": 1095
                },
                {
                    "id": 20038,
                    "title": "Frankenstein; Or, The Modern Prometheus",
                    "authors": [
                        {
                            "name": "Shelley, Mary Wollstonecraft",
                            "birth_year": 1797,
                            "death_year": 1851
                        }
                    ],
                    "translators": [

                    ],
                    "subjects": [
                        "Frankenstein's monster (Fictitious character) -- Fiction",
                        "Frankenstein, Victor (Fictitious character) -- Fiction",
                        "Gothic fiction",
                        "Horror tales",
                        "Monsters -- Fiction",
                        "Science fiction",
                        "Scientists -- Fiction"
                    ],
                    "bookshelves": [
                        "Movie Books",
                        "Precursors of Science Fiction",
                        "Science Fiction by Women"
                    ],
                    "languages": [
                        "en"
                    ],
                    "copyright": False,
                    "media_type": "Sound",
                    "formats": {
                        "audio/mpeg": "http://www.gutenberg.org/files/20038/mp3/20038-17.mp3",
                        "audio/mp4": "http://www.gutenberg.org/files/20038/m4b/20038-01.m4a",
                        "application/zip": "http://www.gutenberg.org/files/20038/20038-spx.zip",
                        "audio/ogg": "http://www.gutenberg.org/files/20038/ogg/20038-12.ogg",
                        "text/plain": "http://www.gutenberg.org/files/20038/20038-readme.txt",
                        "application/rdf+xml": "http://www.gutenberg.org/ebooks/20038.rdf",
                        "text/html": "http://www.gutenberg.org/files/20038/20038-index.html"
                    },
                    "download_count": 310
                }
            ]
        }
    )


@pytest.fixture
def success_top_rating():
    return {'books': [{'id': 84, 'title': 'Frankenstein; Or, The Modern Prometheus',
                       'authors': [{'name': 'Shelley, Mary Wollstonecraft', 'birth_year': 1797, 'death_year': 1851}],
                       'languages': ['en'], 'download_count': 45117, 'rating': 4.0, 'reviews': ['nota 5', 'nota 5']},
                      {'id': 83, 'title': 'From the Earth to the Moon; and, Round the Moon',
                       'authors': [{'name': 'Verne, Jules', 'birth_year': 1828, 'death_year': 1905}],
                       'languages': ['en'], 'download_count': 541, 'rating': 2.5, 'reviews': ['nota 5', 'nota 5']},
                      {'id': 82, 'title': 'Ivanhoe: A Romance',
                       'authors': [{'name': 'Scott, Walter', 'birth_year': 1771, 'death_year': 1832}],
                       'languages': ['en'], 'download_count': 1602, 'rating': 1.5, 'reviews': ['nota 5', 'nota 5']}]}
