from pyspark.sql import SparkSession
from pyspark import SparkContext, SparkConf
from pyspark.sql import Row

if __name__ == '__main__':
    print('Cheguei aq!')
    conf = SparkConf()
    conf.set('spark.shuffle.service.enabled', 'false')
    conf.set('spark.dynamicAllocation.enabled', 'false')
    conf.set('spark.executor.instances', '2')
    conf.set('spark.cores.max', '1')
    conf.set('spark.executor.memory', '600m')
    conf.set('spark.executor.cores', '1')
    context = SparkContext(conf=SparkConf()).getOrCreate()
    spark = SparkSession(context)


    df_times = spark.createDataFrame([
        Row(time='São Paulo', rebaixado=False, bom=True),
        Row(time='Sport', rebaixado=True, bom=False),
        Row(time='Santa Cruz', rebaixado=True, bom=False),
        Row(time='Flamengo', rebaixado=True, bom=False)
    ]) 

    df_times.show()
    print('Deu bom!')

    spark.stop()