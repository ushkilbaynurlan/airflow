from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.bash_operator import BashOperator

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'sequential_sleep_dag',
    default_args=default_args,
    description='DAG with sequential sleep tasks',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2024, 3, 29),
    catchup=False,
) as dag:

    sleep_300 = BashOperator(
        task_id='sleep_300',
        bash_command='sleep 300',
    )

    sleep_1000 = BashOperator(
        task_id='sleep_1000',
        bash_command='sleep 1000',
    )

    sleep_500 = BashOperator(
        task_id='sleep_500',
        bash_command='sleep 500',
    )

    sleep_300 >> sleep_1000 >> sleep_500
