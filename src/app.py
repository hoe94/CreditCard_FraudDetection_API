from flask import Flask, request
import numpy as np
import xgboost as xgb

app = Flask(__name__)
#with open('models/model.pkl', 'rb')as f:
#    model = pickle.load(f)
model = xgb.XGBClassifier()
model.load_model("models/xgboost.bin")


@app.route('/', methods = ['POST'])
def predict():
    data = request.get_json(force = True)
    input_features = np.array(list(data.values())).reshape(1,-1)
    prediction = model.predict(input_features, validate_features = False)
    output = prediction[0]

    if output == 0:
        return f'This is a fraud transaction'

    elif output == 1:
        return f'This is a valid transaction'

if __name__ == "__main__":
    app.run(port = 5002, debug = True)