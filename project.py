import streamlit as st
import pandas as pd
from sklearn.linear_model import LogisticRegression

st.title("🎓 Dropout Risk Prediction System")

uploaded_file = st.file_uploader(
    "Upload School Attendance CSV", type=["csv"]
)

if uploaded_file:
    df = pd.read_csv(uploaded_file)

    df['attendance_percentage'] = (df['Present'] / df['Enrolled']) * 100

    school_attendance = (
        df.groupby('School DBN')['attendance_percentage']
        .mean()
        .reset_index()
    )

    school_attendance['dropout_risk'] = school_attendance[
        'attendance_percentage'
    ].apply(lambda x: 1 if x < 85 else 0)

    X = school_attendance[['attendance_percentage']]
    y = school_attendance['dropout_risk']

    model = LogisticRegression()
    model.fit(X, y)

    school_attendance['risk_probability'] = model.predict_proba(X)[:, 1]

    st.subheader("📊 Dropout Risk by School")
    st.dataframe(school_attendance)

    high_risk = school_attendance[
        school_attendance['risk_probability'] > 0.5
    ]

    st.subheader("⚠️ High Risk Schools")
    st.dataframe(high_risk)
