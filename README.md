
# Wine Quality Prediction
## 🚀 Demo video : 

https://github.com/user-attachments/assets/ef070a30-5834-4573-a4ab-574c912e73af

## 📝 Description

This is an **end-to-end Machine Learning project** focused on **Wine Quality Prediction**, demonstrating best practices in **MLOps**. The project leverages cutting-edge tools and frameworks to manage, optimize, and serve machine learning models while ensuring scalability, reliability, and maintainability. The pipeline spans from data preparation to model deployment, monitoring, and visualization.

### Key Tools:

1. **MLflow**: Tracked training experiments for easy comparison and model selection while versioning and managing models to streamline deployment.

2. **Prefect**: Prefect orchestrated the ML pipeline, managing tasks, scheduling, and monitoring.  Two flows were implemented: one for training and automatic deployment, and another for model monitoring.

3. **Hyperopt**: Optimized hyperparameters by efficiently exploring only promising regions to enhance model performance.

4. **Deepchecks**: Detected both feature and prediction drift, ensuring consistent model performance and early identification of potential issues.

5. **Docker & Docker Compose**: The entire project is containerized using Docker, and Docker Compose is used for managing multi-container setups. This includes services for **MLflow**, **Prefect**, **PostgreSQL**, and **Grafana**.

6. **Grafana**: Visualized drift scores and provided alerts for drift detection, offering real-time insights into deployed model health.

7. **FastAPI**: Served trained models and handled prediction requests in real-time.

8. **OmegaConf**: OmegaConf managed configurations, enabling dynamic parameterization across different environments.

9. **Poetry** : Poetry managed project dependencies and virtual environments for consistent and reproducible development.


8. **PostgreSQL**: Housed both the MLflow backend database and the monitoring database.

9. **Adminer**: Adminer provided a lightweight interface for managing and monitoring the PostgreSQL database.


## ⏳ Dataset
the Red Wine Quality dataset from the UCI Machine Learning Repository was used for model training and evaluation.
- [Download Red Wine Quality Dataset (UCI)](https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv)
