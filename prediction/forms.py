# prediction/forms.py
from django import forms

class PredictionForm(forms.Form):
    age = forms.IntegerField(label='Age')
    sex = forms.ChoiceField(label='Sex', choices=[(0, 'Female'), (1, 'Male')])
    cp = forms.ChoiceField(label='Chest Pain Type', choices=[(0, 'Typical Angina'), (1, 'Atypical Angina'), (2, 'Non-Anginal Pain'), (3, 'Asymptomatic')])
    resting_bp = forms.IntegerField(label='Resting Blood Pressure')
    cholesterol = forms.IntegerField(label='Cholesterol')
    fasting_bs = forms.ChoiceField(label='Fasting Blood Sugar > 120 mg/dl', choices=[(0, 'No'), (1, 'Yes')])
    resting_ecg = forms.ChoiceField(label='Resting ECG', choices=[(0, 'Normal'), (1, 'ST-T Wave Abnormality'), (2, 'Left Ventricular Hypertrophy')])
    max_hr = forms.IntegerField(label='Maximum Heart Rate')
    exercise_angina = forms.ChoiceField(label='Exercise Angina', choices=[(0, 'No'), (1, 'Yes')])
    oldpeak = forms.FloatField(label='Oldpeak')
    st_slope = forms.ChoiceField(label='ST Slope', choices=[(0, 'Up'), (1, 'Flat'), (2, 'Down')])
