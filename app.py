from flask import Flask, jsonify, request
import pandas as pd
import joblib

app = Flask(__name__)


@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON Request
    feat_data = request.json
    # Convert JSON request to Pandas DataFrame
    df = pd.DataFrame(feat_data)
    # Match Column Na,es
    df = df.reindex(columns=col_names)
    # Get prediction
    prediction = list(model.predict(df))
    # Return JSON version of Prediction
    return jsonify({'prediction': str(prediction)})


@app.route('/', methods=['GET'])
def test():
    return 'up and running'


if __name__ == '__main__':
    # LOADS MODEL AND FEATURE COLUMNS
    model = joblib.load("model.pkl")
    col_names = joblib.load("columns.pkl")

    app.run(debug=True)
