import streamlit as st
from boxsdk import JWTAuth, Client
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

client_id = os.getenv("BOX_CLIENT_ID")
client_secret = os.getenv("BOX_CLIENT_SECRET")
enterprise_id = os.getenv("BOX_ENTERPRISE_ID")
jwt_private_key = os.getenv("BOX_JWT_PRIVATE_KEY").replace("\\n", "\n")
jwt_private_key_password = os.getenv("BOX_JWT_PRIVATE_KEY_PASSWORD")
jwt_public_key_id = os.getenv("BOX_JWT_PUBLIC_KEY_ID")

# JWT 인증 설정
auth = JWTAuth(
    client_id=client_id,
    client_secret=client_secret,
    enterprise_id=enterprise_id,
    jwt_key_id=jwt_public_key_id,
    rsa_private_key_data=jwt_private_key,
    rsa_private_key_passphrase=jwt_private_key_password.encode('utf-8')
)

client = Client(auth)

# Box에서 파일 다운로드
file_id = 'YOUR_FILE_ID'
box_file = client.file(file_id).get()
content = box_file.content()

# Streamlit에서 파일 내용 표시
st.text(content.decode('utf-8'))
