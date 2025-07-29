import logging

from producer.kafka_producer.producer import Producer
from util import load_config


if __name__ == "__main__":
    logging.info("Producer pipeline started")
    kafka_config = load_config("/Users/koushiksayani/PycharmProjects/pythonProject/pyspark_demo/config/config.json")
    logging.info("config loaded ")
    producer = Producer(config=kafka_config)
    producer.run()
