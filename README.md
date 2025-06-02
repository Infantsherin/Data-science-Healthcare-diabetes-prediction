# Data-science-Healthcare-diabetes-prediction-
🩺 Diabetes Prediction using SVM | Data Science in Healthcare

🚀 Project Overview
This project aims to predict the likelihood of diabetes in patients using Support Vector Machine (SVM), a robust machine learning classification algorithm. It combines data science practices with a simple, intuitive web interface built with HTML and CSS, enabling users to input health parameters and receive predictions.

📂 Project Structure
bash
Copy
Edit
├── data/
│   └── diabetes.csv
├── model/
│   └── svm_model.pkl
├── app/
│   ├── index.html
│   ├── style.css
│   └── app.py
├── README.md
└── requirements.txt
🔍 Features
📊 Data preprocessing & cleaning

⚙️ Training with Support Vector Machine (SVM)

🧪 Model evaluation (accuracy, confusion matrix)

🖥️ Web interface for user input and result display

📁 Modular code structure

💾 Dataset
Source: Pima Indians Diabetes Dataset

Attributes: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age, Outcome

📈 Machine Learning Workflow
Data Cleaning

Removed zeroes from biologically impossible values (e.g., 0 insulin)

Normalized using StandardScaler

Model Training

Algorithm: sklearn.svm.SVC

Kernel: 'rbf'

Cross-validation for performance tuning

Model Evaluation

Metrics: Accuracy, Precision, Recall, F1-Score

Confusion Matrix visualization

🌐 Web Interface
HTML/CSS Frontend form for user data entry

Flask Backend (Python) for model loading and prediction

Displays prediction results in real-time

🧪 Sample Input (Frontend Form)
html
Copy
Edit
<form action="/predict" method="post">
  <input type="number" name="glucose" placeholder="Glucose Level" required />
  <input type="number" name="bmi" placeholder="BMI" required />
  <input type="number" name="age" placeholder="Age" required />
  <!-- More fields -->
  <button type="submit">Predict</button>
</form>
✅ Result Example
Based on the provided health metrics, the model predicts the patient is at risk of diabetes.
(Accuracy: ~78% on test data)

🛠️ Technologies Used
Tech	Usage
Python	Backend & ML logic
scikit-learn	SVM & preprocessing
pandas, numpy	Data wrangling
Flask	Web server
HTML/CSS	User Interface

🚀 How to Run Locally
bash
Copy
Edit
# Clone the repo
git clone https://github.com/yourusername/diabetes-prediction-svm.git
cd diabetes-prediction-svm

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app/app.py
🧠 Future Enhancements
Use more advanced models (e.g., XGBoost, Random Forest)

Add visual analytics dashboard (Plotly/Dash)

Improve UI/UX with JavaScript interactivity

Deploy to the cloud (Heroku, AWS, etc.)

📌 License
This project is licensed under the MIT License.

🤝 Contributions
Pull requests are welcome! For major changes, please open an issue first.
