import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from module.utils import customer_age

default_args = {
    'owner': 'data-eng-new',
    'depends_on_past': False,
    'start_date': datetime.datetime(2021, 12, 15),
    'retries': 5,
    'retry_delay': datetime.timedelta(seconds=10),
    'execution_timeout': datetime.timedelta(minutes=10),
    'birth_year': 1980
}

dag = DAG(
    dag_id="data_core_new_job",
    default_args=default_args,
    description='holyghost fire',
    schedule_interval="0 * * * *",
    max_active_runs=1,
    catchup=False
)

first = PythonOperator(
    dag=dag,
    task_id='print_customer_age',
    python_callable=lambda **kwargs: print(f"The age of the customer is:\
        {customer_age(kwargs['dag_run'].conf.get('birth_year', 1980))}"),
    provide_context=True,
)

customer_age
