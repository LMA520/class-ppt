import streamlit as st
st.set_page_config(
    page_title="lma App",
    page_icon="🧊",
    layout="wide",
    #initial_sidebar_state="expanded",
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://deepseek.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)
st.title("欢迎来到视频播放区域")
st.video("C:\Users\123\Downloads\VID_135.mp4")
st.write("下面看一个情况，并做出准确判断")
st.image("C:\Users\123\Downloads\IMG_20261101_165439.jpg")
select = st.radio("你认为该行为有传染艾滋病的风险吗?",["有","无"]
if select == "有" :
    st.write("回答错误")
else :
    st.write("回答正确")
