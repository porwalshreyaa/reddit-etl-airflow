from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

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