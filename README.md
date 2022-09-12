# This project shows how to run a pyspark job on Kubernetes, GCP and Airflow

## Simple PySpark model built. Download required dataset in link below:
https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data

## How to run locally on Kubernetes using SparkOperator:
1. Prerequisites:
- Docker
- Minikube

2. Create minikube cluster, build and load image to minikube, and deploy SparkOperator
```bash
make all
```

3. Apply pyspark job
```bash
kubectl apply -f job.yaml
```

4. Port-forward Spark UI. Open Spark UI at https://localhost:4040
```bash
kubectl port-forward pyspark-job-driver 4040:4040
```

5. Check out logs for model accuracy
```bash
kubectl -n=default logs -f pyspark-job-driver | grep accuracy
```

## How to run on GCP:
- Make sure you have the data uploaded on GCS
- Update the \<bucket-name\> in job_dataproc.py file
- When creating the Daraproc cluster make sure to include Anaconda
- Upload job_dataproc.py to GCS and submit job

## How to run on Airflow locally:
1. Install requirements:
    ```bash
    pip install -r requirements_airflow.txt
    ```
2. Run Airflow:
    ```bash
    AIRFLOW_HOME=$(pwd) airflow standalone
    ```
3. Remove example DAGs. Open `airflow.cfg`, change `load_examples = True` to `load_examples = False`
4. Log in to Airflow UI:
    ```
    url: http://localhost:8080
    username: admin
    password: <show during start or in standalone_admin_password.txt>
    ```