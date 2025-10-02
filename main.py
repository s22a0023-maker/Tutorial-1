import streamlit as st
import os 

#Profile
col1, col2 = st.columns([1, 3])

with col1:
    # Use local image (must be in same folder as app.py)
    if os.path.exists("3258247.jpg"):
        st.image("3258247.jpg", caption="Yusri Bin Razali", width=180)
    else:
        st.warning("profile.jpg not found. Please place it in the same folder as this app.")

with col2:
    st.title("YUSRI BIN RAZALI")
    st.markdown("**Internship Applications**")
    st.markdown(""" 
    - **Email:** yuyie047@gmail.com
    - **Phone:** +60 19651 9305
    - **LinkedIn:** (https://www.linkedin.com/in/yusri-razali-b659502a8/) 
    """)

#Education
st.header("🎓 Education")
st.markdown("""
**Bachelor of Information Technology with Honors (AI Track)**  
Universiti Malaysia Kelantan (UMK), Year 4
""")

#Experience
st.header("💼 Work Experience")
st.subheader("President of IT Club (2024/25)")
st.markdown("""
- Led the team towards greater excellence and proactiveness  
- Collaborated with external clubs to manage projects and brainstorm ideas
""")

#Skills
st.header("🛠 Skills")
col3, col4 = st.columns(2)

with col3:
    st.markdown("- Artificial Intelligence / Machine Learning Development")  
    st.markdown("- Website & Mobile App Development")  

with col4:
    st.markdown("- Cybersecurity / Ethical Hacking")  
    st.markdown("- UI/UX Design & Prototyping") 

#Project
st.header("Projects")
st.write("Smart Macaque Detection Live Tracking Cage Monitoring Through CCTV Applications: To develop a real-time monkey detection system using the YOLOv11 object detection algorithm, optimized for deployment on video surveillance feeds in urban, agricultural, and forest-edge environments.")
