import streamlit as st
import time

# Add some CSS 
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(to bottom right, #ff99cc, #cc66ff);
    }
    .css-1d391kg {
        font-size: 35px;
        color: #ff6347;
    }
    .css-1yqzajg {
        color: blue;
    }
</style>
""", unsafe_allow_html=True)

# Function to handle the countdown timer
def countdown_timer(seconds):
    while seconds > 0:
        # Format the time into minutes and seconds
        minutes, sec = divmod(seconds, 60)
        time_str = f"{minutes:02d}:{sec:02d}"
        
        # Display the countdown with colorful text and a blinking effect
        st.markdown(f"<h2 style='color: #ff6347; font-size: 60px; font-family: 'Courier New', Courier, monospace;'>⏳ Time left: {time_str} ⏳</h2>", unsafe_allow_html=True)
        time.sleep(1)  # Wait for one second
        seconds -= 1

    # Display when the timer reaches 0 with a fun notification
    st.markdown("<h2 style='color: #32cd32; font-size: 70px;'>🎉 Time's up! 🎉</h2>", unsafe_allow_html=True)
    st.balloons()  # Adds a balloon effect when time is up

# Streamlit user interface
st.title("⏳ Countdown Timer ⏳", anchor="top")

# A fun message to engage the user
st.markdown("<h3 style='color: #8A2BE2;'>Welcome to the fun Countdown Timer! Let's see how long you can wait! ⏳</h3>", unsafe_allow_html=True)

# User input for the countdown time (in seconds)
countdown_time = st.number_input("Enter time in seconds:", min_value=1, step=1, value=10)

# Add a fun button with an emoji to start the timer
start_button = st.button("🎬 Start Timer")

# If the button is pressed, start the countdown
if start_button:
    # Show a visual countdown animation message
    st.markdown("<h3 style='color: #ff6347;'>Let the countdown begin! 🎉</h3>", unsafe_allow_html=True)
    
    countdown_timer(countdown_time)

# Additional section for the user to try again
if start_button and countdown_time > 0:
    st.markdown("<br><h4 style='color: #ff1493;'>Want to try again? Press the button below to restart the countdown! 🚀</h4>", unsafe_allow_html=True)
    restart_button = st.button("🔄 Restart Timer")
    if restart_button:
        st.experimental_rerun()  # Restart the app to allow a fresh countdown







