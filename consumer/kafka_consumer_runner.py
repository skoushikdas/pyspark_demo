from consumer.kafka_consumer.kafka_consumer import KafkaConsumer
from consumer.sink.mongo_sink_write import MongoSink
from util.config_loader import load_config
from util.session import SparkSessionBuilder


def main():
    config = load_config("config.json")

    spark = SparkSessionBuilder.create(
        app_name=config["spark"]["app_name"],
        master=config["spark"]["master"],
        jars=config["spark"]["jars"]
    )

    consumer = KafkaConsumer(spark, config["kafka"])
    sink = MongoSink(config["mongodb"])

    stream_df = consumer.read_stream()
    agg_df = consumer.aggregate_stream(stream_df)
    query = sink.write(agg_df)

    query.awaitTermination()

if __name__ == "__main__":
    main()
