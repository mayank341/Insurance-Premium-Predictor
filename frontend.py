import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000/predict"

st.set_page_config(
    page_title="Premium Predictor",
    page_icon="💎",
    layout="centered",
    initial_sidebar_state="collapsed",
)

# ---------- Theme State ----------
if "theme" not in st.session_state:
    st.session_state.theme = "dark"

def toggle_theme():
    st.session_state.theme = "light" if st.session_state.theme == "dark" else "dark"

is_dark = st.session_state.theme == "dark"

# ---------- Theme Variables ----------
if is_dark:
    bg_gradient = "linear-gradient(135deg, #0f0c29 0%, #302b63 50%, #24243e 100%)"
    card_bg = "rgba(30, 30, 46, 0.65)"
    card_border = "rgba(255, 255, 255, 0.08)"
    text_color = "#f1f1f5"
    sub_text = "#aaa9c0"
    input_bg = "rgba(255,255,255,0.06)"
    input_border = "rgba(255,255,255,0.12)"
    label_color = "#cfcfe8"
    shadow = "0 8px 32px rgba(0,0,0,0.5)"
    accent1 = "#7f5af0"
    accent2 = "#2cb67d"
else:
    bg_gradient = "linear-gradient(135deg, #e0f7fa 0%, #fce4ec 50%, #ede7f6 100%)"
    card_bg = "rgba(255, 255, 255, 0.75)"
    card_border = "rgba(255, 255, 255, 0.5)"
    text_color = "#2b2b3c"
    sub_text = "#6b6b80"
    input_bg = "rgba(255,255,255,0.9)"
    input_border = "rgba(0,0,0,0.08)"
    label_color = "#4a4a68"
    shadow = "0 8px 32px rgba(120,120,160,0.25)"
    accent1 = "#7f5af0"
    accent2 = "#2cb67d"

# ---------- CSS ----------
st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"] {{
    font-family: 'Poppins', sans-serif;
    color: {text_color};
}}

.stApp {{
    background: {bg_gradient};
    background-attachment: fixed;
    transition: background 0.5s ease;
}}

#MainMenu, footer, header {{visibility: hidden;}}

.main .block-container {{
    max-width: 760px;
    padding-top: 1.5rem;
}}

