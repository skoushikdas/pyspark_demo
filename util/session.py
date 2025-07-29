from pyspark.sql import SparkSession

class SparkSessionBuilder:
    @staticmethod
    def session(app_name, master, jars):
        return SparkSession.builder \
            .appName(app_name) \
            .master(master) \
            .config("spark.jars", jars) \
            .config("spark.mongodb.output.uri", "mongodb://localhost:27017/") \
            .getOrCreate()
