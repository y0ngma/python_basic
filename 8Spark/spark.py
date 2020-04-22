#df1.createOrReplaceTempView("df1_table")
from pyspark.sql import SparkSession
import pandas as pd

#파이썬 설치 위치 지정
import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

#스파크 객체 생성 
spark = SparkSession.builder.master("local[*]") \
    .enableHiveSupport().appName("hive01") \
    .config("spark.sql.warehouse.dir","/user/hive/warehouse") \
    .config("spark.datasource.hive.metastore.uris","hdfs://192.168.0.15:9000") \
    .getOrCreate()

#테이터 프레임 생성
df1 = spark.createDataFrame([(1,'a',10),(2,'b',20),(3,'c',30)]).toDF("id","name","age")
df1.printSchema()
df1.show()
#df1.createOrReplaceTempView("table1")
#spark.sql("SELECT id, name FROM table1").show()


# 하둡 : DB 생성
spark.sql("create database db07") 

#데이터 프레임으로 테이블 생성
spark.sql("create table db07.t01 as select * from table1")

#테이블 내용 가져옴.
spark.sql("select * from db07.t01").show()

# 새로운 행 추가 ( 무한 가능 )
spark.sql("insert into db07.t01 values(4,'d',54)")

# 데이터프레임을 pandas로 변경
pd1 = df1.select("*").toPandas()
print(pd1)
