import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    #int_features = [float(x) for x in request.form.values()]
    #final_features = [np.array(int_features)]
    
    ProductDivision = [float(request.form.get("ProductDivision"))]
    ProductDepartment = [float(request.form.get("ProductDepartment"))]
    ProductGroup = [float(request.form.get("ProductGroup"))]
    ProductCategory = [float(request.form.get("ProductCategory"))]
    ProductOriginalUnitPriceGBP = [float(request.form.get("ProductOriginalUnitPriceGBP"))]
    ProductMaxDaysToSellInFullPrice = [float(request.form.get("ProductMaxDaysToSellInFullPrice"))]
    Season = [float(request.form.get("Season"))]
    FullPriceUnits = [float(request.form.get("FullPriceUnits"))]
    ProductSize = [request.form.get("ProductSize")]
    
    data = {
        'ProductSize':ProductSize,
        'ProductDivision':ProductDivision,
        'ProductDepartment':ProductDepartment,
        'ProductGroup':ProductGroup,
        'ProductCategory':ProductCategory,
        'ProductOriginalUnitPriceGBP':ProductOriginalUnitPriceGBP,
        'ProductMaxDaysToSellInFullPrice':ProductMaxDaysToSellInFullPrice,
        'Season':Season,
        'FullPriceUnits':FullPriceUnits
        }
    df = pd.DataFrame(data)

    prediction = model.predict(df)
    
    output = round(prediction[0], 8)

    return render_template('index.html', prediction_text='Sales Rate should be {}'.format(output))

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)