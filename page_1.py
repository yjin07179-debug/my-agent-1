
import streamlit as st
import base64
from pathlib import Path

st.set_page_config(
    page_title="My Agent",
    page_icon="🐾",
    layout="wide"
)

# 读取比熊背景图
image_path = Path(__file__).parent / "bichon_bg.png"

if image_path.exists():
    image_data = base64.b64encode(image_path.read_bytes()).decode()
    background = f"data:image/png;base64,{image_data}"
else:
    background = ""

# 收藏状态
if "favorite" not in st.session_state:
    st.session_state.favorite = False

# 页面样式
st.markdown(f"""
<style>
.stApp {{
    background:
        linear-gradient(90deg, rgba(70, 40, 75, 0.72),
        rgba(80, 50, 85, 0.30)),
        url("{background}");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

header[data-testid="stHeader"] {{
    background: transparent;
}}

.block-container {{
    padding-top: 2rem;
}}

h1, h2, h3, p, label {{
    color: white !important;
}}

div.stButton > button {{
    background: rgba(255,255,255,0.20);
    color: white;
    border: 1px solid rgba(255,255,255,0.4);
    border-radius: 14px;
    padding: 12px 18px;
    font-weight: bold;
}}

div.stButton > button:hover {{
    background: rgba(180,120,230,0.65);
    border-color: white;
}}

.hero {{
    padding: 75px 15px 25px 15px;
}}

.hero h1 {{
    font-size: 64px;
    font-weight: 800;
}}

.hero p {{
    font-size: 21px;
}}

.feature {{
    background: rgba(255,255,255,0.20);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 18px;
    padding: 18px;
    min-height: 100px;
    color: white;
}}
</style>
""", unsafe_allow_html=True)

# 顶部导航
nav1, nav2, nav3, nav4, nav5 = st.columns([2, 1, 1, 1, 1])

with nav1:
    st.markdown("## 🐾 My Agent")

with nav2:
    if st.button("🏠 首页", use_container_width=True):
        st.rerun()

with nav3:
    if st.button("💬 AI 聊天", use_container_width=True):
        st.switch_page("page_2.py")

with nav4:
    if st.button("🌤️ 天气", use_container_width=True):
        st.switch_page("page_2.py")

with nav5:
    if st.button("📈 股票", use_container_width=True):
        st.switch_page("page_2.py")




# 功能卡片
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div class="feature">
    💬 <b>AI 聊天</b><br>
    智能对话，回答问题
    </div>
    """, unsafe_allow_html=True)
    if st.button("进入 AI 聊天", key="chat"):
        st.switch_page("page_2.py")

with c2:
    st.markdown("""
    <div class="feature">
    🌤️ <b>天气查询</b><br>
    获取实时天气信息
    </div>
    """, unsafe_allow_html=True)
    if st.button("查询天气", key="weather"):
        st.switch_page("page_2.py")

with c3:
    st.markdown("""
    <div class="feature">
    📈 <b>股票查询</b><br>
    查询股票行情信息
    </div>
    """, unsafe_allow_html=True)
    if st.button("查询股票", key="stock"):
        st.switch_page("page_2.py")

st.write("")

# 收藏按钮
star = "★" if st.session_state.favorite else "☆"

if st.button(f"{star} 收藏首页", key="home_favorite"):
    st.session_state.favorite = not st.session_state.favorite
    if st.session_state.favorite:
        st.toast("❤️ 已收藏！")
    else:
        st.toast("已取消收藏！")
    st.rerun()

if not image_path.exists():
    st.warning("暂时没有找到 bichon_bg.png，请确认图片和 page_1.py 在同一个文件夹。")
