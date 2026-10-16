# Taxi Fare & Distance Prediction

**A web app to upload taxi trip data, run it through an interactive pipeline, and predict fares from distance (and distance from fare).**

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?logo=fastapi&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?logo=react&logoColor=61DAFB)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?logo=plotly&logoColor=white)

## Features

- **Upload a CSV** of taxi trips from the browser
- **Step-by-step pipeline**, with each step's output shown in the UI:
  1. **Ingest:** load the file, preview rows and stats
  2. **Clean:** drop missing values
  3. **Aggregate:** summarize numeric columns
  4. **Plot:** interactive Plotly chart
- **Prediction:**
  - fare from trip distance (`POST /predict/fare`)
  - trip distance from fare (`POST /predict/distance`)

## Architecture

```
React frontend (axios)  ──▶  FastAPI backend
                               /upload             → save CSV
                               /step/{ingest|clean|aggregate|plot}
                               /predict/fare       → fare_model.pkl
                               /predict/distance   → distance_model.pkl
```

## Run locally

**Backend**
```bash
cd backend
pip install -r requirements.txt plotly scikit-learn joblib
uvicorn main:app --reload --port 8000
```
(On Windows you can also run `setup.bat`.)

**Frontend**
```bash
cd frontend
npm install
npm start
```

**Example request**
```bash
curl -X POST http://localhost:8000/predict/fare \
  -H "Content-Type: application/json" \
  -d '{"trip_distance": 5.2}'
```

## Author

Reda Jelfa, [LinkedIn](https://linkedin.com/in/reda-jelfa)
