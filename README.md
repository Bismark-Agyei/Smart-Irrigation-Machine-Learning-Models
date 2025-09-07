# Smart-Irrigation-Machine-Learning-Models
This project applies Machine Learning models to predict whether irrigation is needed based on real-time farm data such as temperature, soil moisture, and rainfall. The goal is to assist smart farming systems in making data-driven decisions for efficient water usage.

Multiple ML models were implemented and compared, including:

Decision Tree
Random Forest
Logistic Regression
Support Vector Machine (SVM)
 XGBoost

The models output a binary decision:
1 → Irrigation Needed
0 → No Irrigation Needed   
Disclaimer:All models were trained and tested to evaluate performance in terms of accuracy, latency, and speed. However, only the Decision Tree and Random Forest models were structured to output direct irrigation recommendations (Irrigation Needed / No Irrigation Needed). The remaining models were included primarily for benchmarking and comparative analysis during experimentation.

Machine_Learning/
│── data/
│   ├── YieldResults.csv
│   ├── synthetic_soil_data.csv
│   └── synthetic_soil_data_10000.csv
│
│── models/
│   ├── irrigation_model.pkl
│   └── best_random_forest_model.pkl
│
│── notebooks/
│   ├── DecisionTree.ipynb
│   ├── RandomForest.ipynb
│   ├── LogicRegression.ipynb
│   ├── Xgboost.ipynb
│   └── The_randomforest_classifier.ipynb
│
│── scripts/
│   ├── decision_tree.py
│   ├── regression.py
│   ├── svm.py
│   └── xgboost_model.py
│
│── app.py               # Main entry point for running predictions
│── requirements.txt     # Dependencies
│── README.md            # Project documentation

# Clone this repository
git clone https://github.com/Bismark-Agyei/Smart-Irrigation-Machine-Learning-Models.git

cd Smart-Irrigation-Machine-Learning-Models


Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate   # On Linux/macOS 
venv\Scripts\activate  

pip install -r requirements.txt

p{
  "temperature": 33,
  "soil_moisture": 25,
  "rainfall": 0.0
}

{
  "prediction": 1   // Irrigation Needed
}


Developed by Duah Bismark
 Contact: duahbismarka@gmail.com



