import streamlit as st

st.set_page_config(page_title="Profile", page_icon="👋⚡")
st.markdown("# Ola! Me chamo Moises 👋 ")
st.sidebar.image('foto.jpg', caption='Profile')
st.sidebar.header("Profissional")

col1, col2, col3, col4 = st.columns(4)
        # Profile photo section
with col2: 
            profile_pic = "https://media.licdn.com/dms/image/D4D03AQHLi_7zjzgwag/profile-displayphoto-shrink_800_800/0/1709338480506?e=1722470400&v=beta&t=kUcNcndj5Eg-_thVA0haP-pZKY5u22cHWEh8AlSCcPE"
            st.image(profile_pic, width=200)

st.write("Profissional versátil com experiência em diversas áreas da tecnologia, com ênfase em infraestrutura, cloud computing, DevOps, blockchain e criptomoedas."

)                         
