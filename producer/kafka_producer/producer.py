"This class will publish messages to kafka topic"
import json
import logging
from datetime import time

from util.user_generator import User
from confluent_kafka import Producer


class Producer(User):
    def __init__(self, config):
        # super.__init__()
        self.speed = config["generator"].get("speed_multiplier")
        self.time_int = config["generator"].get("time_interval")
        kafka_conf = config["kafka"]
        self.producer = Producer({
            'bootstrap.servers': kafka_conf["bootstrap.servers"],
            'security.protocol': kafka_conf["security.protocol"],
            'sasl.mechanism': kafka_conf["sasl.mechanism"],
            'sasl.username': kafka_conf["sasl.username"],
            'sasl.password': kafka_conf["sasl.password"],
            'batch.num.messages': kafka_conf.get("batch.num.messages", "1000"),
            'compression.type': kafka_conf.get("compression.type", "snappy")
        })
        self.generate = User()

    def publish(self):
        message = self.generator.generate_message()
        self.producer.produce(
            topic=self.topic,
            key=message["user_id"],
            value=json.dumps(message)
        )
        logging.info(f"message generated {message}")
        self.producer.flush()
        return message

    def run(self):
        logging.info("kafka_producer pipeline started")
        while True:
            msg = self.publish()
            logging.info(f"message sent: {msg}")
            time.sleep(self.interval / self.speed_multiplier)