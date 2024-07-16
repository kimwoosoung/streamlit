import streamlit as st
st.header("김우성은 :blue[축구]를 좋아한다? O/X")
st.text('')

if st.button("O"):
  st.write("다시한번 풀어보세요...")

if st.button("X"):
  st.write("저를 잘 알고 있군요!   감사합니다😆")


import streamlit as st
st.header("김우성의 :blue[생일은 5월 30일]이다? O/X")
st.text('')

if st.button("o"):
  st.write("저를 잘 알고 있군요!   감사합니다😆")

if st.button("x"):
  st.write("다시한번 풀어보세요...")

import streamlit as st

st.title("김우성에 대한 퀴즈!")
password1 = "ㄱㄱ"
answer1 = "브롤스타즈"

quiz1_password = st.text_input("퀴즈를 풀고싶다면, [ㄱㄱ]이라고 적어주세요",  key="quiz1_password")
if quiz1_password == password1:
    quiz1 = st.text_input("김우성이 제일 좋아하는 :blue[게임]은 무엇인가요?")
    if st.button("정답 확인", key="check_answer_button1"):
        if quiz1 == answer1:
            st.balloons()
            st.success("정답입니다!")
            st.write("저 김우성이 하는 유일한 게임이죠 ㅎㅎ")
        else:
            st.warning("엄... 다시 한번 생각해보세요")
    if st.button("힌트 보기", key="check_hint_button1"):
            st.write(" '브'로 시작하는 게임입니다! ")
elif quiz1_password != "" and quiz1_password != password1:
    st.error("다시 입력해 주세요")