import time
import logging
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError

from backend.shared.infrastructure.config import settings

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def wait_for_db(max_retries: int = 30, retry_interval: int = 2) -> bool:
    """Wait for the database to be available."""
    retries = 0

    while retries < max_retries:
        try:
            engine = create_engine(settings.DATABASE_URL)
            with engine.connect():
                logger.info("Database is available!")
                return True
        except OperationalError:
            retries += 1
            logger.info(f"Database unavailable, waiting... ({retries}/{max_retries})")
            time.sleep(retry_interval)

    logger.error(f"Could not connect to database after {max_retries} retries")
    return False


if __name__ == "__main__":
    wait_for_db()
