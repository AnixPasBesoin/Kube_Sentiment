## Kube_Sentiment

Using Kubernetes to deploy a data API composed of two services : a RESTful APIs in Python (simulating sentiment analysis) and a beckend DB in MySql.

The first part is wrapped into a docker container (inside the docker dir). The second is retrieved from dockerhub (datascientest/mysql-k8s:1.0.0). 

Other files are organized as follows :

- my-deployment-eval.yml : containing details on the pods
- my-service-eval.yml : describing the networking part (Service)
- my-ingress-eval.yml : Kubernetes Ingress part
- my-secret-eval.yml : Data needed for DB access (used through env variable)
 

