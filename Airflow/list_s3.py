from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import subprocess

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 6, 5),
    'email': ['your_email@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

dag = DAG(
    dag_id='s3_ls_dag',
    default_args=default_args,
    schedule_interval='*/3 * * * *',
    catchup=False
)

def run_aws_s3_ls():
    subprocess.run(['aws', 's3', 'ls'], check=True)

def run_aws_s3_ls_bucket():
    subprocess.run(['aws', 's3', 'ls', 's3://your_bucket_name'], check=True)

list_s3_bucket = PythonOperator(
    task_id='list_s3_bucket',
    python_callable=run_aws_s3_ls,
    dag=dag
)

list_s3_directory = PythonOperator(
    task_id='list_s3_directory',
    python_callable=run_aws_s3_ls_bucket,
    dag=dag
)

list_s3_bucket >> list_s3_directory
