FROM apache/airflow:2.8.1-python3.10

COPY requirements.txt .
COPY dags /opt/airflow/dags
COPY etl /opt/airflow/etl

# Install Python deps
RUN pip install --no-cache-dir -r requirements.txt

CMD ["airflow", "standalone"]