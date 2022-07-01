import time
import logging
from fastapi import FastAPI

from app.router.book import router as book_router
from app.services.database import run_migration, MigrationType

app = FastAPI(tittle="book-catalog")
app.include_router(book_router, prefix="/book", tags=["book"])


@app.on_event('startup')
async def setup_application():
    """
    Script to execute migrations when starting the API.
    :return:
    """
    try:
        time.sleep(10) # To be sure that the datase has started.
        run_migration(MigrationType.upgrade, 'head')
    except Exception as err:
        logging.error(err)
