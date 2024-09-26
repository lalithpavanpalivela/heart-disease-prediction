# prediction/views.py
from django.shortcuts import render
import joblib
import numpy as np

# Load the saved model
model = joblib.load('best_random_forest_model.pkl')

def home(request):
    return render(request, 'home.html')

def predict(request):
    if request.method == 'POST':
        # Extract the form data
        age = int(request.POST['age'])
        sex = int(request.POST['sex'])
        cp = int(request.POST['cp'])
        restingbp = int(request.POST['restingbp'])
        cholesterol = int(request.POST['cholesterol'])
        fastingbs = int(request.POST['fastingbs'])
        restingecg = int(request.POST['restingecg'])
        maxhr = int(request.POST['maxhr'])
        exerciseangina = int(request.POST['exerciseangina'])
        oldpeak = float(request.POST['oldpeak'])
        st_slope = int(request.POST['st_slope'])

        # Create the input array for prediction
        input_features = np.array([[age, sex, cp, restingbp, cholesterol, fastingbs, restingecg, maxhr, exerciseangina, oldpeak, st_slope]])

        # Make the prediction using the loaded model
        prediction = model.predict(input_features)

        # Interpret the result (this may vary based on your model output)
        result = 'High Risk' if prediction == 1 else 'Low/Moderate Risk'

        # Render the result page with the prediction result
        return render(request, 'result.html', {'result': result})
