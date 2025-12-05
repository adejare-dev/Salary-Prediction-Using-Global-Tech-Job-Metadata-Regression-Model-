Here’s a **complete, polished, and ready-to-use README.md** for your project, integrating the dataset download, code structure, setup instructions, and all useful assists. You can drop this directly into your repo.

---

# **Predicting Tech Salaries in USD Using Job Metadata (Regression Model)**

This project predicts a worker’s salary (in USD) using job-related information such as job title, experience level, company size, location, and remote ratio. It’s a practical regression project that applies Scikit-Learn to real-world data and explores which job attributes most influence compensation.

---

## **Overview**

The dataset contains over 150,000 tech job records from around the world. The goal is to build a regression model that can estimate salary levels based on job metadata.

This project covers:

* Loading and cleaning the dataset
* Handling categorical features
* Exploratory data analysis (EDA)
* Training regression models (Random Forest Regressor)
* Evaluating performance metrics (R², RMSE, MAE)
* Visualizing feature importance
* Providing insights into which features drive salary

---

## **Dataset**

**Data Science Job Salaries**

* Place the dataset in the `data/` folder as `ds_salaries.csv`
* Download automatically using the included `download_dataset.py` script

**Key columns:**

* `experience_level`
* `employment_type`
* `job_title`
* `salary_in_usd` (target variable)
* `remote_ratio`
* `company_location`
* `company_size`

---

## **Project Goal**

Build a regression model to predict **salary_in_usd** from job metadata and explore the relative importance of each feature.

---

## **Tech Stack**

* Python
* Pandas, NumPy
* Scikit-Learn (RandomForestRegressor)
* Matplotlib / Seaborn
* Jupyter Notebook



## Main Workflow

1. Load the dataset
2. Handle missing or inconsistent data
3. Encode categorical features (LabelEncoder / One-Hot Encoding)
4. Split into training and test sets
5. Train a **Random Forest Regressor**
6. Evaluate using **R², RMSE, and MAE**
7. Visualize feature importance to understand which job attributes influence salary most



## **Learning Goals

* Work with structured categorical and numeric data
* Learn regression modeling using Scikit-Learn
* Understand feature importance in predicting salary
* Develop practical skills in data cleaning, encoding, and evaluation



## **Setup & Installation**

1. **Clone the repository**:

```bash
git clone https://github.com/your-username/salary-regression-project.git
cd salary-regression-project
```

2. **Install dependencies**:

```bash
pip install -r requirements.txt
```

3. **Download the dataset**:

```bash
python download_dataset.py
```

This will create a `data/` folder and save `ds_salaries.csv` inside it.

4. **Run the notebook**:

```bash
jupyter notebook notebooks/salary_regression.ipynb
```

Or run the scripts:

```bash
python src/model.py
```

---

## **Results**

The Random Forest model provides a strong baseline for predicting tech salaries. Key insights include:

* Experience level, job title, and company size are among the most important predictors
* Remote ratio and company location also influence compensation
* The model can be extended with hyperparameter tuning, one-hot encoding, or gradient boosting for better performance

---

## **Future Enhancements**

* Hyperparameter optimization (GridSearchCV / RandomizedSearchCV)
* Use XGBoost or LightGBM for improved accuracy
* Implement cross-validation for more robust metrics
* Deploy as a small Streamlit app to predict salary from user inputs

---

## **Requirements (requirements.txt)**

```
numpy
pandas
scikit-learn   # includes RandomForestRegressor
matplotlib
seaborn
jupyter
kaggle         # required for download_dataset.py
```

---

## **Why This Project Is Useful**

* Provides real-world experience predicting salaries using structured data
* Demonstrates handling categorical variables in machine learning pipelines
* Offers insights into the key factors driving compensation in the tech industry
* Great for building a portfolio project with tangible business value

---

If you want, I can also create the **full starter repo** with:

* `preprocess.py`
* `model.py`
* `utils.py`
* `salary_regression.ipynb`

…so you can push it straight to GitHub and run it immediately.

Do you want me to do that next?
