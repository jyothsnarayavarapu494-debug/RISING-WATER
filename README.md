GOOGLE DRIVE LINK : https://drive.google.com/drive/folders/1B5XSuXT-2BUqHcIJ1G8zdO1BpXhlv-E1?usp=sharing

🌊 Rising Waters – Flood Prediction System

Overview

Rising Waters is a Machine Learning-based Flood Prediction System that predicts the likelihood of flooding using historical weather and rainfall data. The application provides a simple web interface where users can enter weather parameters and receive an instant flood risk prediction.

Problem Statement

Floods are among the most destructive natural disasters, causing loss of life, damage to infrastructure, agricultural losses, and economic disruption. Accurate flood prediction helps authorities and communities take preventive measures and improve disaster preparedness.

Objectives

Predict flood risk using machine learning.
Analyze weather and rainfall parameters.
Provide a simple and user-friendly web interface.
Support early decision-making for flood preparedness.
Technologies Used

Python
Flask
Pandas
NumPy
Scikit-learn
XGBoost
Joblib
HTML
CSS
JavaScript
Dataset

This project uses:

Flood Dataset
Rainfall in India (1901–2015)
Input Parameters

Temperature
Humidity
Cloud Cover
Annual Rainfall
Jan–Feb Rainfall
Mar–May Rainfall
Jun–Sep Rainfall
Oct–Dec Rainfall
Average June Rainfall
Subdivision Code
How to Run the Project

Install the required packages:

pip install -r requirements.txt

Train the model:

python train_model.py

Run the Flask application:

python app.py

Open your browser and visit:

http://127.0.0.1:5000/

Project Structure

Rising-waters/ │── app.py │── train_model.py │── requirements.txt │── README.md │── flood dataset.xlsx │── Rain fall in India 1901 - 2015.xlsx │ ├── model/ │ ├── flood_model.pkl │ └── transform.save │ ├── templates/ │ ├── home.html │ ├── index.html │ ├── chance.html │ └── no_chance.html │ └── static/ ├── main.css └── main.js

Results

The application predicts whether a flood is likely based on the user's input and displays one of the following results:

Flood Risk Detected
No Flood Expected
Future Enhancements

Integrate live weather APIs.
Improve prediction accuracy using larger datasets.
Visualize flood-prone regions on interactive maps.
Deploy the application to a cloud platform.
Develop a mobile-friendly version.
Conclusion

Rising Waters demonstrates how Machine Learning and Flask can be combined to build an intelligent flood prediction system. The project provides quick flood risk assessment through a simple web application and highlights the practical use of AI in disaster management.
