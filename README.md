# Reddit Data Extraction Pipeline with Airflow, Docker & SQLite
(Didn't do the Transformation part yet)

![Screenshot 2025-06-19 041131](https://github.com/user-attachments/assets/90bcc2b7-50d5-4165-83eb-a66ba4893109)

A minimal ETL pipeline that extracts top 20 posts from `r/dataengineering` using Reddit API, stores them in SQLite, and orchestrates the job using Apache Airflow—all inside Docker.

---

## Tech Stack
- **Apache Airflow**
- **Python**
- **PRAW (Reddit API wrapper)**
- **SQLite**
- **Docker**

---

I started this project to teach myself Airflow and build a real, reproducible data pipeline. I ran into many bumps along the way, and completed it by 4 AM in the morning.

### Easy part?
Using Api and Fetching Data

### Difficult part?
Creating pipeline in Airflow to automate it

### More Difficult part?
Doing that inside docker

---

## What I wanted to get? (and got!)

![Screenshot 2025-06-19 040557](https://github.com/user-attachments/assets/985dbe74-4d83-478e-9d91-38c9553277f6)

---

## 🐋 DockerHub Image

https://hub.docker.com/r/porwalshreya/reddit-etl

Run via Docker
```
docker compose build --no-cache
docker compose up
```
Access Airflow:
- 🌐 http://localhost:8080
- 👤 admin & Your password (set via CLI if needed, I faced many issues, in the end I deleted admin and created new admin)

---

## TODO (v2 Ideas):
- Add DBT layer for SQL-based modeling
- Use Postgres instead of SQLite
- Add Slack or email alerts via Airflow
- Deploy to cloud (Azure or GCP)

---
### Some Supercool Jargon Airflow logs for flex

![Screenshot 2025-06-19 040624](https://github.com/user-attachments/assets/f59951dc-9776-4724-aa8a-1bf0d7dcc656)

---
Haha, thanks for visiting.
