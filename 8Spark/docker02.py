#-----------------------------------------------
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType, IntegerType, DoubleType, DateType

spark = SparkSession.builder.enableHiveSupport() \
        .appName("pipeline_sample") \
        .master("local[*]") \
        .getOrCreate()
        
# 훈련용 데이터 (키, 몸무게, 나이, 성별)
df1 = spark.createDataFrame([
    (161.0, 69.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 58.32, 29, 0.0),
    (163.0, 70.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 60.32, 29, 0.0),
    (169.4, 75.3, 42, 0.0),
    (168.4, 76.3, 42, 0.0),
    (185.1, 85.0, 37, 1.0),
    (161.6, 61.2, 28, 1.0)
]).toDF("height", "weight", "age", "gender")  

df1.printSchema()
df1.show()


schema = StructType() \
    .add("height", DoubleType(), True) \
    .add("weight", DoubleType(), True) \
    .add("age", IntegerType(), True) \
    .add("gender", DoubleType(), True)

df2 = spark.createDataFrame([
    (161.0, 69.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 58.32, 29, 0.0),
    (163.0, 70.87, 29, 1.0),
    (176.78, 74.35, 34, 1.0),
    (159.23, 60.32, 29, 0.0),
    (169.4, 75.3, 42, 0.0),
    (168.4, 76.3, 42, 0.0),
    (185.1, 85.0, 37, 1.0),
    (161.6, 61.2, 28, 1.0)], schema) 
df2.printSchema()
df2.show()

from pyspark.ml.classification import LogisticRegression
from pyspark.ml.classification import LogisticRegressionModel
from pyspark.ml.feature import VectorAssembler
from pyspark.ml.pipeline import Pipeline
from pyspark.ml.pipeline import PipelineModel

assembler = VectorAssembler(inputCols=["height", "weight", "age"], outputCol="features")

# training 데이터에 features 컬럼 추가
# assembled_training = assembler.transform(df2)
# assembled_training.show(truncate=False)

# 모델 생성 알고리즘 (로지스틱 회귀 평가자)
lr = LogisticRegression(maxIter=10, regParam=0.01, labelCol="gender")

pipeline = Pipeline(stages=[assembler, lr]) # 파이프라인
pipelineModel = pipeline.fit(df2) # 파이프라인 모델 생성
pipelineModel.transform(df2).show(truncate=False) # 파이프라인 모델을 이용한 예측값 생성

#---------------------------------------------------------
