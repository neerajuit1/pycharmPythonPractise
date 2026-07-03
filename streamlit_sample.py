from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("firstApp").getOrCreate()

df = spark.createDataFrame([
("Alice", 1),
("Bob", 2),
("Charlie", 3),
], ["Name", "Value"])

df.show()