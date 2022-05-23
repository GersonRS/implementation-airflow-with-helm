from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row

context = SparkContext(conf=SparkConf()).getOrCreate()
spark = SparkSession(context)


rows = [Row(time='São Paulo', rebaixado=False, bom=True)] * 1000000


df_times = spark.createDataFrame(rows) 

df_times.show(10)


# spark = SparkSession.builder.getOrCreate()

# # "code": "from pyspark.sql import SparkSession; from pyspark.sql import Row; spark = SparkSession.builder.getOrCreate(); df_times = spark.createDataFrame([Row(time='São Paulo', rebaixado=False, bom=True),Row(time='Sport', rebaixado=True, bom=False),Row(time='Santa Cruz', rebaixado=True, bom=False),Row(time='Flamengo', rebaixado=True, bom=False)]); df_times.show(); print('Deu bom!'); spark.stop()",

# # from pyspark.sql import SparkSession; from pyspark.sql import Row; spark = SparkSession.builder.getOrCreate();  df_times = spark.createDataFrame([Row(time='Santa Cruz', rebaixado=True, bom=False)]); df_times.show(); print('cheguei aq')
# from pyspark import SparkContext; spark = SparkContext.getOrCreate(); words = spark.parallelize (['scala', 'java', 'hadoop', 'spark', 'akka', 'spark vs hadoop', 'pyspark','pyspark and spark']); coll = words.collect(); print(f'Deu bom! {coll}');

# from pyspark import SparkContext; spark = SparkContext.getOrCreate(); df = spark.parallelize([(1, 2, 3, 'a b c'), (4, 5, 6, 'd e f'), (7, 8, 9, 'g h i')]).toDF(['col1', 'col2', 'col3','col4']); df.show()


# words = spark.sparkContext.parallelize (['scala', 'java', 'hadoop', 'spark', 'akka', 'spark vs hadoop', 'pyspark','pyspark and spark']); coll = words.collect(); print(f'Deu bom! {coll}'); print(spark.sparkContext.getConf().getAll())