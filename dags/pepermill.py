import os
from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator

START_DATE = datetime(2021, 1, 1)
SCHEDULE_INTERVAL = '0 0 * * *'
DAGRUN_TIMEOUT = timedelta(minutes=60)

with DAG(
    dag_id='example_papermill_operator',
    schedule_interval=SCHEDULE_INTERVAL,
    start_date=START_DATE,
    dagrun_timeout=DAGRUN_TIMEOUT,
    tags=['batata'],
    catchup=False,
) as dag_1:
    # [START howto_operator_papermill]
    run_this = PapermillOperator(
        task_id="run_example_notebook",
        input_nb="/opt/airflow/dags/notebooks/papermill_job.ipynb",
        output_nb="/tmp/out-batata.ipynb",
    )
    # [END howto_operator_papermill]
    
    run_this

# @task
# def check_notebook(inlets, execution_date):
#     """
#     Verify the message in the notebook
#     """
#     notebook = sb.read_notebook(inlets[0].url)
#     message = notebook.scraps['message']
#     print(f"Message in notebook {message} for {execution_date}")

#     if message.data != f"Ran from Airflow at {execution_date}!":
#         return False

#     return True


# with DAG(
#     dag_id='example_papermill_operator_2',
#     schedule_interval=SCHEDULE_INTERVAL,
#     start_date=START_DATE,
#     dagrun_timeout=DAGRUN_TIMEOUT,
#     catchup=False,
# ) as dag_2:

#     run_this = PapermillOperator(
#         task_id="run_example_notebook",
#         input_nb=os.path.join(os.path.dirname(os.path.realpath(__file__)), "input_notebook.ipynb"),
#         output_nb="/tmp/out-{{ execution_date }}.ipynb",
#         parameters={"msgs": "Ran from Airflow at {{ execution_date }}!"},
#     )

#     run_this >> check_notebook(inlets=AUTO, execution_date="{{ execution_date }}")