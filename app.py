from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

# Load models
models = {
    'Logistic Regression': joblib.load('models/logistic_regression_model.pkl'),
    'Random Forest': joblib.load('models/random_forest_model.pkl'),
    'XGBoost': joblib.load('models/xgboost_model.pkl')
}

# Sample confusion matrices (you can update these dynamically if needed)
confusion_matrices = {
    'Logistic Regression': [[970, 30], [20, 80]],
    'Random Forest': [[990, 10], [5, 95]],
    'XGBoost': [[992, 8], [3, 97]]
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        input_data = {
            'User_ID': request.form['User_ID'],
            'Amount': float(request.form['Amount']),
            'Location': request.form['Location'],
            'Transaction_Type': request.form['Transaction_Type'],
            'Previous_Transaction_Minutes_Gap': int(request.form['Previous_Transaction_Time']),
            'Hour': int(request.form['Hour'])
        }

        # Convert to DataFrame
        df_input = pd.DataFrame([input_data])

        results = {}
        for model_name, model in models.items():
            y_pred = model.predict(df_input)[0]
            y_prob = model.predict_proba(df_input)[0][1]
            results[model_name] = {
                'prediction': 'Fraud V2 ' if y_pred == 1 else 'Legit',
                'probability': round(y_prob * 100, 2)
            }

        return render_template('index.html', input_data=input_data, results=results, confusion_matrices=confusion_matrices)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
