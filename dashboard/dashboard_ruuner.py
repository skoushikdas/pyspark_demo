# main_dashboard.py

import json
import logging

from dashboard.export_to_excel import ExcelExporter
from util.config_loader import load_config


if __name__ == "__main__":
    logging.info("Dashboard pipeline started ")
    config = load_config("config.json")
    exporter = ExcelExporter(config)
    exporter.run()
