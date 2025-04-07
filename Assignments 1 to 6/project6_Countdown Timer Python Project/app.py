

import time
import streamlit as st

def countdown_timer(seconds):
    placeholder = st.empty()
    while seconds:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        with placeholder.container():
            st.markdown(f"""
                <div style="display:flex; justify-content:center; align-items:center; flex-direction:column;">
                    <h1 style="font-size: 48px; color: #FF4B4B;">⏳ {timer} ⏳</h1>
                </div>
            """, unsafe_allow_html=True)
        time.sleep(1)
        seconds -= 1
    with placeholder.container():
        st.markdown("""
            <div style="display:flex; justify-content:center; align-items:center; flex-direction:column;">
                <h1 style="font-size: 48px; color: #4CAF50;">🎉 Time's up! ⏰</h1>
            </div>
        """, unsafe_allow_html=True)
    st.balloons()

st.set_page_config(page_title="Smart Countdown Timer", page_icon="⏳", layout="centered")
st.markdown("""
    <style>
        .stButton>button {
            width: 100%;
            font-size: 18px;
            border-radius: 10px;
        }
        .stNumberInput>div>input {
            font-size: 18px;
            text-align: center;
        }
    </style>
""", unsafe_allow_html=True)

st.title("⏳  Countdown Timer ⏳")
st.write("Enter the time and start the countdown!")
seconds = st.number_input("⏲️ Enter countdown time in seconds:", min_value=1, step=1)

col1, col2 = st.columns(2)
if col1.button("🚀 Start Timer"):
    countdown_timer(int(seconds))

if col2.button("🔄 Restart Timer"):
    st.rerun()


