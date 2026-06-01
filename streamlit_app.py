import streamlit as st

import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="나의 자기소개 페이지",
    page_icon="👋",
    layout="centered"
)

# 2. 사이드바 구성 (연락처 및 링크)
with st.sidebar:
    st.header("Contact & Links")
    st.write("📧 이메일: email@example.com")
    st.write("🐙 GitHub: [github.com/username](https://github.com)")
    st.write("📝 블로그: [velog.io/@username](https://velog.io)")
    
    st.markdown("---")
    st.caption("© 2026. All rights reserved.")

# 3. 메인 화면 - 히어로 섹션
st.title("👋 안녕하세요, 홍길동입니다!")
st.subheader("💡 문제를 해결하며 성장하는 풀스택 개발자입니다.")

# 프로필 이미지 넣기 (이미지 파일이 없다면 URL로 대체 가능)
# 여기에 실제 본인 사진 파일 경로(예: 'profile.jpg')를 넣거나, 아래처럼 샘플 이미지를 사용하세요.
st.image("https://images.unsplash.com/photo-1534528741775-53994a69daeb?auto=format&fit=crop&q=80&w=500", width=200)

st.markdown("---")

# 4. 상세 소개 섹션
st.header("📝 About Me")
st.write("""
- **성장 지향성**: 새로운 기술을 배우고 적용하는 것을 즐깁니다.
- **협업 중심**: 원활한 소통을 통해 팀의 생산성을 높이는 데 기여합니다.
- **데이터 관심**: 데이터를 분석하고 이를 기반으로 서비스를 개선하는 것에 관심이 많습니다.
""")

st.markdown("---")

# 5. 기술 스택 섹션 (태그 형태로 시각화)
st.header("🛠️ Tech Stacks")

col1, col2 = st.columns(2)

with col1:
    st.markdown("### Languages")
    st.code("Python, JavaScript, SQL", language="text")

with col2:
    st.markdown("### Frameworks & Tools")
    st.code("Streamlit, Fastapi, React, Git", language="text")

st.markdown("---")

# 6. 인터랙티브 기능 - 방명록 남기기
st.header("💬 방명록")
st.write("이곳을 방문해주신 소감을 남겨주세요!")

# 세션 상태를 이용해 방명록 메시지 저장하기
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"name": "길동이 친구", "text": "포트폴리오가 아주 멋지네요! 👍"}
    ]

# 방명록 입력 폼
with st.form(key="guestbook_form", clear_on_submit=True):
    visitor_name = st.text_input("이름", placeholder="이름을 입력하세요.")
    visitor_msg = st.text_area("메시지", placeholder="따뜻한 한마디를 남겨주세요.")
    submit_button = st.form_submit_button(label="등록하기")

if submit_button:
    if visitor_name and visitor_msg:
        st.session_state.messages.append({"name": visitor_name, "text": visitor_msg})
        st.success("방명록이 등록되었습니다!")
    else:
        st.error("이름과 메시지를 모두 입력해주세요.")

# 등록된 방명록 출력
st.markdown("### 최근 방명록")
for msg in reversed(st.session_state.messages):
    st.markdown(f"**👤 {msg['name']}** : {msg['text']}")