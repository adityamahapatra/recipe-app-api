import time
from typing import Any, Optional

from django.core.management.base import BaseCommand
from django.db import connections
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Django command to pause execution till database is available."""
    def handle(self, *args: Any, **options: Any) -> Optional[str]:
        self.stdout.write("Waiting for the database...")
        db_conn = None
        while db_conn is None:
            try:
                db_conn = connections["default"]
            except OperationalError:
                self.stdout.write("Database unavailable, waiting 1 second...")
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS("Database available"))
