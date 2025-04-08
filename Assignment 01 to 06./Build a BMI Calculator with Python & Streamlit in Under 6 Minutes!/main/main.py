import streamlit as st
import base64

# ----- PAGE CONFIG -----
st.set_page_config(page_title="BMI Calculator", page_icon="💪", layout="centered")


# ----- BACKGROUND IMAGE -----
def set_bg_from_url(url):
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("{url}");
             background-size: cover;
             background-attachment: fixed;
             background-repeat: no-repeat;
             background-position: center;
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

set_bg_from_url("https://images.unsplash.com/photo-1599058917212-d750089bc55b?auto=format&fit=crop&w=1350&q=80")


# ----- CUSTOM CSS -----
st.markdown("""
    <style>
        .main {
            background-color: #f0f2f6;
        }
        .stButton>button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 0.6em 1em;
            font-size: 16px;
        }
        .stNumberInput>div>div>input {
            background-color: #ffffff;
            color: #000000;
        }
        .bmi-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 2px 2px 12px rgba(0,0,0,0.1);
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# ----- TITLE -----
st.markdown("<h1 style='text-align: center;'>💪 BMI Calculator</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Calculate your Body Mass Index to understand your health status.</p>", unsafe_allow_html=True)

# ----- INPUT FIELDS -----
height = st.number_input("📏 Enter your height (in cm):", min_value=50.0, max_value=300.0, value=170.0)
weight = st.number_input("⚖️ Enter your weight (in kg):", min_value=10.0, max_value=300.0, value=70.0)

# ----- CALCULATE BMI -----
if st.button("Calculate BMI"):
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    st.markdown("<div class='bmi-box'>", unsafe_allow_html=True)
    st.markdown(f"<h3>Your BMI is: <span style='color:#4CAF50'>{bmi:.2f}</span></h3>", unsafe_allow_html=True)

    # ----- INTERPRETATION -----
    if bmi < 18.5:
        st.info("📉 You are underweight.")
    elif 18.5 <= bmi < 25:
        st.success("✅ You have a normal weight.")
    elif 25 <= bmi < 30:
        st.warning("⚠️ You are overweight.")
    else:
        st.error("❌ You are obese.")
    st.markdown("</div>", unsafe_allow_html=True)

# ----- BMI CATEGORIES -----
with st.expander("📊 BMI Category Chart"):
    st.markdown("""
    | BMI Range       | Category         |
    |------------------|------------------|
    | Less than 18.5   | Underweight       |
    | 18.5 – 24.9      | Normal weight     |
    | 25.0 – 29.9      | Overweight        |
    | 30.0 and above   | Obese             |
    """, unsafe_allow_html=True)

# ----- FOOTER -----
st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Built by Saba Muhammad Riaz❤️ using Streamlit</p>", unsafe_allow_html=True)

