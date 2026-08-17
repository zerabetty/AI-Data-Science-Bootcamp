# Scoutium Talent Classification ⚽

This project focuses on predicting the potential level of football players based on scout evaluations.

The objective is to build a machine learning classification model that distinguishes **highlighted** players from **average** players using player attributes and scout ratings.

## Dataset

The project uses two datasets:

- `scoutium_attributes.csv`: Contains attribute-based evaluations given to players by scouts.
- `scoutium_potential_labels.csv`: Contains the potential labels assigned to players.

The datasets were merged using common identifiers such as player, match, evaluator, and task response IDs.

## Project Workflow

### 1. Data Preparation
- Loaded and examined both datasets.
- Merged scout attribute scores with player potential labels.
- Removed goalkeeper observations.
- Removed the `below_average` class to create a binary classification problem.

### 2. Data Transformation
- Converted the long-format scout evaluation data into a wide-format dataset using a pivot table.
- Each `attribute_id` was transformed into a separate feature.
- Encoded the target variable:
  - `average` → 0
  - `highlighted` → 1
- Standardized numerical features using `StandardScaler`.

### 3. Model Development

Several classification algorithms were evaluated using 5-fold cross-validation:

- Logistic Regression
- K-Nearest Neighbors
- Decision Tree
- Random Forest
- Support Vector Machine
- Gradient Boosting
- XGBoost
- LightGBM
- CatBoost

Models were compared using:

- Accuracy
- Precision
- Recall
- F1 Score
- ROC-AUC

## Model Results

| Model | Accuracy | Precision | Recall | F1 | ROC-AUC |
|---|---:|---:|---:|---:|---:|
| CatBoost | 0.871 | 0.893 | 0.461 | 0.585 | **0.891** |
| LightGBM | 0.871 | 0.770 | **0.586** | **0.648** | 0.883 |
| Random Forest | 0.871 | 0.860 | 0.461 | 0.584 | 0.883 |
| SVM | 0.849 | **1.000** | 0.267 | 0.415 | 0.871 |
| GBM | 0.867 | 0.760 | 0.530 | 0.610 | 0.869 |
| XGBoost | 0.860 | 0.764 | 0.550 | 0.614 | 0.866 |
| Logistic Regression | 0.845 | 0.683 | 0.482 | 0.555 | 0.834 |
| KNN | 0.838 | 0.817 | 0.265 | 0.390 | 0.773 |
| CART | 0.797 | 0.551 | 0.568 | 0.540 | 0.712 |

## Final Model

CatBoost achieved the highest ROC-AUC score with **0.891**.

However, LightGBM achieved the highest **Recall (0.586)** and **F1 Score (0.648)** while maintaining a strong ROC-AUC score of **0.883**.

Since identifying genuinely high-potential players is particularly important in this problem, **LightGBM was selected for the final analysis** due to its better balance between precision and recall.

## Feature Importance

Feature importance analysis using the final LightGBM model showed that `position_id` was the most influential predictor.

Among the scout evaluation attributes, the following were particularly important:

- `4325`
- `4338`
- `4407`
- `4328`
- `4353`
- `4344`
- `4322`

These results suggest that both the player's position and specific scout evaluation attributes play an important role in identifying highlighted players.

## Conclusion

This project demonstrates an end-to-end classification workflow including data merging, preprocessing, pivot transformation, target encoding, feature scaling, model comparison, cross-validation, and feature importance analysis.

The results show that ensemble learning algorithms, particularly **CatBoost and LightGBM**, perform strongly in predicting player potential from scout evaluations.
