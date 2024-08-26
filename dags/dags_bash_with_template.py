from airflow import DAG
import datetime
import pendulum

from airflow.operators.bash import BashOperator

with DAG(
    dag_id="dags_bash_with_template",
    schedule="10 0 * * *",
    start_date=pendulum.datetime(2024, 1, 1, tz="Asia/Seoul"),
    catchup=False,
    tags=["bash"],
) as dag:

    bash_t1 = BashOperator(
        task_id="bash_t1",
        bash_command=' echo "date_inteval_end: {{date_inteval_end}} " '
    )

    bash_t2 = BashOperator(
        task_id='bash_t2',
        env={
            'START_DATE' : '{{date_inteval_start | ds}}',
            'END_DATE': '{{date_inteval_end | ds}}'
        },
        bash_command='echo $START_DATE && echo $END_DATE'
    )

    bash_t1 >> bash_t2