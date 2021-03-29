# DefaultersPrediction

## This project has the below major parts:

1. ML_Case_Study.ipynb: This file contains code for the Machine Learning model to predict the defaulters.
2. model.pkl: This file contains the trained model saved using pickle.
3. app.py - This file contains Fast APIs that receives the user details details as JSON format through GUI or API calls, computes the predicted probabilitites based on the model and returns it.
4. main.py - This file contains Fast APIs for initial testing.
5. DataFile.py - This file renders the json file and sends it to app.py.
6. ProcFile Local - This file is required to render the API when accessed locally. Add this instead - web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app.
7. ProcFile Public - This file is required to render the API when accessed on public domain. Add this - web: uvicorn app:app --host=0.0.0.0 --port=${PORT:-5000}.
8. requirements.txt - Add the required libraries will be added to this file which will be installed during deployment.
9. results.csv - Contains the results of the test dataset as requested.

## Running the project

### In local:
1. Ensure that you are in the project home directory. Make sure the serialized model.pkl file also exists in this directory.

2. Install the pickle and uvicorn using the below comand

pip install pickle uvicorn

3. Make sure the ProcFile contains the below code:

web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker app:app

5. Run the below code to load the uvicorn API:

uvicorn app:app --reload

8. By default, flask will run on port 8000, navigate to the below URL.

URL: http://localhost:8000/docs
or
URL: http://localhost:8000/redocs

### On the public domain:
1. Access the model API from the below link:

Public hosting API endpoint: https://defaulters-prediction.herokuapp.com/docs
or
https://defaulters-prediction.herokuapp.com/redocs

## Test data:
1. Use the below test data if required to test the model. The below data results a probability of 0.03 and the threshold is set at 0.5 to either identify it as defaulters or not; and this test data gives a response as non-defaulter.
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