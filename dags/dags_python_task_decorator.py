from airflow import DAG
import pendulum
from airflow.decorators import task

with DAG(
    dag_id="dags_python_task_decorator",
    schedule="0 2 * * 1",
    start_date=pendulum.datetime(2024,1,1,tz="Asia/Seoul"),
    catchup=False
) as dag:

    @task(task_id="python_task_1")
    def print_context(input_text):
        print(input_text)

    
    python_task_1 =  print_context("task test !!!!")
