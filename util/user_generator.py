"A class that will generate the User object"
import uuid
import random
from datetime import datetime
import logging

from pyspark.sql.types import TimestampType

class User:
    def __init__(self):
        "Init the User class"
        self.user_id = str(uuid.uuid4())
        self.interaction_type = ["click", "view", "purchase"]
        logging.info(f"User initiated with interaction type {self.interaction_type}")

    def generate_message(self):
        return {
            "user_id" : self.user_id,
            "item_id" : str(uuid.uuid4()),
            "interaction_types" : random.choices(self.interaction_type),
            "timestamp" : datetime.isoformat()
        }
