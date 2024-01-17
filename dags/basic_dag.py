import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator


def add_two_numbers():
    return 10 + 10


def calculate_age():
    return 2024 - 1990


default_args = {
    'owner': 'yinka',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 11, 15),
    'retries': 5,
    'retry_delay': datetime.timedelta(seconds=10),
    'execution_timeout': datetime.timedelta(minutes=10)
}


dag = DAG(
    dag_id="core_data_eng_job",
    default_args=default_args,
    description='senior data engineer',
    schedule_interval="0 * * * *",
    max_active_runs=1,
    catchup=False
)

first = PythonOperator(
    dag=dag,
    task_id='add_two_numbers',
    python_callable=add_two_numbers
)

second = PythonOperator(
    dag=dag,
    task_id='calculate_age',
    python_callable=calculate_age

)
[add_two_numbers, calculate_age]
