
# Wine Quality Prediction

## 📝 Description

This **end-to-end** machine learning project aims to **industrialize** a model for predicting wine quality, showcasing practical **MLOps** best practices. It uses modern tools to manage, optimize, and deploy machine learning models, ensuring the pipeline is scalable, reliable, reproducible and easy to maintain. 

The project spans everything from data extraction to model deployment, and monitoring and covers major aspects of MLOps, including :
* Pipeline automation and orchestration.
* Experiment tracking and model versioning.
* Automated deployment and monitoring. 
* Horizontal Scaling

## 🚀 Demo video : 

Watch this demo video to see the end-to-end process, from data preparation to model deployment and monitoring

https://github.com/user-attachments/assets/ef070a30-5834-4573-a4ab-574c912e73af


## 📦 Key Tools:  
* **🐳 Docker & Docker Compose**: The entire project is containerized using Docker, and Docker Compose is used for managing multi-container setups. This includes services for **MLflow**, **Prefect**, **PostgreSQL**, and **Grafana**.  

* **📊 MLflow**: Used to track training experiments for easy comparison and model selection, while also helping with versioning and managing models to streamline deployment.  

* **⛓️ Prefect**: Used to orchestrate the ML pipeline by managing tasks, scheduling, and monitoring. Two flows were implemented: one for model training and automatic deployment, and another for model monitoring.  

* **🎯 Hyperopt**: Used to optimize hyperparameters by efficiently exploring only promising regions, which contributed to enhancing model performance.  

* **🧪 Deepchecks**: Used to detect both Features and Prediction drift, ensuring consistent model performance and early identification of potential issues.  

* **📈 Grafana**: Used to visualize drift scores and to provide alerts for drift detection, offering real-time insights into deployed model health.  

* **🚀 FastAPI**: Used to serve trained models and handle prediction requests in real-time.  

* **⚙️ OmegaConf**: Used to manage configurations, enabling dynamic parameterization across different environments.  

* **📦 Poetry**: Used to manage project dependencies and virtual environments, ensuring consistent and reproducible development.  

* **🐘 PostgreSQL**: Housed both the MLflow backend database and the monitoring database.  

* **🖥️ Adminer**: Adminer provided a lightweight interface for managing and monitoring the PostgreSQL database.  

## ⏳ Dataset

This project uses the **Red Wine Quality dataset from the UCI Machine Learning Repository** to predict the quality of red wine based on various chemical properties, such as alcohol content, acidity, and pH, helping winemakers assess and improve their product.

- [Download Red Wine Quality Dataset (UCI)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)

## 🛠️ Installation

To set up the project locally, ensure you have **Make, Docker and Docker Compose pre-installed**, then follow these steps:

1. **Clone the repository:**

   ```bash
   git clone zakariajaadi/WinePredictionMlops
   cd WinePredictionMlops
   ```
2. **Build flow image:**

   ```bash
   make build-flow-image # Builds the Docker image for the Prefect flows
   ```
3. **Run docker containers:**
   ```bash
   make compose-up-app # Starts all application containers using Docker Compose.
   ```
4. **Deploy flows in prefect:**
   ```bash
   make deploy-all-flows # Deploys all Prefect flows to the Prefect server
   ```
5. **Run flows in prefect UI:**

Access the prefect UI (`http://localhost:4200`), navigate to Deployments, and trigger a flow Run.

6. **Access the services:**

    * **Prefect UI:** `http://localhost:4200` 
    * **MLflow UI:** `http://localhost:5000` 
    * **Grafana:** `http://localhost:3000` 
    * **Adminer:** `http://localhost:8080` 
    * **Fast API model serving:** `http://localhost:8000` 

## You're all set! The application is now running. 🏃
