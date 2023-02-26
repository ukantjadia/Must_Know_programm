from pathlib import Path

import streamlit as st 
from PIL import Image

## Path settings
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "Ukantjadia.pdf"
profile_pic = current_dir / "assets" / "ukant.jpg"

## gerenral settings
PAGE_TITLE = "Digital CV | Ukant Jadia"
PAGE_ICON = ":wave:"
NAME = "Ukant Jadia"
DESCRIPTION = """
Data Analyst Enthuasist, leading life for better future.
"""
EMAIL = "ukantjadia0120@gmail.com"
SOCIAL_MEDIA = {
    "LinkedIn":"https://linkedin.com/ukantjadia",
    "GitHub":"https://github.com/ukantjadia",
    "Twitter":"https://twitter.com/ukantjadia",
    "Website":"https://www.ukantjadia.me/blog"
}

PROJECTS = {
    "test project" : "https://github.com/ukantjadia",
    "automated yt channel on linux " : "https://github.com/ukantjadia",
    "twitter automated bot" : "https://github.com/ukantjadia",
    "AirBnb stock proce prediction" : "https://github.com/ukantjadia",
}

st.set_page_config(page_title=PAGE_TITLE,page_icon=PAGE_ICON)

## Load css , profile pic and pdf 
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()),unsafe_allow_html=True)
with open(resume_file,"rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


## Hero section

col1, col2 = st.columns(2,gap="small")
with col1: 
    st.image(profile_pic,width=220)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label="Download resume",
        data= PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("XX" , EMAIL)

## SOcial link 
st.write("#")
cols = st.columns(len(SOCIAL_MEDIA))
for index,(platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")

## Experience and qualification 
st.write("#")
st.subheader("Experience and Qualification")
st.write(
    """
    - :right: exp
    - :right: exp
    - :right: exp
    - :right: exp
    - :right: exp
    """
)

## hard skill 
st.write("#")
st.subheader("Hard skills and techniques")
st.write(
    """
    - :right: test skills 
    - :right: test skills 
    - :right: test skills 
    - :right: test skills 
    - :right: test skills 
    """
)

## workk history 
st.write("#")
st.subheader("Work history")
st.write(
    """
    - :right: to much  
    - :right: to much  
    - :right: to much  
    - :right: to much  
    - :right: to much  
    """
)

## job 1
st.write("#")
st.write("Role | Company")
st.write("start date - date end")
st.write(
    """
    salarey, allowance
    expirence there 
    env
    imporvment
    task
    profit to company
    projects
    team, management
    """
)
## job 2
st.write("#")
st.write("Role | Company")
st.write("start date - date end")
st.write(
    """
    salarey, allowance
    expirence there 
    env
    imporvment
    task
    profit to company
    projects
    team, management
    """
)
## job 3
st.write("#")
st.write("Role | Company")
st.write("start date - date end")
st.write(
    """
    salarey, allowance
    expirence there 
    env
    imporvment
    task
    profit to company
    projects
    team, management
    """
)

## Projects and accompleshments 
st.write("#")
st.subheader("projects and Accomplishments")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")