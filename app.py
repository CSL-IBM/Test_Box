import streamlit as st
from boxsdk import JWTAuth, Client
from dotenv import load_dotenv
import os

# .env 파일에서 환경 변수 로드
load_dotenv()

# 환경 변수 로드 및 디버깅 출력
client_id = os.getenv("BOX_CLIENT_ID")
client_secret = os.getenv("BOX_CLIENT_SECRET")
enterprise_id = os.getenv("BOX_ENTERPRISE_ID")
jwt_private_key = os.getenv("BOX_JWT_PRIVATE_KEY")
jwt_private_key_password = os.getenv("BOX_JWT_PRIVATE_KEY_PASSWORD")
jwt_public_key_id = os.getenv("BOX_JWT_PUBLIC_KEY_ID")

# 디버깅 출력
st.write("Client ID: ", client_id)
st.write("Client Secret: ", client_secret)
st.write("Enterprise ID: ", enterprise_id)
st.write("JWT Private Key: ", jwt_private_key[:30] + "...")  # 키의 일부만 출력
st.write("JWT Private Key Password: ", jwt_private_key_password)
st.write("JWT Public Key ID: ", jwt_public_key_id)

# 환경 변수 값이 None인지 확인
if None in [client_id, client_secret, enterprise_id, jwt_private_key, jwt_private_key_password, jwt_public_key_id]:
    st.error("One or more environment variables are not set correctly.")
else:
    # JWT 인증 설정
    try:
        auth = JWTAuth(
            client_id=client_id,
            client_secret=client_secret,
            enterprise_id=enterprise_id,
            jwt_key_id=jwt_public_key_id,
            rsa_private_key_data=jwt_private_key.replace("\\n", "\n"),
            rsa_private_key_passphrase=jwt_private_key_password.encode('utf-8')
        )
        st.write("JWTAuth 객체 생성 성공")
    except Exception as e:
        st.error(f"JWTAuth 객체 생성 실패: {e}")

    # Box 클라이언트 생성 및 파일 다운로드
    try:
        client = Client(auth)
        file_id = 'YOUR_FILE_ID'
        box_file = client.file(file_id).get()
        content = box_file.content()
        st.text(content.decode('utf-8'))
        st.write("파일 다운로드 성공")
    except Exception as e:
        st.error(f"Box 클라이언트 또는 파일 다운로드 실패: {e}")
