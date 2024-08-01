# Defaulter Predictor: ML Model Deployment with FastAPI & Flask

## Project Overview

This project demonstrates a machine learning model for predicting defaulters. It includes components for model training, deployment, and API access using FastAPI and Flask. The project is structured as follows:

- **`ML_Case_Study.ipynb`**: Contains the code for training the machine learning model to predict defaulters.
- **`model.pkl`**: A serialized file containing the trained model, saved using pickle.
- **`app.py`**: FastAPI application that receives user details in JSON format, computes predicted probabilities based on the model, and returns the results.
- **`main.py`**: FastAPI application used for initial testing.
- **`DataFile.py`**: Renders the JSON file and sends it to `app.py`.
- **`Procfile_Local`**: Configuration for local deployment with Gunicorn and Uvicorn. Use the following content:
```
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app
```
- **`Procfile_Public`**: Configuration for public domain deployment. Use the following content:
```
web: uvicorn app
--host=0.0.0.0 --port=${PORT:-5000}
```
- **`requirements.txt`**: Lists required libraries to be installed during deployment.
- **`results.csv`**: Contains results of the test dataset.

## Running the Project

### Local Deployment

1. **Navigate to the Project Directory**: Ensure you are in the project home directory where the `model.pkl` file is located.

2. **Install Required Packages**:
 ```bash
 pip install pickle uvicorn
```
3. ** Configure `Procfile_local`**: Ensure the Procfile_Local contains the following:
```
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app
```
4. ** Run the FastAPI Application:**
```
uvicorn app:app --reload
```
5. **Access the API**: By default, the FastAPI server runs on port 8000. Navigate to:
- [http://localhost:8000/docs](http://localhost:8000/docs) for the interactive API documentation
- [http://localhost:8000/redocs](http://localhost:8000/redocs) for an alternative API documentation view

### Public Deployment

1. **Access the Model API**: Once deployed publicly, you can access the API at:
- [https://defaulters-prediction.herokuapp.com/docs](https://defaulters-prediction.herokuapp.com/docs)
- [https://defaulters-prediction.herokuapp.com/redocs](https://defaulters-prediction.herokuapp.com/redocs)

## Test Data

Use the following test data to evaluate the model. This data yields a probability of 0.03 with a threshold set at 0.5, indicating a non-defaulter response:
```
{
  "account_amount_added_12_24m": 50956,
  "account_days_in_dc_12_24m": 0,
  "account_days_in_rem_12_24m": 77,
  "account_days_in_term_12_24m": 0,
  "account_incoming_debt_vs_paid_0_24m": 0,
  "account_status": 1,
  "age": 28,
  "avg_payment_span_0_12m": 12.5,
  "merchant_category": "Diversified entertainment",
  "merchant_group": "Entertainment",
  "has_paid": 1,
  "max_paid_inv_0_24m": 91980,
  "num_active_div_by_paid_inv_0_12m": 0,
  "num_active_inv": 0,
  "num_arch_dc_0_12m": 0,
  "num_arch_dc_12_24m": 1,
  "num_arch_ok_0_12m": 2,
  "num_arch_ok_12_24m": 7,
  "num_arch_rem_0_12m": 0,
  "num_arch_written_off_0_12m": 0,
  "num_arch_written_off_12_24m": 0,
  "num_unpaid_bills": 0,
  "status_last_archived_0_24m": 1,
  "status_2nd_last_archived_0_24m": 1,
  "status_max_archived_0_24_months": 3,
  "recovery_debt": 0,
  "sum_capital_paid_account_0_12m": 36163,
  "sum_paid_inv_0_12m": 93760,
  "time_hours": 20.3328
}
```
