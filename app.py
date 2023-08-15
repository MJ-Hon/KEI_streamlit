import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.title('KEI 환경 이슈 대시보드')

st.sidebar.header("환경 이슈")
selected_option = st.sidebar.radio("Select an option", ["대기오염", "탄소중립", "기후변화"])

if selected_option == "대기오염":
    st.header("대기오염")
    st.write("이 장에서는 대기오염에 대한 정보를 제공합니다.")
    
    tabs = st.tabs(["Tab 1", "Tab 2"])
    
    # 각 탭의 내용
    with tabs[0]:
        st.write("이것은 Tab 1의 내용입니다.")
        
        # 탭 내에서 그래프 추가
        x = np.linspace(0, 10, 100)
        y = np.sin(x)
        plt.plot(x, y)
        st.pyplot(plt)
        
    with tabs[1]:
        st.write("이것은 Tab 2의 내용입니다.")
        st.write("Google Data Studio 대시보드:")
        st.write('<iframe width="600" height="1200" src="https://lookerstudio.google.com/embed/reporting/3d1b7550-d95b-4cef-aa6b-13f66ca6a5e4/page/XsjYD" frameborder="0" style="border:0" allowfullscreen></iframe>', unsafe_allow_html=True)
  


elif selected_option == "탄소중립":
    st.header("탄소중립")
    st.write("이 장에서는 탄소중립에 대한 정보를 제공합니다.")
    # 추가적인 내용을 작성할 수 있습니다.

elif selected_option == "기후변화":
    st.header("기후변화")
    st.write("이 장에서는 기후변화에 대한 정보를 제공합니다.")
    # 추가적인 내용을 작성할 수 있습니다.
