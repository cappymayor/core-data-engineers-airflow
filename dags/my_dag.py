import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from module.utils import calculate_age

default_args = {
    'owner': 'yimika',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 11, 15),
    'retries': 3,
    'retry_delay': datetime.timedelta(seconds=5),
    'execution_timeout': datetime.timedelta(minutes=10)
}


dag = DAG(
    dag_id="core_data_engineers",
    default_args=default_args,
    description='senior data engineer',
    schedule_interval="0 * * * *",
    max_active_runs=1,
    catchup=False
)


default_args = {
    'owner': 'yimika',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 11, 15),
    'retries': 3,
    'retry_delay': datetime.timedelta(seconds=5),
    'execution_timeout': datetime.timedelta(minutes=10)
}


second = PythonOperator(
    dag=dag,
    task_id='calculate_age',
    python_callable=calculate_age

)
calculate_age
