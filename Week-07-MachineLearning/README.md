# Week 7 - Machine Learning

This folder contains machine learning assignments completed as part of the Miuul Data Science Bootcamp.

The studies focus on regression and classification model evaluation, performance metrics, customer churn prediction, feature engineering, and hyperparameter optimization.

---

## 1. Regression Models - Error Evaluation

**Notebook:** `Regression_models_error_evaluation.ipynb`

This study focuses on evaluating regression model predictions using common error metrics.

### Topics Covered

- Prediction errors and residuals
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)
- Regression model performance evaluation

---

## 2. Classification Model Evaluation

**Notebook:** `classification_model_evaluation.ipynb`

This assignment focuses on evaluating classification models using confusion matrix components and common classification metrics.

### Topics Covered

- Confusion Matrix
- True Positive (TP)
- True Negative (TN)
- False Positive (FP)
- False Negative (FN)
- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

---

## 3. Telco Customer Churn Prediction

**Notebook:** `telco_customer_churn.ipynb`

This project develops a machine learning workflow to predict customer churn using the Telco Customer Churn dataset.

### Project Workflow

- Exploratory Data Analysis (EDA)
- Categorical and numerical variable analysis
- Missing value analysis
- Outlier analysis
- Feature engineering
- Label Encoding
- One-Hot Encoding
- Feature scaling
- Model comparison with cross-validation
- Hyperparameter optimization
- Feature importance analysis

### Models Evaluated

- Logistic Regression
- K-Nearest Neighbors (KNN)
- Decision Tree (CART)
- Random Forest
- Support Vector Machine (SVM)
- XGBoost
- LightGBM
- CatBoost

### Hyperparameter Optimization

GridSearchCV was used to optimize:

- Random Forest
- XGBoost
- LightGBM
- CatBoost

Model performance was evaluated using 5-fold cross-validation and the following metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

### Final Results

Logistic Regression achieved the strongest overall performance with a **ROC-AUC of 0.850**.

Hyperparameter optimization improved the ensemble models, with Tuned CatBoost achieving the highest ROC-AUC among the optimized models at **0.847**.

Feature importance analysis also showed that several engineered features contributed significantly to churn prediction, particularly:

- `NEW_ENGAGED`
- `NEW_AVG_SERVICE_FEE`
- `NEW_INCREASE`
- `NEW_AVG_CHARGES`
- `NEW_TOTAL_SERVICES`

This demonstrates that more complex algorithms do not necessarily outperform simpler models and highlights the importance of feature engineering and systematic model comparison.

---

## Technologies

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- XGBoost
- LightGBM
- CatBoost
- Jupyter Notebook

---

## Dataset

The Telco Customer Churn dataset contains customer-level information including demographic characteristics, subscribed services, contract information, charges, tenure, and churn status.

The objective is to identify patterns associated with customer churn and develop machine learning models capable of predicting customers who are likely to leave the company.
