from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator


args = {
    'owner': 'KarinaT',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    default_args=args,
    dag_id='dag_cron_expression_v02',
    start_date=datetime(2025, 8, 25),
    schedule='0 0 * * *'
    ) as dag:
    task1 = BashOperator(
        task_id='task1',
        bash_command='echo "dag with cron expression!"'
    )
    
    task1