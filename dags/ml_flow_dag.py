from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def preprocess_data():
    # code to preprocess data for machine learning
    print("preprocess data")

def train_model():
    # code to train machine learning model
    print("train model")

def evaluate_model():
    # code to evaluate model performance
    print("evaluate model")

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2024, 4, 1),
    'email_on_failure': False,
    'email_on_retry': False,
}

dag = DAG('ml_pipeline', default_args=default_args, schedule_interval='@weekly')

preprocess_task = PythonOperator(
    task_id='preprocess_data',
    python_callable=preprocess_data,
    dag=dag
)

train_task = PythonOperator(
    task_id='train_model',
    python_callable=train_model,
    dag=dag
)

evaluate_task = PythonOperator(
    task_id='evaluate_model',
    python_callable=evaluate_model,
    dag=dag
)

preprocess_task >> train_task >> evaluate_task
