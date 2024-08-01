#!/bin/bash

# Start Jupyter Notebook server
jupyter notebook --ip 0.0.0.0 --no-browser --allow-root   --NotebookApp.token='' --NotebookApp.password=''&

# Start MLflow server
mlflow server --backend-store-uri sqlite:///mlflow.db --host 0.0.0.0 --port 5000