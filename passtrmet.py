import re
import streamlit as st

# Page styling
st.set_page_config(
    page_title="Password Strength Generator",
    page_icon="🔐",
    layout="centered",
)

# Custom CSS with animations, gradients, and modern styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');
        body {
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(45deg, #ff9a9e, #fad0c4);
            animation: gradientAnimation 10s infinite alternate;
            color: white;
        }
        @keyframes gradientAnimation {
            0% { background: linear-gradient(45deg, #ff9a9e, #fad0c4); }
            100% { background: linear-gradient(45deg, #a18cd1, #fbc2eb); }
        }
        .stTextInput input {
            width: 80% !important;
            padding: 10px;
            border-radius: 8px;
            border: 2px solid white;
            background: rgba(255, 255, 255, 0.2);
            color: white;
        }
        .stTextInput input::placeholder {
            color: white;
        }
        .stButton button {
            width: 60%;
            padding: 12px;
            border-radius: 8px;
            background: #4CAF50;
            color: white;
            font-size: 18px;
            transition: all 0.3s ease-in-out;
        }
        .stButton button:hover {
            background: #45a049;
            transform: scale(1.05);
            box-shadow: 0px 0px 15px rgba(72, 239, 128, 0.6);
        }
    </style>
""", unsafe_allow_html=True)

# Page title and description
st.title("🔒 Password Strength Generator")
st.write("Enter your password and check its security level. 🔎")

# Function to check password strength
def check_password_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 1
        feedback.append("✔ Password is at least 8 characters long.")
    else:
        feedback.append("❌ Password is too short! It should be at least 8 characters long.")

    if re.search(r'[A-Z]', password) and re.search(r'[a-z]', password):
        score += 1
        feedback.append("✔ Contains both uppercase and lowercase letters.")
    else:
        feedback.append("❌ Should contain both uppercase and lowercase letters.")

    if re.search(r"\d", password):
        score += 1
        feedback.append("✔ Contains at least one digit.")
    else:
        feedback.append("❌ Should contain at least one digit.")
    
    # 🔥 Fixed regex issue here!
    if re.search(r"[!@#$%^&*()]", password):
        score += 1
        feedback.append("✔ Contains at least one special character.")
    else:
        feedback.append("❌ Should contain at least one special character.")
    
    # Display password strength results
    if score >= 4:
        st.success("✅ Password is strong!")
    elif score >= 3:
        st.warning("⚠️ Password is medium strength. Consider making it stronger.")
    else:
        st.error("❌ Password is weak. Please make it stronger.")
    
    # Feedback for improvement
    with st.expander("Improve Your Password 🔍"):
        for item in feedback: 
            st.write(item)

# Password input
password = st.text_input("Enter your password", type="password", help="Password should be at least 8 characters long and contain both uppercase and lowercase letters, at least one digit, and at least one special character. 🔐")

# Check password strength button
if st.button("Check Password Strength"):
    if password:
        check_password_strength(password)
    else:
        st.warning("⚠️ Please enter a password to check its strength.")

# Footer
st.write("Made with ❤️ by [Rizwan](https://github.com/RizSheik)")
st.write("🔑 Password Strength Generator")