.brand {{
    font-size: 1.3rem;
    font-weight: 700;
    color: {text_color};
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

/* Hero */
.hero {{
    text-align: center;
    margin-bottom: 2rem;
}}

.hero h1 {{
    font-size: 2.6rem;
    font-weight: 800;
    background: linear-gradient(90deg, {accent1}, {accent2});
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 0.3rem;
}}

.hero p {{
    color: {sub_text};
    font-size: 1.05rem;
    font-weight: 400;
}}

/* Glass card */
.glass-card {{
    background: {card_bg};
    border: 1px solid {card_border};
    border-radius: 22px;
    padding: 2rem;
    box-shadow: {shadow};
    backdrop-filter: blur(16px);
    -webkit-backdrop-filter: blur(16px);
    margin-bottom: 1.5rem;
}}

.section-title {{
    font-size: 1.05rem;
    font-weight: 700;
    color: {text_color};
    margin-bottom: 1.2rem;
    display: flex;
    align-items: center;
    gap: 0.5rem;
}}

.field-label {{
    font-size: 0.85rem;
    font-weight: 600;
    color: {label_color};
    margin-bottom: 0.3rem;
    margin-top: 0.6rem;
    text-transform: uppercase;
    letter-spacing: 0.5px;
}}

/* Inputs */
.stNumberInput input, div[data-baseweb="select"] > div, .stSlider {{
    background-color: {input_bg} !important;
    border: 1.5px solid {input_border} !important;
    border-radius: 12px !important;
    color: {text_color} !important;
}}

div[data-baseweb="select"] > div:hover, .stNumberInput input:hover {{
    border-color: {accent1} !important;
    box-shadow: 0 0 0 3px {accent1}22;
}}

div[data-baseweb="select"] span, div[data-baseweb="select"] div {{
    color: {text_color} !important;
}}

.stNumberInput button {{
    background-color: {input_bg} !important;
    border-color: {input_border} !important;
    color: {text_color} !important;
}}

/* Radio / pills for smoker */
div[role="radiogroup"] {{
    gap: 0.6rem;
}}

div[role="radiogroup"] label {{
    background: {input_bg};
    border: 1.5px solid {input_border};
    border-radius: 12px;
    padding: 0.5rem 1rem !important;
    transition: all 0.2s ease;
}}

div[role="radiogroup"] label:hover {{
    border-color: {accent1};
}}

/* Predict Button */
div[data-testid="stButton"] > button:first-child {{
    width: 100%;
    background: linear-gradient(90deg, {accent1}, {accent2});
    color: white;
    font-weight: 700;
    font-size: 1.1rem;
    padding: 0.85rem 0;
    border-radius: 14px;
    border: none;
    margin-top: 0.5rem;
    box-shadow: 0 6px 20px {accent1}55;
    transition: all 0.2s ease;
}}

div[data-testid="stButton"] > button:first-child:hover {{
    transform: translateY(-3px);
    box-shadow: 0 10px 28px {accent1}77;
}}

/* Theme toggle button */
.theme-btn button {{
    border-radius: 50% !important;
    width: 42px !important;
    height: 42px !important;
    padding: 0 !important;
    font-size: 1.2rem !important;
    background: {card_bg} !important;
    border: 1px solid {card_border} !important;
    color: {text_color} !important;
    box-shadow: {shadow};
}}

/* Result cards */
.result-grid {{
    display: grid;
    grid-template-columns: 1.4fr 1fr 1fr;
    gap: 1rem;
    margin-top: 0.5rem;
}}

.result-box {{
    border-radius: 18px;
    padding: 1.3rem 1rem;
    text-align: center;
    background: {card_bg};
    border: 1px solid {card_border};
    box-shadow: {shadow};
    animation: fadeUp 0.5s ease;
}}

.result-box.primary {{
    background: linear-gradient(135deg, {accent1}, {accent2});
    color: white;
}}

.result-box .label {{
    font-size: 0.75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: 1px;
    opacity: 0.85;
    margin-bottom: 0.4rem;
}}

.result-box .value {{
    font-size: 1.6rem;
    font-weight: 800;
}}

.result-box.primary .value {{
    font-size: 2rem;
}}

@keyframes fadeUp {{
    from {{ opacity: 0; transform: translateY(15px); }}
    to {{ opacity: 1; transform: translateY(0); }}
}}

.footer-note {{
    text-align: center;
    color: {sub_text};
    font-size: 0.8rem;
    margin-top: 2.5rem;
    opacity: 0.7;
}}
</style>
""", unsafe_allow_html=True)

# ---------- Top bar with theme toggle ----------
top_col1, top_col2 = st.columns([5, 1])
with top_col1:
    st.markdown('<div class="brand">💎 PremiumIQ</div>', unsafe_allow_html=True)
with top_col2:
    st.markdown('<div class="theme-btn">', unsafe_allow_html=True)
    icon = "☀️" if is_dark else "🌙"
    st.button(icon, on_click=toggle_theme, key="theme_toggle")
    st.markdown('</div>', unsafe_allow_html=True)

# ---------- Hero ----------
st.markdown("""
<div class="hero">
    <h1>Insurance Premium Predictor</h1>
    <p>AI-powered estimate of your premium, risk score & health risk</p>
</div>
""", unsafe_allow_html=True)

# ---------- Input Card ----------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)
st.markdown('<div class="section-title">📝 Your Details</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown('<div class="field-label">👤 Age</div>', unsafe_allow_html=True)
    age = st.number_input("", min_value=18, max_value=119, value=30, label_visibility="collapsed", key="age")

    st.markdown('<div class="field-label">⚖️ BMI</div>', unsafe_allow_html=True)
    bmi = st.number_input("", min_value=10.0, max_value=60.0, value=25.0, step=0.1, label_visibility="collapsed", key="bmi")

    st.markdown('<div class="field-label">📍 Region</div>', unsafe_allow_html=True)
    region = st.selectbox("", options=["southwest", "southeast", "northwest", "northeast"], label_visibility="collapsed", key="region")

with col2:
    st.markdown('<div class="field-label">⚧ Gender</div>', unsafe_allow_html=True)
    sex = st.selectbox("", options=["male", "female"], label_visibility="collapsed", key="sex")

    st.markdown('<div class="field-label">👶 Children</div>', unsafe_allow_html=True)
    children = st.number_input("", min_value=0, max_value=20, value=2, label_visibility="collapsed", key="children")

    st.markdown('<div class="field-label">🚬 Smoker?</div>', unsafe_allow_html=True)
    smoker = st.radio("", options=["no", "yes"], horizontal=True, label_visibility="collapsed", key="smoker")

predict_clicked = st.button("🔮  Predict My Premium")

st.markdown('</div>', unsafe_allow_html=True)

# ---------- Prediction ----------
if predict_clicked:
    input_data = {
        "age": age,
        "sex": sex,
        "bmi": bmi,
        "children": children,
        "smoker": smoker,
        "region": region
    }

    with st.spinner("Analyzing your profile..."):
        try:
            response = requests.post(API_URL, json=input_data, timeout=10)

            if response.status_code == 200:
                result = response.json()
                premium = result.get("predicted_premium", "N/A")
                risk_score = result.get("risk_score", "N/A")
                health_risk = result.get("health_risk", "N/A")

                premium_fmt = f"${premium:,.2f}" if isinstance(premium, (int, float)) else premium
                risk_fmt = f"{risk_score:,.2f}" if isinstance(risk_score, (int, float)) else risk_score
                health_fmt = str(health_risk).title()

                st.markdown(f"""
                <div class="result-grid">
                    <div class="result-box primary">
                        <div class="label">Predicted Premium</div>
                        <div class="value">{premium_fmt}</div>
                    </div>
                    <div class="result-box">
                        <div class="label">Risk Score</div>
                        <div class="value">{risk_fmt}</div>
                    </div>
                    <div class="result-box">
                        <div class="label">Health Risk</div>
                        <div class="value">{health_fmt}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                st.balloons()
            else:
                st.error(f"⚠️ API Error: {response.status_code} - {response.text}")

        except requests.exceptions.ConnectionError:
            st.error("❌ Could not connect to the FastAPI server. Make sure it's running on port 8000.")
        except requests.exceptions.Timeout:
            st.error("⏳ The request timed out. Please try again.")
        except Exception as e:
            st.error(f"🚨 Unexpected error: {e}")

st.markdown('<div class="footer-note">Built with Streamlit & FastAPI · PremiumIQ © 2026</div>', unsafe_allow_html=True)