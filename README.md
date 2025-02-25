## Demo 

https://github.com/user-attachments/assets/ef070a30-5834-4573-a4ab-574c912e73af


# Wine Quality Prediction

## 📝 Description

This is an **end-to-end Machine Learning project** focused on **Wine Quality Prediction**, demonstrating best practices in **MLOps**. The project leverages cutting-edge tools and frameworks to manage, optimize, and serve machine learning models while ensuring scalability, reliability, and maintainability. The pipeline spans from data preparation to model deployment, monitoring, and visualization.

### Key Features:

1. **MLflow**: Used for model tracking, versioning, and experiment management. This allows us to log and compare different models, manage hyperparameter tuning, and track the entire lifecycle of machine learning experiments.

2. **Prefect**: Used for orchestration of the machine learning pipeline, enabling task management, scheduling, and monitoring of workflows. The pipeline is divided into different flows for training, deployment, and monitoring, ensuring smooth execution of ML operations.

3. **Hyperopt**: Integrated for hyperparameter optimization to find the best model configuration, maximizing the performance of machine learning algorithms.

4. **OmegaConf**: Configurations are managed using OmegaConf, allowing dynamic parameterization and easy management of configurations for different environments (e.g., development, production).

5. **FastAPI**: For serving the trained models in a high-performance, asynchronous web framework. FastAPI handles incoming prediction requests, loads the model, and returns the predictions in real-time.

6. **Docker & Docker Compose**: The entire project is containerized using Docker, and Docker Compose is used for managing multi-container setups. This includes services for **MLflow**, **Prefect**, **PostgreSQL**, and **Grafana**, providing a reliable and consistent environment for development, testing, and production.

7. **Grafana**: Integrated for monitoring model performance and drift detection. The model’s performance metrics and drift scores are visualized on Grafana, providing real-time insights into the health of the deployed model.

8. **PostgreSQL**: Used as the database for storing model metrics, logs, and other operational data. PostgreSQL ensures data persistence and scalability for large ML workloads.

9. **Adminer**: A lightweight database management tool for interacting with the PostgreSQL database, providing an easy-to-use interface for querying, managing, and monitoring the database.

10. **Deepchecks**: Used for model validation and drift detection, Deepchecks ensures that the deployed model's performance is consistently monitored and validated against real-world data. It helps track data drift, concept drift, and other model performance metrics.

#### Architecture Overview:

- **Data Preparation**: The pipeline begins with loading and preprocessing the wine quality dataset.
- **Model Training**: The data is fed into a model training process that is orchestrated by Prefect. Hyperopt is used to optimize the model’s hyperparameters for better performance.
- **Model Tracking**: During training, MLflow logs experiments, tracks model versions, and stores trained models for later deployment.
- **Model Deployment**: The trained models are served using FastAPI in Docker containers, providing a REST API for making predictions.
- **Monitoring**: Once deployed, the model’s predictions and performance are monitored using Grafana, which fetches metrics from the PostgreSQL database. Deepchecks continuously evaluates the model for data and concept drift.
- **Database**: PostgreSQL stores model metrics, logs, and drift scores, while Adminer provides a user-friendly interface for database management.

## ⏳ Dataset
the Red Wine Quality dataset from the UCI Machine Learning Repository 
- [Download Red Wine Quality Dataset (UCI)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
