from airflow import DAG
import pendulum
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist2

with DAG(
    dag_id="dags_python_with_op_kwargs",
    schedule="30 1 1 * *",
    start_date=pendulum.datetime(2024,1,1,tz="Asia/Seoul"),
    catchup=False
) as dag:

    regist2_t1 = PythonOperator(
        task_id = "regist2_t1",
        python_callable=regist2,
        op_args=['sdudekim','man','kr','seoul'],
        op_kwargs={'email':'walnam777@naver.com', 'phone':'01012121212'}
    )
    
    regist2_t1