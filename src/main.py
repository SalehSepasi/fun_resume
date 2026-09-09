import streamlit as st

st.set_page_config(
    page_title="Fun Resume Generator",
    page_icon="📄",
    layout="wide"
)

st.title("Fun Resume Generator")
st.write("Turn your boring resume into something unforgettable! 😎")
st.header("Tell us about yourself")

with st.container():

    name = st.text_input("your name")
    job = st.text_input("your job or major")
    
    age = st.number_input("your age", min_value=1, max_value=100, value=20)

    skills = st.text_input(
        "your skills",
        placeholder="Python, Git, Cooking..."
    )

    hobbies = st.text_input(
        "your hobbies",
        placeholder="Gaming, Sleeping, Watching movies..."
    )

    personality = st.selectbox(
        "your personality",
        [
            "Lazy 😴",
            "Nerd 🤓",
            "Funny 😂",
            "Serious 😐",
            "Chaotic 💀",
            "Ambitious 🚀",
        ],
    )
    if st.button("Generate my resume 🚀"):
        st.success("Your fun resume is coming soon!")