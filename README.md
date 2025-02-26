
# Wine Quality Prediction

## 📝 Description

This is an **end-to-end** machine learning project aimed at **industrializing** a model for predicting wine quality, showcasing practical **MLOps** best practices. It uses modern tools to manage, optimize, and deploy machine learning models, ensuring the pipeline is scalable, reliable, and easy to maintain. 

The project covers major aspects of MLOps, including :
* Pipeline automation and orchestration.
* Experiment tracking and model versioning.
* Automated deployment and monitoring. 
* Scaling

The project spans everything from data extraction to model deployment, monitoring, and visualization.
## 🚀 Demo video : 

https://github.com/user-attachments/assets/ef070a30-5834-4573-a4ab-574c912e73af


##  🛠️ Key Tools: 

1. **Docker & Docker Compose**: The entire project is containerized using Docker, and Docker Compose is used for managing multi-container setups. This includes services for **MLflow**, **Prefect**, **PostgreSQL**, and **Grafana**.

2. **MLflow**: Used to track training experiments for easy comparison and model selection, while also helping with versioning and managing models to streamline deployment.

3. **Prefect**: Used to orchestrate the ML pipeline by managing tasks, scheduling, and monitoring. Two flows were implemented: one for model training and automatic deployment, and another for model monitoring.

4. **Hyperopt**: Used to optimize hyperparameters by efficiently exploring only promising regions, which contributed to enhancing model performance.

5. **Deepchecks**: Used to detect both Features and Prediction drift, ensuring consistent model performance and early identification of potential issues.

6. **Grafana**: Used to visualize drift scores and to provide alerts for drift detection, offering real-time insights into deployed model health.

7. **FastAPI**: Used to serve trained models and handle prediction requests in real-time.

8. **OmegaConf**: Used to manage configurations, enabling dynamic parameterization across different environments.

9. **Poetry** : Used to manage project dependencies and virtual environments, ensuring consistent and reproducible development.

10. **PostgreSQL**: Housed both the MLflow backend database and the monitoring database.

11. **Adminer**: Adminer provided a lightweight interface for managing and monitoring the PostgreSQL database.


## ⏳ Dataset
the Red Wine Quality dataset from the UCI Machine Learning Repository was used for model training and evaluation.
- [Download Red Wine Quality Dataset (UCI)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
