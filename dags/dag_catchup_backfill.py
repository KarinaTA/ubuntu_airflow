from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'KarinaT',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='dag_cathcup_backfill_v02',
    default_args=default_args,
    start_date=datetime(2025, 8, 28),
    schedule='@daily',
    catchup=False
    ) as dag:
    
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "This is a simple bash command!"'
    )