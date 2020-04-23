from pyspark.sql import SparkSession
import pandas as pd
import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

spark = SparkSession.builder.master("local[*]") \
    .appName("exam01") \
    .config('spark.driver.extraClassPath','/home/user1/spark-sql-kafka-0-10_2.11-2.4.5.jar' ) \
    .config('spark.driver.extraClassPath','/home/user1/kafka-clients-0.11.0.0.jar' ) \
    .config('spark.jars.packages','org.apache.spark:spark-sql-kafka-0-10_2.11:2.4.5' ) \
    .getOrCreate()

df = spark.readStream.format("kafka") \
    .option("kafka.bootstrap.servers","192.168.0.15:9092") \
    .option("subscribe", "testTopic2") \
    .option("startingOffsets", "latest") \
    .load()

#df의 값을 변경해서 df1에 보관
df1 = df.selectExpr("CAST (key AS STRING)", "CAST(value AS STRING)")

# 분석



#df1의 실시간 값을 console에 출력함 (출력을 위한 코드)
df1.writeStream.outputMode("append") \
    .format("console") \
    .option("truncate", "false") \
    .start() \
    .awaitTermination()