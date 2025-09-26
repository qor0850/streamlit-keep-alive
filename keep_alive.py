import requests
from datetime import datetime

URL = "https://qr-landing.streamlit.app/"

def main():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("🌐 Streamlit KeepAlive 스크립트 시작")
    print(f"🕐 실행 시간 : {now}")
    print(f"🌍 접속 URL  : {URL}")

    try:
        response = requests.get(URL, timeout=10)
        if response.status_code == 200:
            print(f"✅ 접속 성공 - 상태 코드: {response.status_code}")
        else:
            print(f"⚠️ 접속 실패 - 상태 코드: {response.status_code}")
    except Exception as e:
        print(f"❌ 예외 발생: {e}")

    print("🔚 실행 완료. 로그는 GitHub Actions에서 확인하세요.")

if __name__ == "__main__":
    main()
