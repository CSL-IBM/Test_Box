import streamlit as st
from boxsdk import Client, OAuth2

# Streamlit Secrets에서 Box API 정보 로드
client_id = st.secrets["BOX_CLIENT_ID"]
client_secret = st.secrets["BOX_CLIENT_SECRET"]
developer_token = st.secrets["BOX_DEVELOPER_TOKEN"]

# OAuth2 인증 설정
auth = OAuth2(
    client_id=client_id,
    client_secret=client_secret,
    access_token=developer_token,
)

client = Client(auth)

# Box에서 파일 다운로드
file_id = 'YOUR_FILE_ID'
box_file = client.file(file_id).get()
content = box_file.content()

# Streamlit에서 파일 내용 표시
st.text(content.decode('utf-8'))
