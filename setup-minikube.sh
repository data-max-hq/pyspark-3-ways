SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"

minikube start \
	--mount --mount-string="$SCRIPTPATH/:/mnt" \
	--driver=docker \
	--memory 8192 --cpus 4

docker build . -t localspark
minikube image load localspark

kubectl create serviceaccount spark
kubectl create clusterrolebinding spark-role --clusterrole=edit --serviceaccount=default:spark --namespace=default

helm repo add spark-operator https://googlecloudplatform.github.io/spark-on-k8s-operator
helm upgrade --install spark-operator spark-operator/spark-operator \
	--namespace spark-operator --create-namespace \
	--set webhook.enable=true \
	--set sparkJobNamespace=default
