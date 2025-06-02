from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np
import pandas as pd
from pydantic import BaseModel
from pathlib import Path

app = FastAPI(title="Diabetes Prediction App")

# Mount static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="templates")

# Load your model
model_path = Path("lin.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

class DiabetesInput(BaseModel):
    Pregnancies: int
    Glucose: float
    BloodPressure: float
    SkinThickness: float
    Insulin: float
    BMI: float
    DiabetesPedigreeFunction: float
    Age: int

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    Pregnancies: int = Form(...),
    Glucose: float = Form(...),
    BloodPressure: float = Form(...),
    SkinThickness: float = Form(...),
    Insulin: float = Form(...),
    BMI: float = Form(...),
    DiabetesPedigreeFunction: float = Form(...),
    Age: int = Form(...)
):
    # Prepare input data
    input_data = np.array([
        Pregnancies, Glucose, BloodPressure, SkinThickness, 
        Insulin, BMI, DiabetesPedigreeFunction, Age
    ]).reshape(1, -1)
    
    # Make prediction
    prediction = model.predict(input_data)
    
    try:
        # Try to get probabilities if available
        probability = model.predict_proba(input_data)[0][1] * 100
    except AttributeError:
        # If predict_proba not available, use decision function or default to 0 or 100
        try:
            decision = model.decision_function(input_data)[0]
            probability = (1 / (1 + np.exp(-decision))) * 100  # Sigmoid to convert to probability
        except AttributeError:
            probability = 100.0 if prediction[0] == 1 else 0.0
    
    # Determine result
    result = "Positive" if prediction[0] == 1 else "Negative"
    result_class = "danger" if prediction[0] == 1 else "success"
    
    # Create interpretation
    if probability < 30:
        interpretation = "Low risk of diabetes"
    elif 30 <= probability < 70:
        interpretation = "Moderate risk of diabetes"
    else:
        interpretation = "High risk of diabetes"
    
    return templates.TemplateResponse("result.html", {
        "request": request,
        "result": result,
        "probability": f"{probability:.2f}",
        "interpretation": interpretation,
        "result_class": result_class,
        "input_data": {
            "Pregnancies": Pregnancies,
            "Glucose": Glucose,
            "BloodPressure": BloodPressure,
            "SkinThickness": SkinThickness,
            "Insulin": Insulin,
            "BMI": BMI,
            "DPF": DiabetesPedigreeFunction,
            "Age": Age
        }
    })

@app.get("/about", response_class=HTMLResponse)
async def about(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})