import streamlit as st

# App title
st.title("GFR Estimator")
st.subheader("Using Creatinine (Cockcroft-Gault Formula)")

# App description
st.markdown("""
This tool estimates **Glomerular Filtration Rate (GFR)** using the **Cockcroft-Gault equation**.
While BUN is displayed for clinical context, only **serum creatinine**, **age**, **weight**, and **sex** are used in the calculation.

**Formula:**
> GFR (mL/min) = [(140 - age) × weight (kg)] / (72 × serum creatinine)  
> *Multiply by 0.85 for females.*
""")

# User inputs
age = st.number_input("Age (years)", min_value=1, max_value=120, value=40)
weight = st.number_input("Weight (kg)", min_value=10.0, max_value=200.0, value=70.0)
creatinine = st.number_input("Serum Creatinine (mg/dL)", min_value=0.1, max_value=20.0, value=1.0)
bun = st.number_input("Blood Urea Nitrogen (BUN) (mg/dL)", min_value=1.0, max_value=100.0, value=14.0)
sex = st.radio("Sex", ["Male", "Female"])

# GFR calculation
gfr = ((140 - age) * weight) / (72 * creatinine)
if sex == "Female":
    gfr *= 0.85

# Display results
st.markdown(f"### Estimated GFR: `{gfr:.2f}` mL/min")
st.markdown(f"**BUN (for reference only):** `{bun}` mg/dL")

# Interpretation (optional)
if gfr < 60:
    st.warning("GFR suggests possible kidney dysfunction. Consider nephrology consult.")
elif gfr < 90:
    st.info("GFR is mildly reduced. Monitor renal function if risk factors present.")
else:
    st.success("GFR is in normal range.")
