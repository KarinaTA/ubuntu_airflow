from airflow import DAG
from airflow.operators.bash import BashOperator
#from airflow.utils.dates import days_ago
from datetime import datetime, timedelta


default_args={
    'owner': 'KarinaT',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    dag_id='my_first_dag',
    description='This is my first dag that I wrote',
    default_args=default_args,
    start_date=datetime(2025, 8, 28, 17),
    #start_date=days_ago(1),
    schedule='@daily',
    catchup=False
    
) as dag:
    task_1 = BashOperator(
        task_id='task_1',
        bash_command='echo "Hello, world! This is the first task!"'
    )
    
    task_1