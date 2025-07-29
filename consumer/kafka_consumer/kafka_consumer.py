from pyspark.sql.functions import from_json, col, avg, max, min
from pyspark.sql.types import StructType, StringType, IntegerType

class KafkaConsumer:
    def __init__(self, spark, kafka_config):
        self.spark = spark
        self.kafka_config = kafka_config

        self.schema = StructType() \
            .add("user_id", StringType()) \
            .add("item_id", StringType()) \
            .add("interaction_count", IntegerType()) \
            .add("timestamp", StringType())

    def read_stream(self):
        df = self.spark.readStream \
            .format("kafka") \
            .option("kafka.bootstrap.servers", self.kafka_config["bootstrap.servers"]) \
            .option("subscribe", self.kafka_config["subscribe"]) \
            .option("startingOffsets", self.kafka_config["startingOffsets"]) \
            .load()

        value_df = df.selectExpr("CAST(value AS STRING)")
        json_df = value_df.select(from_json(col("value"), self.schema).alias("data")).select("data.*")

        return json_df

    def aggregate_stream(self, df):
        return df.groupBy("user_id", "item_id").agg(
            avg("interaction_count").alias("avg_interaction"),
            max("interaction_count").alias("max_interaction"),
            min("interaction_count").alias("min_interaction")
        )
