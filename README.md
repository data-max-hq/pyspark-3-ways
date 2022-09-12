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

## How to run on GCP:
- Make sure you have the data uploaded on GCS
- Update the <bucket-name> in job_dataproc.py file
- When creating the Daraproc cluster make sure to include Anaconda
- Upload job_dataproc.py to GCS and submit job