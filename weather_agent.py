import requests
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

@tool
def get_weather(city: str) -> str:
    """查询指定城市的实时天气，例如首尔、北京、上海、东京。"""

    cities = {
        "首尔": (37.5665, 126.9780),
        "北京": (39.9042, 116.4074),
        "上海": (31.2304, 121.4737),
        "东京": (35.6762, 139.6503)
    }

    if city not in cities:
        return "暂时不支持这个城市。"

    latitude, longitude = cities[city]

    url = "https://api.open-meteo.com/v1/forecast"

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,apparent_temperature,wind_speed_10m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    weather = response.json()["current"]

    return (
        f"{city}当前气温：{weather['temperature_2m']}℃，"
        f"体感温度：{weather['apparent_temperature']}℃，"
        f"湿度：{weather['relative_humidity_2m']}%，"
        f"风速：{weather['wind_speed_10m']} km/h"
    )
import os
from dotenv import load_dotenv

#读取 API Key
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

#创建 Gemini 模型
model = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    google_api_key=api_key
)
#创建记忆保存器
memory = InMemorySaver()

#创建 LangChain Agent
agent = create_agent(
    model=model,
    tools=[get_weather],
    checkpointer=memory,
    system_prompt="你是一个天气助手。用户询问天气时，使用天气工具获取真实数据，再用中文清晰地回答。"
)

print("天气 Agent 创建成功！")

#设置对话线程
config = {
    "configurable": {
        "thread_id": "weather-chat-001"
    }
}

#开始对话
if __name__ == "__main__":
    while True:     
        user_input = input("\n你：")

        if user_input.lower() in ["exit", "quit", "退出"]:
            print("再见！")
            break

        result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": user_input}
            ]
        },
        config=config
    )

        print("\nAI：", result["messages"][-1].content)
