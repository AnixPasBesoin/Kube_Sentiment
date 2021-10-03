apiVersion: v1
kind: Service
metadata:
  name: my-eval-service
  labels:
    app: my-eval-api
spec:
  type: ClusterIP
  ports:
  - port: 8002
    protocol: TCP
    targetPort: 8000
  selector:
    app: my-eval-api

