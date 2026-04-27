"""
Loan Approval Prediction — Streamlit App
Models: Logistic Regression | Random Forest
Dataset: loan_approval_dataset.csv
"""

import streamlit as st
import numpy as np
import pandas as pd
import joblib
import json
import os


# Page Config
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.4rem;
        font-weight: 800;
        color: #1a237e;
        text-align: center;
        margin-bottom: 0.2rem;
    }
    .sub-header {
        font-size: 1rem;
        color: #546e7a;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background: linear-gradient(135deg, #f5f7fa 0%, #c3cfe2 100%);
        padding: 1rem 1.5rem;
        border-radius: 12px;
        text-align: center;
        margin: 0.3rem;
    }
    .metric-label {
        font-size: 0.8rem;
        color: #546e7a;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.05rem;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 800;
        color: #1a237e;
    }
    .approved-box {
        background: linear-gradient(135deg, #e8f5e9, #a5d6a7);
        border: 2px solid #388e3c;
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
    }
    .rejected-box {
        background: linear-gradient(135deg, #ffebee, #ef9a9a);
        border: 2px solid #c62828;
        border-radius: 14px;
        padding: 1.5rem;
        text-align: center;
    }
    .result-title {
        font-size: 1.8rem;
        font-weight: 800;
    }
    .result-sub {
        font-size: 1rem;
        margin-top: 0.5rem;
    }
    .section-title {
        font-size: 1.1rem;
        font-weight: 700;
        color: #1a237e;
        margin-top: 1rem;
        margin-bottom: 0.5rem;
    }
    .stButton > button {
        background: linear-gradient(135deg, #1a237e, #283593);
        color: white;
        font-size: 1.1rem;
        font-weight: 700;
        padding: 0.75rem 2rem;
        border-radius: 10px;
        border: none;
        width: 100%;
        cursor: pointer;
        transition: all 0.3s;
    }
    .stButton > button:hover {
        background: linear-gradient(135deg, #283593, #3949ab);
        transform: translateY(-1px);
        box-shadow: 0 4px 15px rgba(26, 35, 126, 0.4);
    }
    div[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #e8eaf6 0%, #c5cae9 100%);
    }
</style>
""", unsafe_allow_html=True)

# Load models + artifacts
@st.cache_resource
def load_artifacts():
    base = "models"
    lr_model   = joblib.load(f"{base}/logistic_regression.pkl")
    rf_model   = joblib.load(f"{base}/random_forest.pkl")
    scaler     = joblib.load(f"{base}/scaler.pkl")
    le_edu     = joblib.load(f"{base}/le_education.pkl")
    le_se      = joblib.load(f"{base}/le_self_employed.pkl")
    le_target  = joblib.load(f"{base}/le_target.pkl")
    with open(f"{base}/model_metrics.json") as f:
        metrics = json.load(f)
    return lr_model, rf_model, scaler, le_edu, le_se, le_target, metrics

lr_model, rf_model, scaler, le_edu, le_se, le_target, stored_metrics = load_artifacts()


# Header
st.markdown('<center><h1>🏦 Loan Approval Prediction System</h1></center>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Logistic Regression &amp; Random Forest | SPPU Computer Engineering Project</p>', unsafe_allow_html=True)
st.markdown('<center><h4>Team Members : Shravan Shidruk (C-29) | Divyaraj Shinde (C-30) | Tanuja Shirole (C-31) | Vrushali Shirole (C-32)</h4></center>', unsafe_allow_html=True)
st.divider()


# Sidebar — Model Selection + Metrics
with st.sidebar:
    st.markdown("## ⚙️ Model Configuration")
    selected_model = st.selectbox(
        "Select ML Model",
        ["Logistic Regression", "Random Forest"],
        help="Choose which trained model to use for prediction"
    )

    st.divider()
    st.markdown(f"## 📊 {selected_model} — Test Set Metrics")

    m = stored_metrics[selected_model]
    metrics_data = {
        "🎯 Accuracy"  : f"{m['accuracy']:.2f}%",
        "🔍 Precision" : f"{m['precision']:.2f}%",
        "🔁 Recall"    : f"{m['recall']:.2f}%",
        "⚖️ F1 Score"  : f"{m['f1_score']:.2f}%",
        "📈 ROC-AUC"   : f"{m['roc_auc']:.2f}%",
    }
    for label, val in metrics_data.items():
        st.markdown(f"""
        <div class="metric-card">
            <div class="metric-label">{label}</div>
            <div class="metric-value">{val}</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()
    st.markdown("### 🏆 Quick Comparison")
    lr_acc = stored_metrics["Logistic Regression"]["accuracy"]
    rf_acc = stored_metrics["Random Forest"]["accuracy"]
    st.markdown(f"- **Logistic Regression**: `{lr_acc:.2f}%`")
    st.markdown(f"- **Random Forest**: `{rf_acc:.2f}%`")
    winner = "Random Forest 🌲" if rf_acc > lr_acc else "Logistic Regression 📉"
    st.success(f"**Best Model → {winner}**")

# Main Input Form
st.markdown("## 📝 Enter Applicant Details")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('<div class="section-title">👤 Personal Info</div>', unsafe_allow_html=True)
    no_of_dependents = st.slider(
        "Number of Dependents", min_value=0, max_value=5, value=2,
        help="How many people are financially dependent on the applicant"
    )
    education = st.selectbox(
        "Education Level",
        ["Graduate", "Not Graduate"],
        help="Highest level of education completed"
    )
    self_employed = st.selectbox(
        "Self Employed?",
        ["No", "Yes"],
        help="Is the applicant self-employed?"
    )

with col2:
    st.markdown('<div class="section-title">💰 Financial Details</div>', unsafe_allow_html=True)
    income_annum = st.number_input(
        "Annual Income (₹)", min_value=200000, max_value=10000000,
        value=5000000, step=100000,
        help="Total annual income of the applicant in INR"
    )
    loan_amount = st.number_input(
        "Loan Amount Requested (₹)", min_value=300000, max_value=40000000,
        value=10000000, step=500000,
        help="Total loan amount being requested"
    )
    loan_term = st.slider(
        "Loan Term (months)", min_value=2, max_value=20, value=12,
        help="Duration of the loan in months"
    )
    cibil_score = st.slider(
        "CIBIL Score", min_value=300, max_value=900, value=650,
        help="Credit score of the applicant (300–900). Higher is better."
    )

with col3:
    st.markdown('<div class="section-title">🏠 Asset Details</div>', unsafe_allow_html=True)
    residential_assets_value = st.number_input(
        "Residential Assets Value (₹)", min_value=0, max_value=30000000,
        value=5000000, step=500000,
        help="Total value of residential properties owned"
    )
    commercial_assets_value = st.number_input(
        "Commercial Assets Value (₹)", min_value=0, max_value=20000000,
        value=3000000, step=500000,
        help="Total value of commercial properties owned"
    )
    luxury_assets_value = st.number_input(
        "Luxury Assets Value (₹)", min_value=0, max_value=40000000,
        value=8000000, step=500000,
        help="Value of luxury assets (vehicles, jewelry, etc.)"
    )
    bank_asset_value = st.number_input(
        "Bank Asset Value (₹)", min_value=0, max_value=15000000,
        value=3000000, step=200000,
        help="Total value of assets held in bank (FDs, savings, etc.)"
    )

st.markdown("")

# Predict Button
col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
with col_btn2:
    predict_clicked = st.button("🔍 Predict Loan Approval", width="stretch")

# Prediction Logic
if predict_clicked:
    # Encode inputs using saved label encoders
    edu_encoded = le_edu.transform([education])[0]
    se_encoded  = le_se.transform([self_employed])[0]

    input_data = np.array([[
        no_of_dependents,
        edu_encoded,
        se_encoded,
        income_annum,
        loan_amount,
        loan_term,
        cibil_score,
        residential_assets_value,
        commercial_assets_value,
        luxury_assets_value,
        bank_asset_value
    ]])

    input_df = pd.DataFrame(input_data, columns=[
        'no_of_dependents', 'education', 'self_employed',
        'income_annum', 'loan_amount', 'loan_term', 'cibil_score',
        'residential_assets_value', 'commercial_assets_value',
        'luxury_assets_value', 'bank_asset_value'
    ])

    if selected_model == "Logistic Regression":
        input_scaled = scaler.transform(input_df)
        prediction  = lr_model.predict(input_scaled)[0]
        probability = lr_model.predict_proba(input_scaled)[0]
    else:
        prediction  = rf_model.predict(input_df)[0]
        probability = rf_model.predict_proba(input_df)[0]

    # Decode prediction: 0 = Approved, 1 = Rejected
    result_label = le_target.inverse_transform([prediction])[0]
    prob_approved = probability[0] * 100  # index 0 = Approved
    prob_rejected = probability[1] * 100  # index 1 = Rejected

    st.divider()
    st.markdown("## 📋 Prediction Result")

    col_res1, col_res2 = st.columns([1.5, 1])

    with col_res1:
        if result_label == "Approved":
            st.markdown(f"""
            <div class="approved-box">
                <div class="result-title" style="color:#1b5e20;">✅ LOAN APPROVED</div>
                <div class="result-sub" style="color:#2e7d32;">
                    Congratulations! Based on the provided details, the applicant is
                    <strong>eligible</strong> for the loan.
                </div>
                <div class="result-sub" style="color:#388e3c;">
                    Model Used: <strong>{selected_model}</strong> &nbsp;|&nbsp;
                    Confidence: <strong>{prob_approved:.2f}%</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="rejected-box">
                <div class="result-title" style="color:#b71c1c;">❌ LOAN REJECTED</div>
                <div class="result-sub" style="color:#c62828;">
                    Based on the provided details, the applicant is
                    <strong>not eligible</strong> for the loan at this time.
                </div>
                <div class="result-sub" style="color:#d32f2f;">
                    Model Used: <strong>{selected_model}</strong> &nbsp;|&nbsp;
                    Confidence: <strong>{prob_rejected:.2f}%</strong>
                </div>
            </div>
            """, unsafe_allow_html=True)

    with col_res2:
        st.markdown("### Prediction Confidence")
        st.metric("✅ Approved Probability", f"{prob_approved:.2f}%")
        st.metric("❌ Rejected Probability", f"{prob_rejected:.2f}%")

        # Visual probability bar
        st.markdown(f"""
        <div style='margin-top:1rem;'>
            <div style='font-size:0.85rem;color:#546e7a;font-weight:600;margin-bottom:0.4rem;'>
                Approved vs Rejected
            </div>
            <div style='background:#ef9a9a;border-radius:8px;height:24px;width:100%;'>
                <div style='background:#81c784;border-radius:8px;height:24px;
                    width:{prob_approved:.1f}%;display:flex;align-items:center;
                    justify-content:center;font-size:0.8rem;font-weight:700;color:#1b5e20;'>
                    {prob_approved:.1f}%
                </div>
            </div>
            <div style='display:flex;justify-content:space-between;
                font-size:0.75rem;color:#546e7a;margin-top:0.3rem;'>
                <span>✅ Approved</span><span>❌ Rejected</span>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # Show input summary
    st.divider()
    st.markdown("### 📌 Input Summary")
    summary_df = pd.DataFrame({
    "Feature": [
        "No. of Dependents", "Education", "Self Employed",
        "Annual Income (₹)", "Loan Amount (₹)", "Loan Term (months)",
        "CIBIL Score", "Residential Assets (₹)", "Commercial Assets (₹)",
        "Luxury Assets (₹)", "Bank Assets (₹)"
    ],
    "Value": list(map(str, [
        no_of_dependents, education, self_employed,
        f"₹{income_annum:,}", f"₹{loan_amount:,}", loan_term,
        cibil_score, f"₹{residential_assets_value:,}",
        f"₹{commercial_assets_value:,}", f"₹{luxury_assets_value:,}",
        f"₹{bank_asset_value:,}"
    ]))
    })
    st.dataframe(summary_df, width="stretch")

# Footer
st.divider()
st.markdown("""
<div style='text-align:center; color:#90a4ae; font-size:0.85rem; padding: 1rem 0;'>
    🏦 Loan Approval Predictor &nbsp;|&nbsp; 
    Built by <strong>Shravan Shidruk and Team</strong> &nbsp;|&nbsp; 
    SPPU Computer Engineering &nbsp;|&nbsp;
    Genba Sopanrao Moze College Of Engineering, Balewadi-411045 &nbsp;|&nbsp;
    DSBDA MINI PROJECT
</div>
""", unsafe_allow_html=True)
