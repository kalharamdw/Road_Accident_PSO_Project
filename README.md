# AI-Based Road Accident Hotspot Analysis and Risk Prediction for Sri Lanka

## Module Details
* **Module Name:** Nature Inspired Algorithms[cite: 1]
* **Module Code:** IT41033[cite: 1]

## Project Background & Objectives
Road accidents are a serious public safety issue in Sri Lanka[cite: 1]. This project addresses the challenge of analyzing historical road accident statistics across all 25 districts to identify accident hotspots[cite: 1], calculate risk scores, and prioritize dangerous locations using the **Particle Swarm Optimization (PSO)** algorithm[cite: 1].



## Group Members & Contributions

### 1. A.W.D Kalhari
* **Index Number:** ITBIN – 2313 -0047[cite: 1]
* **Role / Contributions:** 
  * **Data Pre-processing & Management (`data_prep.py`):** Responsible for designing and scaling the dataset structure to cover all 25 districts of Sri Lanka, incorporating attributes such as District, Police Division, Road Name, Weather, Vehicle Type, Accident Cause, Severity, Injuries, and Deaths[cite: 1].
  * Handled data cleaning, missing value imputation, and coordinate mapping across regions.

### 2. W.Elika Sevindya
* **Index Number:** ITBIN – 2313 -0119[cite: 1]
* **Role / Contributions:** 
  * **Risk Score Calculation & Analysis (`risk_calculation.py`):** Developed the mathematical risk-scoring logic based on accident severity, fatalities, and injuries.
  * Formulated weighted metrics to evaluate and rank high-risk districts and road segments for safety prioritization.

### 3. Kalhara medawela
* **Index Number:** ITBNM – 2313 -0048[cite: 1]
* **Role / Contributions:** 
  * **Nature-Inspired Algorithm Implementation (`pso_model.py`):** Implemented the **Particle Swarm Optimization (PSO)** algorithm using PySwarms to optimize and identify critical high-risk spatial coordinates (hotspots)[cite: 1].
  * Tuned hyperparameters (cognitive/social parameters and inertia weights) to maximize risk-detection efficiency.

### 4. Kalana wohara
* **Index Number:** ITBNM – 2313 -0044[cite: 1]
* **Role / Contributions:** 
  * **Streamlit Dashboard & Live Integration (`app.py`, `api_service.py`):** Developed the interactive web user interface using Streamlit, combining national maps, risk charts, and real-time live environmental API integrations.
  * Handled Git branch merging, local repository version control, and deployment preparation.

---

## System Architecture & Workflow
1. **Data Collection & Pre-processing:** Scaled multi-district records with 2026 current-year timestamps[cite: 1].
2. **Risk Scoring Engine:** Evaluates severity weights to quantify danger levels[cite: 1].
3. **Particle Swarm Optimization (PSO):** Explores spatial parameters to pinpoint core hotspots[cite: 1].
4. **Interactive Dashboard:** Visualizes results via maps and charts with live auto-refresh features[cite: 1].

---

## How to Run the Project Locally

1. **Clone or open the repository** in VS Code.
2. **Activate your virtual environment:**
   ```bash
   env\Scripts\activate



   DIRECT LINK 
   http://localhost:8508/