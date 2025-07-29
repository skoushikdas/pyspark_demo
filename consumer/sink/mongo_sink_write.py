class MongoSink:
    def __init__(self, config):
        self.uri = config["uri"]
        self.db = config["database"]
        self.collection = config["collection"]

    def write(self, df):
        return df.writeStream \
            .format("mongodb") \
            .option("checkpointLocation", "/tmp/mongo-checkpoint") \
            .option("uri", f"{self.uri}/{self.db}.{self.collection}") \
            .outputMode("complete") \
            .start()
