# Importing all required libraries
import uvicorn
from fastapi import FastAPI
import pandas as pd
from DataFile import Data
import pickle

# Creating the app object
app = FastAPI()
pickle_in = open("model.pkl",'rb')
model = pickle.load(pickle_in)

# Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello, World'}

# 4. Route with a single parameter, returns the parameter within a message
#    Located at: http://127.0.0.1:8000/AnyNameHere
@app.get('/{name}')
def get_name(name: str):
    return {'Welcome To Defaults prediction': f'{name}'}

# 3. Expose the prediction functionality, make a prediction from the passed
#    JSON data and return the predicted Bank Note with the confidence
@app.post('/predict')
def predict_defaults(data:Data):
    
    # data = data.dict()
    # account_amount_added_12_24m = data['account_amount_added_12_24m']
    # account_days_in_dc_12_24m = data['account_days_in_dc_12_24m']
    # account_days_in_rem_12_24m = data['account_days_in_rem_12_24m']
    # account_days_in_term_12_24m = data['account_days_in_term_12_24m']
    # account_incoming_debt_vs_paid_0_24m = data['account_incoming_debt_vs_paid_0_24m']
    # account_status = data['account_status']
    # age = data['age']
    # avg_payment_span_0_12m = data['avg_payment_span_0_12m']
    # merchant_category = data['merchant_category']
    # merchant_group = data['merchant_group']
    # has_paid = data['has_paid']
    # max_paid_inv_0_24m = data['max_paid_inv_0_24m']
    # num_active_div_by_paid_inv_0_12m = data['num_active_div_by_paid_inv_0_12m']
    # num_active_inv = data['num_active_inv']
    # num_arch_dc_0_12m = data['num_arch_dc_0_12m']
    # num_arch_dc_12_24m = data['num_arch_dc_12_24m']
    # num_arch_ok_0_12m = data['num_arch_ok_0_12m']
    # num_arch_ok_12_24m = data['num_arch_ok_12_24m']
    # num_arch_rem_0_12m = data['num_arch_rem_0_12m']
    # num_arch_written_off_0_12m = data['num_arch_written_off_0_12m']
    # num_arch_written_off_12_24m = data['num_arch_written_off_12_24m']
    # num_unpaid_bills = data['num_unpaid_bills']
    # status_last_archived_0_24m = data['status_last_archived_0_24m']
    # status_2nd_last_archived_0_24m = data['status_2nd_last_archived_0_24m']
    # status_max_archived_0_24_months = data['status_max_archived_0_24_months']
    # recovery_debt = data['recovery_debt']
    # sum_capital_paid_account_0_12m = data['sum_capital_paid_account_0_12m']
    # sum_paid_inv_0_12m = data['sum_paid_inv_0_12m']
    # time_hours = data['time_hours']
    
    # data2 = {
    # 'account_amount_added_12_24m':account_amount_added_12_24m,
    # 'account_days_in_dc_12_24m':account_days_in_dc_12_24m,
    # 'account_days_in_rem_12_24m':account_days_in_rem_12_24m,
    # 'account_days_in_term_12_24m':account_days_in_term_12_24m,
    # 'account_incoming_debt_vs_paid_0_24m':account_incoming_debt_vs_paid_0_24m,
    # 'account_status':account_status,
    # 'age':age,
    # 'avg_payment_span_0_12m':avg_payment_span_0_12m,
    # 'merchant_category':merchant_category,
    # 'merchant_group':merchant_group,
    # 'has_paid':has_paid,
    # 'max_paid_inv_0_24m':max_paid_inv_0_24m,
    # 'num_active_div_by_paid_inv_0_12m':num_active_div_by_paid_inv_0_12m,
    # 'num_active_inv':num_active_inv,
    # 'num_arch_dc_0_12m':num_arch_dc_0_12m,
    # 'num_arch_dc_12_24m':num_arch_dc_12_24m,
    # 'num_arch_ok_0_12m':num_arch_ok_0_12m,
    # 'num_arch_ok_12_24m':num_arch_ok_12_24m,
    # 'num_arch_rem_0_12m':num_arch_rem_0_12m,
    # 'num_arch_written_off_0_12m':num_arch_written_off_0_12m,
    # 'num_arch_written_off_12_24m':num_arch_written_off_12_24m,
    # 'num_unpaid_bills':num_unpaid_bills,
    # 'status_last_archived_0_24m':status_last_archived_0_24m,
    # 'status_2nd_last_archived_0_24m':status_2nd_last_archived_0_24m,
    # 'status_max_archived_0_24_months':status_max_archived_0_24_months,
    # 'recovery_debt':recovery_debt,
    # 'sum_capital_paid_account_0_12m':sum_capital_paid_account_0_12m,
    # 'sum_paid_inv_0_12m':sum_paid_inv_0_12m,
    # 'time_hours':time_hours
    # }
    
    print(data)
    df = pd.DataFrame(data, index=[0])
    
    print(df.shape)
    prediction = model.predict_proba(df)
    # output = round(prediction[0], 8)
    # print(prediction[:,1])
    
    
    # prediction = model.predict([[account_amount_added_12_24m, account_days_in_dc_12_24m, account_days_in_rem_12_24m,
    #                              account_days_in_term_12_24m, account_incoming_debt_vs_paid_0_24m, account_status, 
    #                              age, avg_payment_span_0_12m, merchant_category, merchant_group, has_paid, max_paid_inv_0_24m,
    #                              num_active_div_by_paid_inv_0_12m, num_active_inv, num_arch_dc_0_12m, num_arch_dc_12_24m, 
    #                             num_arch_ok_0_12m, num_arch_ok_12_24m, num_arch_rem_0_12m, num_arch_written_off_0_12m,
    #                              num_arch_written_off_12_24m, num_unpaid_bills, status_last_archived_0_24m, status_2nd_last_archived_0_24m,
    #                              status_max_archived_0_24_months, recovery_debt, sum_capital_paid_account_0_12m, sum_paid_inv_0_12m, time_hours,]])
    
    if(prediction[:,1][0]>0.5):
        prediction="This user is a potential defauter"
    else:
        prediction="This user is NOT a potential defaulter"
    return {
        'prediction': prediction
    }

# 5. Run the API with uvicorn
#    Will run on http://127.0.0.1:8000
if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8000)
    
#uvicorn app:app --reload