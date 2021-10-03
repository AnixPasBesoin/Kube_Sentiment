apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: my-eval-ingress
spec:
  defaultBackend:
    service:
      name: my-eval-service
      port:
        number: 8002

