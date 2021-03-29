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
