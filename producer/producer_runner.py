import logging
import time
from math import trunc

from producer.producer.producer import Producer
from util.config_loader import load_config


if __name__ == "__main__":
    kafka_config = load_config("/Users/koushiksayani/PycharmProjects/pythonProject/pyspark_demo/config/config.json")
    logging.info("config loaded ")
    producer = Producer(config=kafka_config)
    producer.run()
