# Airflow 
- platform for developing, scheduling and monitoring batch-oriented workflows. 
- there's a web interface too. 
- workflows as code. 

## Internals 
- default database used in the backend is sqlite. 
- sqlite is sequential and not preferred for production deployment 

## Code: 
```bash 
# initialize the database tables
airflow db migrate

# print the list of active DAGs
airflow dags list

# prints the list of tasks in the "tutorial" DAG
airflow tasks list tutorial

# prints the hierarchy of tasks in the "tutorial" DAG
airflow tasks list tutorial --tree
```

## TODO:
- why does 'airflow tasks test' work but not 'airflow tasks run'
- https://airflow.apache.org/docs/apache-airflow/stable/tutorial/fundamentals.html
