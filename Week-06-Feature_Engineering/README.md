# 🩺 Diabetes Feature Engineering

This project demonstrates a complete **Feature Engineering** workflow using the **Pima Indians Diabetes Dataset**. The primary goal is to improve machine learning model performance by applying data preprocessing techniques and creating meaningful new features based on domain knowledge.

The project follows an end-to-end machine learning preprocessing pipeline, from exploratory data analysis to final model evaluation.

---

## 📌 Project Objectives

- Perform Exploratory Data Analysis (EDA)
- Detect and handle missing values
- Detect and cap outliers
- Create meaningful engineered features
- Encode categorical variables
- Scale numerical variables
- Train and evaluate a Random Forest classifier
- Compare the baseline model with the engineered model

---

## 📂 Dataset

**Dataset:** Pima Indians Diabetes Database

The dataset contains medical information collected from female patients and aims to predict whether a patient has diabetes.

**Target Variable**

- `Outcome`
  - 0 → Non-diabetic
  - 1 → Diabetic

---

##  Project Workflow

### 1. Data Preparation

- Imported required libraries
- Loaded the dataset
- Configured notebook display settings

### 2. Exploratory Data Analysis (EDA)

- Dataset overview
- Variable type detection
- Missing value inspection
- Numerical feature analysis
- Target variable analysis
- Correlation analysis

### 3. Baseline Model

A baseline Random Forest model was trained before any preprocessing steps to establish benchmark performance.

---

### 4. Missing Value Handling

Missing values represented by impossible zero values were converted to `NaN`.

Affected variables:

- Glucose
- BloodPressure
- SkinThickness
- Insulin
- BMI

Missing values were imputed using the **median**.

---

### 5. Outlier Detection

Outliers were detected using the **IQR method**.

Instead of removing observations, extreme values were capped using calculated lower and upper thresholds.

---

### 6. Feature Engineering

Several new features were created using medical domain knowledge.

Examples include:

- Age categories
- BMI categories
- Glucose categories
- Age × BMI interaction
- Age × Glucose interaction
- Insulin score
- Glucose × Insulin interaction
- Glucose × Pregnancies interaction

---

### 7. Encoding

Categorical variables were converted into numerical representations.

- Label Encoding
- One-Hot Encoding

---

### 8. Feature Scaling

Continuous numerical variables were standardized using **StandardScaler**.

---

### 9. Final Model

A new Random Forest model was trained using the engineered dataset.

Performance metrics were compared against the baseline model.

---

## 📊 Results

### Baseline Model

| Metric | Score |
|---------|------:|
| Accuracy | 0.77 |
| Recall | 0.71 |
| Precision | 0.74 |
| F1 Score | 0.72 |

### Final Model

| Metric | Score |
|---------|------:|
| Accuracy | **0.79** |
| Recall | **0.654** |
| Precision | **0.72** |
| F1 Score | **0.68** |
| ROC-AUC | **0.76** |

Although recall and F1-score slightly decreased, feature engineering introduced meaningful interaction variables and improved the model's overall predictive structure.

---

## ⭐ Key Findings

The most influential engineered features included:

- NEW_GLUCOSE_X_INSULIN
- NEW_GLUCOSE_X_PREGNANCIES
- NEW_GLUCOSE
- NEW_AGE_BMI
- NEW_AGE_GLUCOSE

The interaction features created during feature engineering became some of the strongest predictors in the final Random Forest model.

---

## 📚 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn

---

## 📖 Key Concepts Practiced

- Exploratory Data Analysis (EDA)
- Missing Value Imputation
- Outlier Handling
- Feature Engineering
- Feature Interaction
- Label Encoding
- One-Hot Encoding
- Feature Scaling
- Random Forest Classification
- Feature Importance Analysis

---

## 🚀 Lessons Learned

This project reinforced that feature engineering is not simply about creating more variables, but about creating **more informative variables**.

Thoughtful preprocessing and domain-driven feature engineering can significantly influence how a machine learning model learns patterns from the data.

---


Miuul Data Science Bootcamp – Week 6  
Feature Engineering Project
