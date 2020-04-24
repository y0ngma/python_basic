'''
# 다운로드
## 그래프
wget http://dl.bintray.com/spark-packages/maven/graphframes/graphframes/0.7.0-spark2.4-s_2.11/graphframes-0.7.0-spark2.4-s_2.11.jar
'''
#########graph########################################################
# 파일명 : graph01
from pyspark.sql import SparkSession

import os
os.environ['PYSPARK_PYTHON']='/home/user1/anaconda3/bin/python3'
os.environ['PYSPARK_DRIVER_PYTHON']='/home/user1/anaconda3/bin/python3'

spark = SparkSession.builder.master("local[*]").enableHiveSupport().appName("spark_app1") \
    .config('spark.driver.extraClassPath','/home/user1/graphframes-0.7.0-spark2.4-s_2.11.jar') \
    .config('spark.jars.packages', 'graphframes:graphframes:0.7.0-spark2.4-s_2.11').getOrCreate()

from graphframes import GraphFrame
from pyspark.sql.functions import desc     

# https://towardsdatascience.com/graphframes-in-jupyter-a-practical-guide-9b3b346cebc5
v1 = spark.createDataFrame([('1', 'Carter', 'Derrick', 50), 
                                  ('2', 'May', 'Derrick', 26),
                                 ('3', 'Mills', 'Jeff', 80),
                                  ('4', 'Hood', 'Robert', 65),
                                  ('5', 'Banks', 'Mike', 93),
                                 ('98', 'Berg', 'Tim', 28),
                                 ('99', 'Page', 'Allan', 16)],
                                 ['id', 'name', 'firstname', 'age'])
e1 = spark.createDataFrame([('1', '2', 'friend'), 
                               ('2', '1', 'friend'),
                              ('3', '1', 'friend'),
                              ('1', '3', 'friend'),
                               ('2', '3', 'follows'),
                               ('3', '4', 'friend'),
                               ('4', '3', 'friend'),
                               ('5', '3', 'friend'),
                               ('3', '5', 'friend'),
                               ('4', '5', 'follows'),
                              ('98', '99', 'friend'),
                              ('99', '98', 'friend')],
                              ['src', 'dst', 'type'])

########################################################                    

g = GraphFrame(v1, e1)
## Take a look at the DataFrames
#g.vertices.show()
print(g.vertices.count())
print(g.edges.count())

########################################################                    

# g.edges.show()
## Check the number of edges of each vertex
g.degrees.show()     

g.bfs(fromExpr="id='1'", toExpr="id='4'", maxPathLength=30).show(truncate=False)