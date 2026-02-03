# 🎓 Dropout Risk Prediction System

An AI-powered web application that helps education NGOs identify schools at high risk of student dropouts using attendance data.

---

## 📌 Problem Statement

Education NGOs collect large amounts of attendance data, but often lack intelligent tools to analyze it effectively.  
Without data-driven insights, it becomes difficult to:

- Identify schools with high dropout risk  
- Prioritize interventions  
- Measure the impact of educational programs  

This project addresses that gap by transforming raw attendance data into actionable dropout risk predictions.

---

## 💡 Solution Overview

We built a machine learning–based system that:

1. Accepts school attendance data as input  
2. Calculates attendance percentages  
3. Identifies dropout risk using a supervised ML model  
4. Displays high-risk schools through an interactive web interface  

The system enables NGOs to **focus resources where they are needed most**.

---

## 🧠 Approach

**Data Pipeline:**
Attendance Data → Cleaning → Feature Engineering → ML Model → Risk Prediction → Visualization


**Key Steps:**
- Calculate attendance percentage using Present / Enrolled
- Aggregate data at the school level
- Label dropout risk based on attendance thresholds
- Train a Logistic Regression model
- Generate dropout risk probabilities

---

## 🤖 Machine Learning Model

- **Model Used:** Logistic Regression  
- **Problem Type:** Binary Classification  
- **Target Variable:** Dropout Risk (High / Low)  

**Why Logistic Regression?**
- Simple and interpretable  
- Works well with numerical features like attendance  
- Suitable for NGOs with limited technical infrastructure  

---

## 🌐 Web Application

The project is implemented as a **Streamlit web app** that allows users to:

- Upload attendance CSV files
- View attendance statistics per school
- Identify high-risk schools
- View dropout risk probabilities

---

## 🛠️ Tech Stack

- **Programming Language:** Python  
- **Data Processing:** Pandas, NumPy  
- **Machine Learning:** Scikit-learn  
- **Web Framework:** Streamlit  
- **Environment:** VS Code / Jupyter Notebook  

---

## 📂 Dataset

The system works with school-level attendance data containing:
- School DBN
- Enrolled students
- Present students
- Absent students

Attendance percentage is derived from existing data.

> Note: Student-level data was unavailable due to privacy constraints.  
> The model currently predicts **school-level dropout risk**, and can be extended to student-level prediction when individual data is available.

---

## ▶️ How to Run the Project

### 1. Install dependencies
1.pip install streamlit pandas scikit-learn

2. Run the application
streamlit run app.py

3. Upload attendance CSV
Use the file uploader in the browser to view predictions.


📊 Output
->Attendance percentage per school
->Dropout risk probability
->List of high-risk schools for intervention

🚀 Future Enhancements

->Student-level dropout prediction
->Time-series attendance analysis
->Interactive dashboards and charts
->Automated impact measurement reports
->Deployment on cloud platforms

👥 Team

Niya Ann Joseph
Arushi Punhani
