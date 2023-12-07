# Spark on Kubernetes

## Initializing Minikube

Read how to install Minikube:
https://minikube.sigs.k8s.io/docs/start/

We have to install Docker as well
https://docs.docker.com/engine/install/ubuntu/

Start Minikube:
```sh
$ sudo usermod -aG docker $USER
$ minikube start machine
$ minikube dashboard
```

## Deploying Spark on Minikube

Build the Docker image:

```sh
$ minikube docker-env
$ docker build -t spark-hadoop:latest -f ./docker/Dockerfile ./docker
```

Create the deployments and services:

```sh
$ kubectl create -f ./kubernetes/spark-master-deployment.yaml
$ kubectl create -f ./kubernetes/spark-master-service.yaml
$ kubectl create -f ./kubernetes/spark-worker-deployment.yaml
$ minikube addons enable ingress
$ kubectl apply -f ./kubernetes/minikube-ingress.yaml
```

Add an entry to hosts:

```sh
$ echo "$(minikube ip) " | sudo tee -a /etc/hosts
```

### Checking the new Spark cluster

Run on Spark to check that it works

```scala
val myWords = "HI HI HOW ARE YOU HAH"
val mySplit = myWords.split(" ").foldLeft(Map.empty[String, Int]) {
    (count, word) => count + (word -> (count.getOrElse(word, 0) + 1))
}
```

## Example notebook from Databricks

[Delta Lake](https://delta.io/) is an open-source storage layer that brings ACID transactions to Apache Spark™ and big data workloads. But it is **way more** then that!

This is a rewritten notebook example from this [blog post](https://databricks.com/blog/2019/10/03/simple-reliable-upserts-and-deletes-on-delta-lake-tables-using-python-apis.html) by Databricks. The intension is to show why Delta Lake is a big deal and how to run Delta Lake without a Databricks services.

Delta Lake examples in this notebook:
* Convert data to as Delta Lake format
* Create Delta Lake table
* Spark SQL capabilities
* Delete data
* Update data
* View audit history of table
* Merge (union) of two tables which remove duplicates, updates rows and add a new row

## Generate

Generate py-files:

```sh
pip install -r requirements
python ipynb2py.py
```

### Author

Example notebook [here](https://www.databricks.com/blog/2019/10/03/simple-reliable-upserts-and-deletes-on-delta-lake-tables-using-python-apis.html) [by](https://www.linkedin.com/in/andersboje/)
