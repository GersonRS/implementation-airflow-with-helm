from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from datetime import datetime, date
import pandas as pd
from pyspark.sql import Row
from pyspark.sql.functions import pandas_udf

# spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate())

conf = SparkConf()
conf.set("spark.shuffle.service.enabled", "false")
conf.set("spark.dynamicAllocation.enabled", "false")
conf.set("spark.executor.instances", "2")
conf.set("spark.cores.max", "1")
conf.set("spark.executor.memory", "600m")
conf.set("spark.executor.cores", "1")
spark = SparkContext(conf=SparkConf())

spark = SparkSession(SparkContext(conf=SparkConf()).getOrCreate())


df_times = spark.createDataFrame([
    Row(time='São Paulo', rebaixado=False, bom=True),
    Row(time='Sport', rebaixado=True, bom=False),
    Row(time='Santa Cruz', rebaixado=True, bom=False),
    Row(time='Flamengo', rebaixado=True, bom=False)
]) 

rdd_times = spark.parallelize([
    Row(time='São Paulo', rebaixado=False, bom=True),
    Row(time='Sport', rebaixado=True, bom=False),
    Row(time='Santa Cruz', rebaixado=True, bom=False),
    Row(time='Flamengo', rebaixado=True, bom=False)
])


# rdd_times.collect()

df_times.show()

# @pandas_udf('string')
# def pandas_plus_A(series: pd.Series) -> pd.Series:
#     return series + ' A'

# df_times.select(pandas_plus_A(df_times.time)).show()