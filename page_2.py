
import streamlit as st
from google import genai
from dotenv import load_dotenv
import os 
import requests

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
def get_weather(city: str) -> dict:
    """
    查询指定城市的实时天气。

    Args:
        city: 城市名称，例如首尔、北京、上海、东京。
    """
    cities = {
        "首尔": (37.5665, 126.9780),
        "서울": (37.5665, 126.9780),
        "东京": (35.6762, 139.6503),
        "北京": (39.9042, 116.4074),
        "上海": (31.2304, 121.4737)
    }

    if city not in cities:
        return "暂时不支持这个城市"

    latitude, longitude = cities[city]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,precipitation,weather_code,wind_speed_10m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    return response.json()["current"]


#创建聊天记录存储空间
if "messages" not in st.session_state:
    st.session_state.messages = []

#创建输入框
prompt = st.chat_input("请输入消息...")

#用户输入后，保存用户消息
if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    #调用 Gemini AI
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt,
            config=genai.types.GenerateContentConfig(
                tools=[get_weather]
            )
        )

        ai_reply = response.text

        st.session_state.messages.append({
            "role": "assistant",
            "content": ai_reply
        })

    except Exception as e:
        st.error(f"AI 调用失败：{e}")

#显示所有聊天记录
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
