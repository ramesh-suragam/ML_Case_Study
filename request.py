import requests

url = 'http://localhost:5000/predict_api'
r = requests.post(url,json={'ProductDivision':1.000000,'ProductDepartment':1.000000,'ProductGroup':19.000000,'ProductCategory':221.000000,'ProductOriginalUnitPriceGBP':1764.000000,'ProductMaxDaysToSellInFullPrice':67.000000,'Season':0.000000,'FullPriceUnits':1.000000,'ProductSize':'40.5 EU/IT'})

print(r.json())