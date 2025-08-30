from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta


default_args = {
    'owner': 'KarinaT',
    'retries': 5,
    'retry_delay': timedelta(minutes=2)
}


def greet(name, age):
    print(f'Hello World! My name is {name}, '
          f'and I am {age} years old')


with DAG(
    dag_id='dag_python_operator_v02',
    description='My first dag using PythonOperator',
    default_args=default_args,
    start_date=datetime(2025,8,29),
    schedule='@daily',
    catchup=False
    ) as dag:
    
    task1 = PythonOperator(
        task_id='greet',
        python_callable=greet,
        op_kwargs={'name': 'Tom', 'age': 20}
    )
    
    task1