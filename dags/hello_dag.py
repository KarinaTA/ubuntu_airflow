from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

with DAG(
    dag_id="hello_world",
    start_date=datetime(2025, 1, 1),
    schedule=None,
    catchup=False,
) as dag:
    task = BashOperator(
        task_id="say_hi",
        bash_command="echo 'Hello Airflow!'"
    )
