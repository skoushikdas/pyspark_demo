
import os
import pandas as pd
from datetime import datetime
from pymongo import MongoClient
import logging as logger

class ExcelExporter:
    def __init__(self, config: dict):
        self.mongo_config = config["mongo"]
        self.output_path = self.mongo_config.get("output_path", "./data")
        os.makedirs(self.output_path, exist_ok=True)

    def _get_mongo_client(self):
        return MongoClient(self.mongo_config["uri"])

    def _get_collection(self, client):
        db = client[self.mongo_config["database"]]
        return db[self.mongo_config["collection"]]

    def fetch_data(self):
        client = self._get_mongo_client()
        collection = self._get_collection(client)
        documents = list(collection.find())
        client.close()
        return pd.DataFrame(documents)

    def save_to_excel(self, df: pd.DataFrame):
        today = datetime.now().strftime("%Y-%m-%d")
        output_file = os.path.join(self.output_path, f"dashboard_metrics_{today}.xlsx")
        df.to_excel(output_file, index=False)
        logger.info(f"Excel file saved to {output_file}")

    def run(self):
        df = self.fetch_data()
        if df.empty:
            logger.info("No data found in MongoDB.")
            return
        self.save_to_excel(df)
