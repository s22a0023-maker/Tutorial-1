import streamlit as st

# Page config
st.set_page_config(page_title="Internship Application - Yusri Razali", layout="centered")

col1, col2 = st.columns([1, 3])
with col1:
    st.image("profile.jpg", width=160)
with col2:
    st.title("YUSRI BIN RAZALI - Internship Applications")
    st.markdown("**Internship Applications**")
    st.markdown("Bachelor of Information Technology (Hons) - Artificial Intelligence Track, Universiti Malaysia Kelantan (UMK)")


st.header("Contact Information")
st.write("Email: yuyie047@gmail.com")
st.write("Phone: +60 19651 9305")
st.write("LinkedIn: https://www.linkedin.com/in/yusri-razali-b659502a8/") 

st.header("Education")
st.write("Bachelor of Information Technology with Honors - Artificial Intelligence Track, Universiti Malaysia Kelantan (UMK), Year 4") 

st.header("Work Experience")
st.write("President of Club, IT Club, 24/25")
st.write("-Responsible for leading the team towards greater excellence and proactiveness.")
st.write("-Collaborate with external clubs to manage projects and brainstorm ideas") 

st.header("Skills") 
st.write("-Artificial Intellingence (AI)/Machine Learning (ML) Developement")
st.write("-Website/Apps Developement and Designer")
st.write("-CyberSecurity Specialist/Ethical Hacking") 

st.header("Project")
st.write("Smart Macaque Detection Live Tracking Cage Monitoring Through CCTV Applications: To develop a real-time monkey detection system using the YOLOv11 object detection algorithm, optimized for deployment on video surveillance feeds in urban, agricultural, and forest-edge environments.")
