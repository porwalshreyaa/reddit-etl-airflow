from airflow import DAG
from airflow.providers.standard.operators.python import PythonOperator
from datetime import datetime
from etl.reddit_etl import fetch_and_store_reddit_posts

with DAG(
    dag_id="reddit_etl_pipeline",
    start_date=datetime(2025,6,18),
    schedule="@daily",
    catchup=False,
    tags=["reddit", "etl"]
) as dag:
    fetch_store_task = PythonOperator(
        task_id="fetch_reddit_posts",
        python_callable=fetch_and_store_reddit_posts
    )