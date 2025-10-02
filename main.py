import streamlit as st

# Page config
st.set_page_config(page_title="Internship Application - Yusri Razali", layout="centered")

# Header with photo and name
col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpg", width=160)  # replace with your local profile image

with col2:
    st.title("YUSRI BIN RAZALI")
    st.markdown("**Internship Applications**")
    st.markdown("Bachelor of Information Technology (Hons) - Artificial Intelligence Track, Universiti Malaysia Kelantan (UMK)")

# Contact Information
st.header("📞 Contact Information")
st.markdown("""
- **Email:** [yuyie047@gmail.com](mailto:yuyie047@gmail.com)  
- **Phone:** +60 19651 9305  
- **LinkedIn:** [Yusri Razali](https://www.linkedin.com/in/yusri-razali-b659502a8/)  
""")

# Education
st.header("🎓 Education")
st.markdown("""
**Universiti Malaysia Kelantan (UMK)**  
_Bachelor of Information Technology with Honors - Artificial Intelligence Track_  
**Year 4**
""")

# Work Experience
st.header("💼 Work Experience")
st.markdown("""
**President, IT Club (2024/25)**  
- Led the team towards greater excellence and proactiveness  
- Collaborated with external clubs to manage projects and brainstorm ideas  
""")

# Skills
st.header("🛠 Skills")
col1, col2 = st.columns(2)

with col1:
    st.markdown("- Artificial Intelligence (AI) / Machine Learning (ML) Development")
    st.markdown("- Website / Apps Development & Design")

with col2:
    st.markdown("- Cybersecurity Specialist / Ethical Hacking")
    st.markdown("- Data Analysis & Computer Vision")

# Projects
st.header("📂 Project")
st.markdown("""
**Smart Macaque Detection & Live Tracking Cage Monitoring**  
Developed a **real-time monkey detection system** using **YOLOv11 object detection** algorithm, optimized for deployment on video surveillance feeds in **urban, agricultural, and forest-edge environments**.  
""")
