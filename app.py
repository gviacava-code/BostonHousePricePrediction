# Import the pickle module
import pickle
# Import the flask module and its submodules
from flask import Flask,request,app,jsonify,url_for,render_template
# Import numpy and pandas for data manipulation
import numpy as np 
import pandas as pd 

# Create a flask app object
app=Flask(__name__)
# Load the random forest regressor model from the file named RandomForestRegressor.pkl
# Use the load function to read the model object from the file in binary mode (rb)
model=pickle.load(open('RandomForestRegressor.pkl', 'rb'))
# Load the scaler object from the file named Scaler.plk
# Use the load function to read the scaler object from the file in binary mode (rb)
scaler=pickle.load(open('Scaler.pkl', 'rb'))

# Define a route for the home page of the web app
@app.route('/')
# Define a function to render the home page template
def home():
    # Return the rendered HTML template named home.html
    return render_template('home.html')

# Define a route for the prediction API of the web app
# Specify that it only accepts POST requests
@app.route('/predict_api', methods=['POST'])

# Define a function to handle the prediction requests
def predict_api():
    # Get the JSON data from the request
    data=request.json['data']
    # Print the data to the console
    print(data)
    # Convert the data to a numpy array and reshape it to have one row and -1 columns
    print(np.array(list(data.values())).reshape(1,-1))
    # Scale the data using the scaler object
    scaled_data=scaler.transform(np.array(list(data.values())).reshape(1,-1))
    # Make a prediction using the model object
    ouput=model.predict(scaled_data)
    # Print the prediction to the console
    print(ouput[0])
    # Return the prediction as a JSON response
    return jsonify(ouput[0])

# Define a route for the prediction page of the web app
# Specify that it only accepts POST requests
@app.route('/predict', methods=['POST'])
# Define a function to handle the prediction requests
def predict():
    # Get the data from the request form as a list of floats
    data = [float(x) for x in request.form.values()]
    # Scale the data using the scaler object and reshape it to have one row and -1 columns
    final_input = scaler.transform(np.array(data).reshape(1,-1))
    # Print the scaled data to the console
    print(final_input)
    # Make a prediction using the model object and get the first element of the output array
    output = model.predict(final_input)[0]
    # Return the rendered HTML template named home.html with the prediction text
    return render_template('home.html', perdiction_text='>> The house prediction price is {}'.format(output))

# Check if the script is run directly
if __name__=='__main__':
    # Run the flask app in debug mode
    app.run(debug=True, port=5001)
