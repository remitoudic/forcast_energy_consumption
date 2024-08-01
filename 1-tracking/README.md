# About Experiment tracking and model registry

## About mflow setup:  

[Experiement Notebook](http://localhost:8888/notebooks/MLOPS_Project.ipynb)
If you explore and run the jupyter notebook you will be able to  find some 
    -  hyperparameter tuning 
    -  experiment tracking 
    -  data version control 
    -  model registry 



The server  mlflow server is available on port http://localhost:5000/

<img src="./docs/mflow_setup.png " alt="drawing" width="400" class="center/>

If you want to reproduce the experiments and try model management model registry.You can access the notebook and run it from the docker container. 

http://localhost:8888/notebooks/notebook_experiment.ipynb

Data will  produced  in the container folder mlruns and models,   
the sqlite database. It should be produced locally as well as in the container.

<img src="./docs/run_all_cells_pics.png" alt="drawing" width="400"/>

it lasts around 5 minutes to run. 

Ater that  you should see

An overview of all the runs 

<img src="./docs/mlflows_runs.png" alt="drawing" width="4 00"/>

you can click on an a specific run  and have an overview of all the parameters 

<img src="./docs/run_overview.png" alt="drawing" width="400"/>

 as well as  the artifacts log

<img src="./docs/mlflow_artifacts.png" alt="drawing" width="400"/>

and finally you can also see the model registered

<img src="./docs/model_registry.png" alt="drawing" width="400"/>
