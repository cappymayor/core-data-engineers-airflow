import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from faker_profile import data_extract_to_s3

default_args = {
    'owner': 'data-eng-new',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 12, 15),
    'retries': 5,
    'retry_delay': datetime.timedelta(seconds=10),
    'execution_timeout': datetime.timedelta(minutes=10),
}

dag = DAG(
    dag_id="fakers_user_ingestion",
    default_args=default_args,
    description='Ingesting faker profile datasets',
    schedule_interval="0 * * * *",
    max_active_runs=1,
    catchup=False
)

data_extract_to_s3 = PythonOperator(
    dag=dag,
    task_id='data_extract_to_s3',
    python_callable=data_extract_to_s3
)

data_extract_to_s3
