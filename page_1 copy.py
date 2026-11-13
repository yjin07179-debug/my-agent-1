
import streamlit as st

if "favorite" not in st.session_state:
    st.session_state.favorite = False


st.markdown(
    '<h1 style="color:#00BFFF;">Hello</h1>',
    unsafe_allow_html=True
)
st.badge("Welcome", icon=":material/check:", color="green")

st.markdown("""
本网站功能

🌤️ 天气查询：通过天气 API 获取实时天气。

📈 股票查询：通过 Alpha Vantage API 获取股票行情。
""")


if "favorite" not in st.session_state:
    st.session_state.favorite = False


star = "★" if st.session_state.favorite else "☆"
label = f"{star} Favorite"

st.markdown(
    f"""
    <style>
    div.stButton > button {{
        background-color: #9B59B6;
        color: white;
        border: none;
        border-radius: 8px;
        font-weight: bold;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

if "favorites" not in st.session_state:
    st.session_state.favorites = []

if st.button(label, key="favorite_button"):
    url = st.session_state["current_url"]

    if url not in st.session_state.favorites:
        st.session_state.favorites.append(url)
        st.toast("❤️ 已加入收藏！")
    else:
        st.session_state.favorites.remove(url)
        st.toast("已取消收藏")

    st.rerun()



st.markdown("""
<style>
@keyframes toastFade {
    0% {
        opacity: 1;
    }
    70% {
        opacity: 1;
    }
    100% {
        opacity: 0;
    }
}

div[data-testid="stToast"] {
    animation: toastFade 3s ease forwards;
}
</style>
""", unsafe_allow_html=True)
