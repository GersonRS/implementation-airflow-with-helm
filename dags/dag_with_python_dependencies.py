from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.python import PythonOperator

default_args = {
    'owner': 'gerson',
    'retry': 5,
    'retry_delay': timedelta(minutes=5)
}


def get_sklearn():
    import sklearn
    print(f"sklearn with version: {sklearn.__version__} ")

with DAG(
    default_args=default_args,
    dag_id="dag_with_python_dependencies_v03",
    start_date=datetime(2022, 5, 24),
    schedule_interval='@daily'
) as dag:
    task1 = PythonOperator(
        task_id='get_sklearn',
        python_callable=get_sklearn
    )

    task1
