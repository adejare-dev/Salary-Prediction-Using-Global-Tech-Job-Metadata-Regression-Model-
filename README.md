# Salary Prediction Using Global Tech Job Metadata (Regression Model)

This project focuses on predicting a worker’s salary (in USD) using job-related information such as job title, experience level, company size, location, and remote ratio. It’s a practical regression project built to test and strengthen Scikit-Learn skills using real-world job data.


## Overview

The dataset includes more than 150,000 job records from different regions and tech roles.
The goal is simple: use structured job metadata to build a regression model that can estimate salary levels.

This project walks through:

* Understanding the dataset
* Cleaning and preparing the data
* Encoding categorical features
* Training and evaluating regression models
* Visualizing insights such as feature importance

It’s a solid hands-on exercise for anyone practicing machine learning fundamentals.




## Dataset

**Data Science Job Salaries**
Source: Kaggle

Key columns include:

* `experience_level`
* `employment_type`
* `job_title`
* `salary_in_usd`
* `remote_ratio`
* `company_location`
* `company_size`

The target variable is **salary_in_usd**.



## **Project Goal**

Build a regression model that predicts a worker’s salary (in USD) using job metadata and identify which features affect compensation the most.



## Tech Stack

* Python
* Pandas, NumPy
* Scikit-Learn
* Matplotlib / Seaborn



## Main Workflow

1. **Load the dataset**
2. **Clean missing or inconsistent entries**
3. **Encode categorical features** (experience level, job title, etc.)
4. **Split data into train and test sets**
5. **Train a Random Forest Regressor**
6. **Evaluate using**:

   * R²
   * RMSE
   * MAE
7. **Plot feature importance** to see which job attributes drive salary predictions



## Learning Goals 
This project helps you understand:

* How to work with categorical job data
* How regression models behave with mixed data types
* How to evaluate model performance in a practical way
* How to read feature importance and extract insights
* How job roles and attributes influence compensation patterns


## Quick Start (Assist)

Clone the project:

```bash
git clone https://github.com/your-username/salary-regression-project
cd salary-regression-project
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the notebook:

```bash
jupyter notebook notebooks/salary_regression.ipynb
```

Or run the scripts:

```bash
python src/model.py
```



## Results

The model gives a reliable baseline for predicting tech salaries using structured features.
With improvements (such as hyperparameter tuning, one-hot encoding, or boosting models), performance can improve even further.



## Future Enhancements (Assists)

You can extend this project with:

* GridSearchCV or RandomizedSearchCV
* XGBoost or LightGBM models
* More advanced feature engineering
* A small Streamlit app that predicts salary from user inputs
* Cross-validation for more stable metrics




