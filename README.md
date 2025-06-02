# 🩺 Diabetes Prediction using Machine Learning (SVM + FastAPI)

![Python](https://img.shields.io/badge/Python-3.9%2B-blue) ![Machine Learning](https://img.shields.io/badge/Model-SVM-green) ![Deployment](https://img.shields.io/badge/Deployed-FastAPI-orange) ![Web UI](https://img.shields.io/badge/Frontend-HTML%2FCSS-yellow)

### 📌 Overview

This project uses machine learning techniques to predict whether a person is likely to have **diabetes** based on key health indicators. The prediction model is built using **Support Vector Machine (SVM)** and is deployed through a **FastAPI backend** with a **simple HTML/CSS frontend** for user interaction.

---

### 📁 Project Structure

```bash
├── svm.ipynb                # Jupyter Notebook: Data processing & model training
├── svm.pkl                  # Trained SVM model (serialized)
├── main.py                  # FastAPI backend for model inference
├── templates/
│   └── index.html           # HTML form for user input
├── static/
│   └── style.css            # CSS styling for the web form
├── diabetes.csv             # Dataset used for model training
└── README.md                # Project documentation
```

---

### ⚙️ Technologies Used

| Component    | Tech Used                                  |
| ------------ | ------------------------------------------ |
| Language     | Python                                     |
| ML Algorithm | Support Vector Machine (SVM)               |
| ML Library   | scikit-learn                               |
| Backend      | FastAPI                                    |
| Frontend     | HTML, CSS                                  |
| Deployment   | Localhost or any cloud platform (optional) |

---

### 🧠 Model Training Summary

* Dataset: Pima Indians Diabetes Dataset
* Features: Pregnancies, Glucose, Blood Pressure, Skin Thickness, Insulin, BMI, Diabetes Pedigree Function, Age
* Labels: Binary outcome (0 = No Diabetes, 1 = Diabetes)
* Model: `SVC(kernel='rbf')` and `SVC(kernel='linear')`
* Preprocessing: Standardization using `StandardScaler`
* Evaluation:

  * Accuracy: \~77-78%
  * Metrics: Confusion matrix, classification report

---

### 🚀 How to Run This Project Locally

#### ✅ Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/diabetes-prediction-svm.git
cd diabetes-prediction-svm
```

#### ✅ Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

#### ✅ Step 3: Run FastAPI Server

```bash
uvicorn main:app --reload
```

#### ✅ Step 4: Access Web Interface

Go to: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

### 🌐 Web Interface

* Users can input health metrics via an HTML form
* FastAPI receives input, loads the SVM model (`svm.pkl`), and returns prediction
* The result is rendered dynamically on the web page

---

### 📉 Sample Prediction Flow

1. User enters input (Glucose, BMI, Age, etc.)
2. FastAPI collects form data and converts to DataFrame
3. `svm.pkl` model is loaded and used for prediction
4. Output shown as either:

   * **"You may have diabetes"**
   * **"You are unlikely to have diabetes"**

---

### 📌 Future Improvements

* Add client-side validation and JavaScript interactivity
* Use multiple models and compare performance
* Deploy using Docker, AWS, or Streamlit Cloud
* Include real-time charts and visual analytics
