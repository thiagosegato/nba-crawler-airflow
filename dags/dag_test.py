from airflow.decorators import task
from airflow.utils.dates import days_ago
from airflow import DAG

with DAG(
    dag_id='dag_test',
    description='Uma apresentação de uma DAG mais simples',
    start_date=days_ago(2), schedule="@once") as dag:

    @task()
    def tarefa1():
        print('Executando tarefa 1')

    @task()
    def tarefa2():
        print('Executando tarefa 2')

    tarefa1() >> tarefa2()




    