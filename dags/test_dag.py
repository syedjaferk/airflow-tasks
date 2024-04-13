from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 3, 31),
}

# Define the DAG
dag = DAG(
    'test_dag',
    default_args=default_args,
    description='A simple example DAG',
    schedule_interval='@daily',
)

# Define tasks
task1 = BashOperator(task_id="hello3", bash_command="echo task1", dag=dag)
task2 = BashOperator(task_id="hello2", bash_command="echo task2", dag=dag)
task3 = BashOperator(task_id="hello1", bash_command="echo task3", dag=dag)

# Set task dependencies
task1 >> task2 >> task3
