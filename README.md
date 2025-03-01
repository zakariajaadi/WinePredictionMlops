
# Industrializing ML with MLOps: Wine Quality Pipeline 🍷

## 📝 Description

This end-to-end machine learning project serves as a blueprint for deploying ML models with **MLOps** principles. The **primary goal** is to demonstrate the complete journey from a trained model to a production-ready, industrialized pipeline, rather than achieving state-of-the-art accuracy in prediction. 

For this demonstration, I use a wine quality prediction model, specifically an Elastic Net regression, to predict wine quality based on its chemical composition (e.g., acidity, sugar, pH). (More info on this below)

The project spans the entire ML lifecycle from data extraction to model deployment, and monitoring and covers major aspects of MLOps, including :
* Pipeline automation and orchestration.
* Experiment tracking and model versioning.
* Automated deployment and monitoring. 
* Horizontal Scaling

## 🚀 Demo video 
Watch this brief demo video to see the complete process, from data preparation all the way through to model deployment and monitoring.

https://github.com/user-attachments/assets/c9bf8485-51b6-4fe6-8346-04702c296454


## 📦 Key Tools
* **🐳 Docker & Docker Compose**: The entire project is containerized using Docker, and Docker Compose is used for managing multi-container setups. This includes services for **MLflow**, **Prefect**, **PostgreSQL**, and **Grafana**.  

* **📊 MLflow**: Used to track training experiments for easy comparison and model selection, and also to help version and manage models  to streamline deployment. 

* **⛓️ Prefect**: Used to orchestrate the ML pipeline by managing tasks, scheduling, and monitoring. Two flows were implemented: one for model training and automatic deployment, and another for model monitoring.  

* **🎯 Hyperopt**: Used to optimize hyperparameters by exploring exclusively promising regions, which contributed in enhancing model performance.  

* **🧪 Deepchecks**: Used to detect both Features and Prediction drift, ensuring consistent model performance and early identification of potential issues.  

* **📈 Grafana**: Used to visualize drift scores and to provide alerts for drift detection, enabling real-time insights into deployed model health.  

* **🚀 FastAPI**: Used to serve trained models and handle prediction requests in real-time.  

* **⚙️ OmegaConf**: Used to manage configurations, enabling dynamic parameterization across different environments.  

* **📦 Poetry**: Used to manage project dependencies and virtual environments, for reproducible and consistent development.  

* **🐘 PostgreSQL**: Housed both the MLflow backend database and the monitoring database.  

* **🖥️ Adminer**: Adminer provided a light-weight front-end to manage and monitor the PostgreSQL database.  

## 📊  Dataset

This project uses the **Red Wine Quality dataset from the UCI Machine Learning Repository** to predict the quality of red wine based on various chemical properties, such as alcohol content, acidity, and pH.

- [Download Red Wine Quality Dataset (UCI)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

## 🧙 Model 

The **Wine Quality Prediction Model** is built using **ElasticNet** regression, a linear regression technique that balances Lasso (L1) and Ridge (L2) regularization.

**Hyperopt** is used for hyperparameter tuning to find the best values for `alpha` regularization strength and `l1_ratio` balance between L1 and L2 penalties.

## 🛠️ Installation

To set up the project locally, make sure you have **Make**, **Docker** and **Docker Compose** pre-installed**, then proceed with the following steps:

1. Clone the repository:

   ```bash
   git clone https://github.com/zakariajaadi/WinePredictionMlops.git
   cd WinePredictionMlops
   ```
2. Build flow image:

   ```bash
   make build-flow-image # Builds the Docker image for the Prefect flows
   ```
3. Run docker containers:
   ```bash
   make compose-up-app # Starts all application containers using Docker Compose.
   ```
4. Deploy flows in prefect:
   ```bash
   make deploy-all-flows # Deploys all Prefect flows to the Prefect server
   ```
5. Run flows in prefect UI:

Access the prefect UI (`http://localhost:4200`), navigate to Deployments, and trigger a flow Run.

6. Access the services:

    * Prefect UI: `http://localhost:4200` 
    * MLflow UI: `http://localhost:5000` 
    * Grafana: `http://localhost:3000` 
    * Adminer: `http://localhost:8080` 
    * Fast API model serving: `http://localhost:8000`
   
7. **To stop the services:**
    ```bash
    make compose-down #Stops the docker containers.
    ```
## 📜 License
This project is licensed under the MIT License.

## 🚧 Future Improvements
- Integrate CI/CD.
- Integrate data versioning with DVC
- Migrate the project to Kubernetes for improved scalability.
