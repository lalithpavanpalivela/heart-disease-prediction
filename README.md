# Heart Disease Prediction Web Application

This project is a Django-based web application designed to predict the likelihood of heart disease (low, moderate, or high) based on user input. It uses a Random Forest Classifier trained on a large dataset of medical records, achieving high accuracy. The system provides a user-friendly interface to input relevant medical information and view prediction results.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies](#technologies)
- [Setup](#setup)
- [Model Download](#model-download)
- [Usage](#usage)
- [Model Training](#model-training)
- [License](#license)

## Overview

This web application predicts the likelihood of heart disease based on key medical factors such as age, blood pressure, cholesterol, and more. Users can enter their health details, and the application will provide a prediction about their heart disease risk using a trained Random Forest machine learning model.

## Features

- User-friendly Interface: Simple form-based input for medical data such as:
  - Age
  - Chest pain type
  - Resting blood pressure
  - Cholesterol levels
  - Maximum heart rate
- Predictions: Displays heart disease risk as Low, Moderate, or High.
- Detailed Information: Includes modals (pop-ups) explaining the significance of each input parameter with helpful links.

## Technologies

- Django: For the web backend.
- Python: Core programming language for both development and machine learning.
- Scikit-learn: Used for building the Random Forest model.
- HTML/CSS/Bootstrap: For the frontend user interface.

## Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/lalithpavanpalivela/heart-disease-prediction.git
   cd heart-disease-prediction
   ```

2. Install dependencies:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. Migrate the database:
   ```bash
   python manage.py migrate
   ```

4. Download the trained model:
   - The Random Forest model (`.pkl` file) can be downloaded from [this link](https://drive.google.com/file/d/15k7dCU0j_lTJwftIiqtz2YYWAhdiR27x/view?usp=drive_link).
   - Place the `.pkl` file in the `models/` directory.

5. Run the application:
   ```bash
   python manage.py runserver
   ```

   Visit `http://127.0.0.1:8000/` in your browser.

## Model Download

Due to file size limitations, the trained model is available for download from [Google Drive](https://drive.google.com/file/d/15k7dCU0j_lTJwftIiqtz2YYWAhdiR27x/view?usp=drive_link).

---

## Usage

1. Visit the application and fill in your medical details.
2. Click "Predict" to receive a prediction on your heart disease risk.
3. The prediction will show as Low, Moderate, or High risk.

## Model Training

The model is a Random Forest Classifier trained using medical records. Key hyperparameters were tuned to optimize performance, achieving higher accuracy of on the validation set. The model was trained using features such as age, sex, blood pressure, cholesterol, and other health indicators.

---

## License

This project is licensed under the MIT License.
