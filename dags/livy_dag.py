from datetime import datetime

from airflow import DAG
from airflow.providers.apache.livy.operators.livy import LivyOperator

livy_default


with DAG(
    dag_id='example_livy_operator',
    default_args={'args': [10]},
    schedule_interval='@daily',
    start_date=datetime(2021, 1, 1),
    catchup=False,
) as dag:

    livy_python_task = LivyOperator(task_id='pi_python_task', file='/opt/airflow/dags/spark_jobs/livy_code.py', polling_interval=60)

    livy_python_task