# Project Description: Credit Score Classifier

## Overview

This project aims to build a Credit Score Classifier to predict credit scores based on a credit score dataset. The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/parisrohan/credit-score-classification). We will perform Exploratory Data Analysis (EDA) and feature engineering on the dataset, selecting the last 22 columns for analysis.

## Dataset Columns

```markdown
| Column                   | Non-Null Count | Dtype    |
|--------------------------|----------------|----------|
| ID                       | 100000         | int64    |
| Customer_ID              | 100000         | int64    |
| Month                    | 100000         | int64    |
| Name                     | 100000         | object   |
| Age                      | 100000         | float64  |
| SSN                      | 100000         | float64  |
| Occupation               | 100000         | object   |
| Annual_Income            | 100000         | float64  |
| Monthly_Inhand_Salary    | 100000         | float64  |
| Num_Bank_Accounts        | 100000         | float64  |
| Num_Credit_Card          | 100000         | float64  |
| Interest_Rate            | 100000         | float64  |
| Num_of_Loan              | 100000         | float64  |
| Type_of_Loan             | 100000         | object   |
| Delay_from_due_date      | 100000         | float64  |
| Num_of_Delayed_Payment   | 100000         | float64  |
| Changed_Credit_Limit     | 100000         | float64  |
| Num_Credit_Inquiries     | 100000         | float64  |
| Credit_Mix               | 100000         | object   |
| Outstanding_Debt         | 100000         | float64  |
| Credit_Utilization_Ratio | 100000         | float64  |
| Credit_History_Age       | 100000         | float64  |
| Payment_of_Min_Amount    | 100000         | object   |
| Total_EMI_per_month      | 100000         | float64  |
| Amount_invested_monthly  | 100000         | float64  |
| Payment_Behaviour        | 100000         | object   |
| Monthly_Balance          | 100000         | float64  |
| Credit_Score             | 100000         | object   |
```

## Model Training

We will train multiple models using the credit score dataset and perform hyperparameter tuning to optimize their performance. After conducting experiments, we identified the XGBoostClassifier as the best model for this task.

## Model Serialization

Once the best model (XGBoostClassifier) is trained, we will save it in JSON format using the xgb.save() method.
Dockerizing the Flask App

To provide a user-friendly interface, we will create a Flask web application with an HTML form that allows users to interact with the Credit Score Classifier. We will then containerize the Flask app using Docker.
Continuous Integration and Deployment

We will leverage GitHub Actions to automate the deployment process:
```
   - Build the Docker image for the Flask app.
   - Push the Docker image to Docker Hub.
   - Deploy the Docker image on the Render cloud platform,                  making the Credit Score Classifier accessible for end-users.
```
## More info
check out [ipynb](https://github.com/Abhishekkaddipudi/Credit_score/blob/main/CREDIT_SCORE_CLASSIFIER.ipynb) for info on EDA

## Contribution

Except me there are no other contributors 

