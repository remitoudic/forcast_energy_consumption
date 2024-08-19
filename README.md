## Forecasting France's Global Energy Consumption

This project focuses on time series forecasting, utilizing historical daily data on France's energy consumption to predict future energy consumption. The historical data is sourced from [RTE](https://www.rte-france.com/en/home), France's Transmission System Operator. The data is available on their [data portal](https://www.services-rte.com/en/download-data-published-by-rte.html?category=consumption&type=energy_consumption) (a free account may be required). For convenience, the data used in this project has also been saved in a [Google Drive folder](https://drive.google.com/drive/folders/1-XpTf70thgwDp7z4k2AxOetPem9Mz5ya?usp=sharing).

The user interface for this project has two main components: one for the forecasting model and another for managing the model. The management interface is designed for MLOps purposes, enabling you to trigger the ETL pipeline, access Mage and MLflow dashboards, and monitor system performance.

![System Overview](./README_docs/sys_overview.png)

The project is deployed at this [IP address](http://34.173.156.32:3000).

### How to Run the Project Locally

The project is built with Docker Compose. Each folder contains a Dockerfile and a README related to different aspects of the course. These READMEs provide more detailed information about the implementation.

To run the project locally, follow these steps:

1. Clone the project repository:
   ```bash
   git clone git@gitlab.com:remitoudic/forcast_energy_consumption.git
    ```

2. start the project with docker compose:
    ```bash
    cd to the folder and run:
    docker compose up --build
    ```

3. You can check that the project is running properly if
go to http://remotes/origin/cloud_gcp:8000/system_health_check

4. Then trigger the ETL pipeline to create load and setup the  database.


### Mlops Topics:
Mlops practices have been implemented  on this project, for each step  find below a short description and some explication about the implementation:

- 1  Experient Tracking & model registring:
Experiment tracking and model registration are essential in the machine learning workflow, allowing researchers and developers to systematically track their experiments and efficiently share results. MLflow, an open-source tool, enables users to track models and parameters used during experiments, register models, and assign them to different environments. This ensures that the machine learning process is transparent, reproducible, and easily shareable

[More about tracking implemention in the project](1-tracking/README.md)

- 2 Pipeline orchestration simplifies the process of collecting, transforming, and integrating data. Tools like Mage AI allow you to schedule and run scripts easily through interfaces. Mage AI has a robust Python/UI interface, although it may have some bugs (e.g., it may not run well on Chrome but works smoothly on Firefox).

[More about Pipeline orchestration implemention in the project](2-orchestration/README.md)


- 3 Deployment is the core of this project, as it connects all system components. This includes a backend that facilitates communication between MLflow, Mage AI, and the monitoring system. It also includes a frontend server for the user interface, allowing interaction with the forecasting model.

[More about  the deployment implemention in the project](3-deployment/README.md)

- 4 Monitoring:
    - Service
    - Evidently AI


- 5 DevOps practices:
    - Continous Intergation has been done with Github Action.
    - Code quality:
        - Linter: flake 8
        - format: ruff
    - Cloud usage: the project is deploy on GCP.
    - API docs with OpenAPI
    - Testing /test coverage: Pytest


