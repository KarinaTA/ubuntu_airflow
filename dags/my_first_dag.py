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
    dag_id='my_first_dag_v2',
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
    
    task_2 = BashOperator(
        task_id='task_2',
        bash_command='echo "This is the second task and will be running after the first task!"'
    )
    
    task_3 = BashOperator(
        task_id='task_3',
        bash_command='echo "This is the third task and will be running at the same time as the second task!"'
    )
    
    # Task dependancy method 1 
    task_1 >> task_2
    task_1 >> task_3