"""
# Spark

## 스파크 @윈도우 로컬
- Path, SPARK_HOME, HADOOP_HOME, JAVA_HOME 설정 완료
    - Master/Slave 환경변수 설정 하기 전에 실행 가능한 테스트
"""

import findspark
findspark.init()
findspark.find()

import pyspark
findspark.find()

"""#### spark 세션을 생성해주기 위해서 다음과 같이 컴파일을 진행해준다."""

from pyspark import SparkContext, SparkConf
from pyspark.sql import SparkSession

# local 에 마스터로 잡고
conf = pyspark.SparkConf().setAppName('appName').setMaster('local[2]') 
sc = pyspark.SparkContext(conf=conf)
spark = SparkSession(sc)

"""#### 만약 세션이 끝났다면 다음과 같은 코드를 실행한다.
- sc.stop()
"""

# 리스트에서 RDD 생성
data = [1, 2, 3, 4, 5]
data

"""### Resilient Distributed Dataset
- RDD

- 클라이언트 모드 (밖) -> 실습은 이쪽
- 클러스터   모드(안)
"""

# 데이터를 4개 단위로 쪼개서 처리
rdd = sc.parallelize(data, 4)
rdd

sc.defaultParallelism

rdd1=rdd.map(lambda x: x*2)
rdd1

# action을 하는순간 실행된다.
rdd1.collect()

rdd2 = rdd.filter(lambda x: x% 2 ==0) # 조건에 맞는 애들만 가져오는것
rdd2

rdd2.collect()

rdd3=sc.parallelize([1,4,2,2,3])
# pandas -> unique와 같은 함수 distinct()중복값 제거
rdd3.distinct().collect()
# 순서 섞이는듯

"""### map() 과 flatMap()"""

rdd4 = sc.parallelize([1,2,3])
# 키, 값을 정해주는 느낌??
# [원본, 계산값,......]
rdd4.map(lambda x: [x, x+5]).collect()

# [원본, 계산값]을 한번에 다 가져오게 하려고 따로 or 한번에 가능
rdd4.flatMap(lambda x:[x, x+5]).collect()

"""### actions
```py
reduce(func) # 최종 결과값, 함수를 이용하여 최종 결과를 도출한다. ex) lambda
take(n) # pandas의 head()
collect() # 결과값 바로 받아오는거
takeOrdered(n,key=func) # 몇개 가져오는데 , 함수를 이용하여 정렬 할수 있음.
```
"""

rdd= sc.parallelize([1,2,3])
rdd.reduce(lambda a, b : a*b)

rdd.take(2)   # 앞에서 2개 가져오기

rdd.collect() # 다 가져 오는것

rdd5=sc.parallelize([5,3,1,2])
rdd5.takeOrdered(3, lambda s: -1*s)

"""## 스파크 데이터 타입

- ByteType      : int, long 
    - 128~127 사이의 값
- ShortType     : int, long 
    - 32768 ~ 32767 사이의 값
- IntegerType   : int, long 2 바이트 크기
- LongType      : long 8 bytes
- FloatType     : float 4 bytes
- DoubleType    : float
- DecimalType   : decimal.Decimal
- StringType    : string
- BinaryType    : bytearray
- BooleanType   : bool
- TimestampType : datetime.datetime
- DateType      : datetime.date
- ArrayType     : list, tuple, array

### DataFrame
- Row 타입의 레코드 (테이블의 로우 같은) 와 각 레코드에 수행할 연산표현식을 나타내는 여러컬럼( 스프레드시트의 컬럼 같은) 으로 구성됩니다.
- 스키마는 각 컬럼명과 데이터 타입을 정의
"""

import os
cwd = os.getcwd()
cwd

spark.read.format("json").load("../../data/spark_json/flight-data/json/2015-summary.json")

"""- spark.read.format("json").load("../../data/spark_json/flight-data/json/2015-summary.json").schema
    ```xml
    StructType( List( StructField(DEST_COUNTRY_NAME,StringType,true)
                     ,StructField(ORIGIN_COUNTRY_NAME,StringType,true)
                     ,StructField(count,LongType,true) )
                )
   ```
"""

df = spark.read.format("json").load("../../data/spark_json/flight-data/json/2015-summary.json")
df.printSchema()

df.take(3)

from pyspark.sql.types import StructField, StructType, StringType, LongType

myManualSchema = StructType([
    StructField("DEST_COUNTRY_NAME",StringType() ,True)
   ,StructField("ORIGIN_COUNTRY_NAME",StringType() ,True)
   ,StructField("count",LongType(), False, metadata={"hello":"world"})
    ])
# format 형식이 csv이면 "csv"
df = spark.read.format("json").schema(myManualSchema)\
    .load("../../data/spark_json/flight-data/json/2015-summary.json")

df.printSchema()

# pandas의 series
df.take(3)

from pyspark.sql.functions import col, column

col("someColumnName")
column("someColumnName")

type(df)

df.columns

from pyspark.sql import Row
myRow = Row("Hello", None, 1, False)

myRow[0]

myRow[1] # None 이므로 없음

myRow[2]

myRow[3]

df = spark.read.format("json").schema(myManualSchema)\
.load("../../data/spark_json/flight-data/json/2015-summary.json")

df.createOrReplaceTempView('dfTable')

myManualSchema = StructType([
    StructField("some",StringType() ,True)
   ,StructField("col",StringType() ,True)
   ,StructField("names",LongType(), False)
    ])

myRow = Row("Hello", None, 1)
myDf = spark.createDataFrame([myRow], myManualSchema)

myDf.show()

type(myDf)

df.printSchema()

"""### select
- select()안의 내용은 타언어들과 비슷함
    - 쿼리문을 알면 유리
        - if문 까지 가능함
"""

# TempView를 해주면 다음처럼 사용 가능
df.select("DEST_COUNTRY_NAME").show(2)

"""- 다음과 같은 효과
```SQL
SELECT DEST_COUNTRY_NAME FROM dfTable LIMIT 2
```
"""

df.select("DEST_COUNTRY_NAME", "ORIGIN_COUNTRY_NAME").show(2)

"""- 다음과 같은 효과
```SQL
SELECT DEST_COUNTRY_NAME, ORIGIN_COUNTRY_NAME FROM dfTable LIMIT 2
```

### select expression
- select에 추가로 연산이 들어가는
"""

# as 이름짓기 + Boolean으로 참/거짓 출력 (컬럼 생성)
df.selectExpr(
    "*", # 모든 원본 컬럼
    "(DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withincountry" 
    ).show(2)

"""```SQL
SELECT *, (DEST_COUNTRY_NAME = ORIGIN_COUNTRY_NAME) as withincountry
FROM dfTable
LIMIT 2
```
"""

df.selectExpr("avg(count)", "count(distinct(DEST_COUNTRY_NAME))").show(2)

"""```SQL
SELECT avg(count), count(distinct(DEST_COUTNRY_NAME))
FROM dfTable
LIMIT 2
```
"""

