import streamlit as st
st.session_state["current_url"] = st.context.url

#创建三个页面
page_1 = st.Page("page_1.py", title="page 1")
page_2 = st.Page("page_2.py", title="robot chat")
page_3 = st.Page("page_3.py", title="page 3")

#创建导航菜单
pages = st.navigation([page_1, page_2, page_3])

#运行页面
pages.run()
