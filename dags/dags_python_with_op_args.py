from airflow import DAG
import pendulum 
import datetime
from airflow.operators.python import PythonOperator
from common.common_func import regist

with DAG(
    dag_id="dags_python_with_op_args",
    schedule="30 1 * * *",
    start_date=pendulum.datetime(2026, 3, 1, tz="Asia/Seoul"),
    catchup=False,
) as dag:
    
    register_t1 = PythonOperator(
        task_id = "register_t1",
        python_callable=regist,
        op_args=['choisunghoon','man','kr','kyenggi']
    )

    register_t1    