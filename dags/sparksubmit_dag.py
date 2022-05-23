import airflow
from datetime import timedelta
from airflow import DAG
from airflow.providers.apache.spark.operators.spark_submit import SparkSubmitOperator 
from airflow.utils.dates import days_ago

default_args = {
    'owner': 'airflow',
    'retry_delay': timedelta(minutes=5),
}

dag_spark = DAG(
        dag_id = "sparkoperator_demo",
        default_args=default_args,
        schedule_interval='@once',	
        dagrun_timeout=timedelta(minutes=60),
        description='use case of sparkoperator in airflow',
        start_date = airflow.utils.dates.days_ago(1)
)

spark_submit_local = SparkSubmitOperator(
		application ='/opt/airflow/dags/spark_jobs/sparksubmit_test.py' ,
		conn_id= 'spark_local', 
		task_id='spark_submit_task',
		dag=dag_spark
		)

spark_submit_local