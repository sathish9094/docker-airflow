from datetime import datetime
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

def print_greetings():
    return 'Hey Sathish ! Python Operator called me!'


#schedule for every 5 minutes
#Minutes specified as a number from 0 to 59.
#Hours specified as numbers from 0 to 23.
#Days of the month, specified as numbers from 1 to 31.
#Months specified as numbers from 1 to 12.
#Days of the week, specified as numbers from 0 to 7, with Sunday represented as either/both 0 and 7.

dag = DAG('python_operator',description='simple scheduler dag',schedule_interval='*/5 * * * *',
           start_date=datetime(2019,12,19),catchup=False)

dummy_operator = DummyOperator(task_id='dummy_task',retries=3,dag=dag)
hello_operator = PythonOperator(task_id='hello_task',python_callable=print_greetings,dag=dag)

dummy_operator >> hello_operator