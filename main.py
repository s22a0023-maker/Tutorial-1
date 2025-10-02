import streamlit as st
import os 

#Profile
col1, col2 = st.columns([1, 3])

with col1:
    # Use local image (must be in same folder as app.py)
    if os.path.exists("profile.png"):
        st.image("profile.png", caption="YUSRI BIN RAZALI", width=180)
    else:
        st.warning("profile.jpg not found. Please place it in the same folder as this app.")

with col2:
    st.title("Internship Resume Page")
    st.markdown("**Yusri Bin Razali**")
    st.markdown("📧**Email:** yuyie047@gmail.com")
    st.markdown("📞**Phone:** +60 19651 9305")
    st.markdown("🔗**LinkedIn:** (https://www.linkedin.com/in/yusri-razali-b659502a8/)")

#Education
st.header("🎓 Education")
st.markdown("""
**Bachelor of Information Technology with Honors - AI Track,**
Universiti Malaysia Kelantan (UMK), Year 4
""")

#Experience
st.header("💼 Work Experience")
st.subheader("Promoter, PETRONAS, 2023")
st.markdown("""
- Get a customer support for Setel apps to refill the fuel easily.  
- Provide the benefits and advantages of using the Setel app.
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
st.header("💻 Projects")
st.subheader("Smart Macaque Detection Live Tracking Cage Monitoring Through CCTV Applications")
st.markdown("""
Developed a **real-time monkey detection system** using **YOLOv11**,  
optimized for deployment on **CCTV video surveillance feeds** in urban, agricultural, and forest-edge environments.
""")

#Achievements 
st.header("🎯 Achievements") 
st.markdown("**3rd Place in Trailblazer Cup 2025**")
st.markdown("**1st place in Lawn Ball Men's Category of KRISMA 2025**")
st.markdown("**Dean's Award: Semester 1, 2, and 5**")

#Activities and Societies 
st.header("♟️ Activities and Societies")
st.markdown("**Information Technology Club (SST) 24/25**")
st.markdown("**Position:** President")
st.markdown("**Acedemic Ambassador of FSDK 24/25**")
st.markdown("**Member of the Student Conference Board 24/25**")
st.markdown("**Genius Madani @ SMK Machang 2025**")
st.markdown("**Position:** Chief Facilitator") 
st.markdown("**Jom Masuk U 2024 Zon Timur 1**")
