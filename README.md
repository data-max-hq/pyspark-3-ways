# Simple PySpark model built for:
https://www.kaggle.com/competitions/kkbox-churn-prediction-challenge/data

### The model is trained in a local minikube cluster using spark-on-k8s-operator:
https://github.com/GoogleCloudPlatform/spark-on-k8s-operator

## How to run locally:
- Make sure u have docker and minikube installed

- Then run
```bash
make all
```
To set up the local minikube cluster with spark-operator

- Then apply the job
```bash
kubectl apply -f job.yaml
```

### Port-forward Spark UI
```bash
kubectl port-forward pyspark-job-driver 4040:4040
```

### Check out logs for model accuracy
```bash
kubectl -n=default logs -f pyspark-job-driver | grep accuracy
```

## How to run on GCP:
- Make sure you have the data uploaded on GCS
- Update the \<bucket-name\> in job_dataproc.py file
- When creating the Daraproc cluster make sure to include Anaconda
- Upload job_dataproc.py to GCS and submit job

## How to run on Airflow locally:
- Install requirements:
    ```bash
    pip install requirements_airflow.txt
    ```
- Run Airflow:
    ```bash
    AIRFLOW_HOME=$(pwd) airflow standalone
    ```
- Remove example DAGs. Open `airflow.cfg`, change `load_examples = True` to `load_examples = False`
- Log in to Airflow UI:
    ```bash
    url: http://localhost:8080
    username: admin
    password: <show during start or in standalone_admin_password.txt>
    ```