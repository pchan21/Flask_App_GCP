import numpy as np
from flask import Flask, request, jsonify, render_template, url_for
import pickle
import os
#from io import TextIOWrapper

app = Flask(__name__)
#model = pickle.load(open('randomForestRegressor.pkl','rb'))


@app.route('/')
def home():
    #return 'Hello World'

    data = ['Moteur', 'Modele', 'Consommation']
    return render_template('home.html', data=data)
    #return render_template('index.html')

@app.route('/predict',methods = ['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    final_features = [np.array(int_features)]
    #prediction = model.predict(final_features)
    #print(prediction[0])
    prediction = [0.32]
    #output = round(prediction[0], 2)
    return render_template('home.html', prediction_text="AQI for Jaipur {}".format(prediction[0])) # prediction[0]

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    #prediction = model.predict([np.array(list(data.values()))])

    prediction = [0.32]

    output = prediction[0]
    return jsonify(output)



if __name__ == '__main__':
    #app.run(debug=True)
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get("PORT", 8080)))