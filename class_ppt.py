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
st.video("VID_135.mp4")
st.write("下面看一个情况，并做出准确判断")
st.image("IMG_6733.jpeg")
select = st.radio("你认为该行为有传染艾滋病的风险吗?",["有","无"])
if st.button("提交答案"):
    if select == "有" :
        st.write("回答错误")
        st.image("IMG_6726.jpeg")
        st.title("不行啊，老弟")
    else :
        st.write("回答正确")
        st.image("IMG_6728.jpg")
        st.title("恭喜你，答对了~")
