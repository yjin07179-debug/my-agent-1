
import streamlit as st
import base64
from pathlib import Path

# =========================
# 페이지 기본 설정
# =========================

st.set_page_config(
    page_title="My Agent",
    page_icon="🐾",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# =========================
# 배경 이미지 불러오기
# =========================

image_path = Path(__file__).parent / "bichon_bg.png"

if image_path.exists():
    image_data = base64.b64encode(
        image_path.read_bytes()
    ).decode()
    background = f"data:image/png;base64,{image_data}"
else:
    background = ""

# =========================
# 즐겨찾기 상태
# =========================

if "favorite" not in st.session_state:
    st.session_state.favorite = False

# =========================
# 페이지 CSS 스타일
# =========================

st.markdown(f"""
<style>

#MainMenu {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

.stApp {{
    background:
        linear-gradient(
            90deg,
            rgba(45, 30, 48, 0.78),
            rgba(70, 45, 75, 0.35)
        ),
        url("{background}");

    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}}

header[data-testid="stHeader"] {{
    background: transparent;
}}

.block-container {{
    max-width: 1450px;
    padding-top: 1rem;
    padding-bottom: 3rem;
}}

h1, h2, h3, p, label, span {{
    color: white;
}}

.hero {{
    padding: 95px 15px 35px 15px;
}}

.hero h1 {{
    font-size: 68px;
    font-weight: 850;
    letter-spacing: 2px;
    margin-bottom: 8px;
}}

.hero h2 {{
    font-size: 27px;
    font-weight: 500;
    margin-bottom: 22px;
}}

.hero p {{
    font-size: 19px;
    color: rgba(255,255,255,0.85);
}}

div.stButton > button {{
    background: rgba(255,255,255,0.17);
    color: white;
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 16px;
    padding: 12px 15px;
    font-size: 16px;
    font-weight: 600;
    transition: 0.25s;
}}

div.stButton > button:hover {{
    background: rgba(160,110,230,0.55);
    border-color: white;
    color: white;
    transform: translateY(-2px);
}}

div[data-testid="stTextInput"] input {{
    background: rgba(255,255,255,0.88);
    color: #393044;
    border: none;
    border-radius: 20px;
    padding: 18px;
    font-size: 18px;
    min-height: 62px;
}}

div[data-testid="stTextInput"] input::placeholder {{
    color: #827987;
}}

.feature {{
    background: rgba(255,255,255,0.19);
    backdrop-filter: blur(15px);
    -webkit-backdrop-filter: blur(15px);
    border: 1px solid rgba(255,255,255,0.35);
    border-radius: 22px;
    padding: 25px 20px;
    min-height: 125px;
    color: white;
    margin-bottom: 12px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
}}

.feature-title {{
    font-size: 21px;
    font-weight: bold;
    margin-bottom: 10px;
}}

.feature-desc {{
    font-size: 15px;
    color: rgba(255,255,255,0.85);
}}

.section-title {{
    font-size: 25px;
    font-weight: bold;
    margin: 25px 0 15px 5px;
}}

</style>
""", unsafe_allow_html=True)

# =========================
# 상단 네비게이션
# =========================

nav1, nav2, nav3, nav4, nav5, nav6 = st.columns(
    [2.2, 1, 1.2, 1, 1, 1]
)

with nav1:
    st.markdown("## 🐾 My Agent")

with nav2:
    if st.button("🏠 홈", use_container_width=True):
        st.rerun()

with nav3:
    if st.button("💬 AI 채팅", use_container_width=True):
        st.switch_page("page_2.py")

with nav4:
    if st.button("🌤️ 날씨", use_container_width=True):
        st.switch_page("page_2.py")

with nav5:
    if st.button("📈 주식", use_container_width=True):
        st.switch_page("page_2.py")

with nav6:
    if st.button("⚙️ 설정", use_container_width=True):
        st.info("설정 기능은 현재 개발 중입니다.")

st.markdown("---")


# =========================
# 주요 기능 카드
# =========================

st.markdown(
    '<div class="section-title">✨ 주요 기능</div>',
    unsafe_allow_html=True
)

c1, c2, c3 = st.columns(3)

with c1:

    st.markdown("""
    <div class="feature">
        <div class="feature-title">💬 AI 채팅</div>
        <div class="feature-desc">
            AI와 자유롭게 대화하고 궁금한 질문을 해결하세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("AI 채팅 시작하기 →", key="chat", use_container_width=True):
        st.switch_page("page_2.py")

with c2:

    st.markdown("""
    <div class="feature">
        <div class="feature-title">🌤️ 날씨 정보</div>
        <div class="feature-desc">
            실시간 날씨와 기온, 일기예보를 확인하세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("날씨 확인하기 →", key="weather", use_container_width=True):
        st.switch_page("page_2.py")

with c3:

    st.markdown("""
    <div class="feature">
        <div class="feature-title">📈 주식 정보</div>
        <div class="feature-desc">
            주식 시세와 시장 정보를 확인하세요.
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("주식 확인하기 →", key="stock", use_container_width=True):
        st.switch_page("page_2.py")

# =========================
# 이미지 확인
# =========================

if not image_path.exists():
    st.warning(
        "bichon_bg.png 파일을 찾을 수 없습니다. "
        "이미지를 page_1.py와 같은 폴더에 넣어 주세요."
    )
