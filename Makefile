all:
	sh setup-minikube.sh
requirements-airflow:
	pip install -r requirements_airflow.txt
airflow:
	AIRFLOW_HOME=$(pwd) airflow standalone