## Introduction

This project it's an integration with [gutendex](https://gutendex.com/]) to work with datas.

## Technologies

I used python 3.9 with the following libraries:

 - FastAPI
 - sqlalchemy
 - uvicorn
 - alembic
 - redis
 - pydantic
 - requests

## Structure

```shell
.
├── alembic
│   ├── env.py
│   ├── README
│   ├── script.py.mako
│   └── versions                                    # Migration files
├── alembic.ini
├── app                                                   # Main folder with the API
│   ├── gutendex                                    # Gutendex functions
│   │   ├── finder.py
│   │   ├── review.py
│   │   ├── schemas.py
│   │   └── utils.py
│   ├── main.py
│   ├── models                                       # Database Models
│   │   ├── __init__.py
│   │   └── review.py
│   ├── router                                       # Routes
│   │   ├── book.py
│   ├── services
│   │   ├── cache.py
│   │   ├── database.py
│   └── settings.py
├── conftest.py
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── README.md
├── requirements.txt
└── tests                                                   # Tests
    └── app
        └── router
            └── test_book.py
```

## Starting

To start our application we need to use `docker-compose`
```shell
# Start project
$ docker-compose up --build
```

After docker has initialized we can access `http://localhost:8000/docs` to see our API.

## Executing Tests

To execute the tests we need to enter our docker container and after run covarege.
```shell
# Access docker container
$ docker exec -it book-catalog bash
# Run tests
$ coverage run -m pytest
================================================ test session starts =================================================
platform linux -- Python 3.9.12, pytest-6.2.2, py-1.11.0, pluggy-0.13.1
rootdir: /code
collected 7 items                                                                                                    

tests/app/router/test_book.py .......                                                                          [100%]

================================================= 7 passed in 4.44s ==================================================
# To get coverage cover.
$ coverage report
Name                                                   Stmts   Miss  Cover
--------------------------------------------------------------------------
alembic/env.py                                            23      5    78%
alembic/versions/ef41da5467ab_create_review_table.py      10      0   100%
app/gutendex/finder.py                                    48      8    83%
app/gutendex/review.py                                    20      2    90%
app/gutendex/schemas.py                                   40      0   100%
app/gutendex/utils.py                                      6      0   100%
app/main.py                                               14      5    64%
app/models/__init__.py                                    27     16    41%
app/models/review.py                                      18      0   100%
app/router/book.py                                        19      0   100%
app/services/cache.py                                     17      5    71%
app/services/database.py                                  23      2    91%
app/settings.py                                            4      0   100%
conftest.py                                               35      0   100%
tests/app/router/test_book.py                             71      0   100%
--------------------------------------------------------------------------
TOTAL                                                    375     43    89%
```
