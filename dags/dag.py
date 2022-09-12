from airflow import DAG
from datetime import datetime, timedelta
from airflow.contrib.operators.spark_submit_operator import SparkSubmitOperator

default_args = {
    "owner": "local",
    "start_date": datetime(2022, 9, 12),
    "retries": 5,
    "retry_delay": timedelta(hours=1),
}
with DAG("spark", default_args=default_args, schedule_interval="0 1 * * *") as dag:
    pyspark_job = SparkSubmitOperator(
        task_id="pyspark_job", conn_id="spark", application="job_airflow.py", dag=dag
    )
    pyspark_job

if __name__ == "__main__":
    dag.cli()