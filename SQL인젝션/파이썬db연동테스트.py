import pyodbc

# ✅ ODBC 연결 문자열 정의
# - DRIVER: 설치된 ODBC 드라이버 이름과 일치해야 함
# - SERVER: 데이터베이스 서버 주소 (로컬이면 localhost 또는 컴퓨터이름\인스턴스명)
# - DATABASE: 사용할 데이터베이스 이름
# - UID: 사용자명
# - PWD: 비밀번호
# - TrustServerCertificate: 인증서 오류 무시 (테스트용으로 주로 사용)

# 연결 문자열 (ODBC 드라이버 및 로그인 정보)
conn_str = (
    "DRIVER={ODBC Driver 17 for SQL Server};"
    "SERVER=localhost;"
    "DATABASE=mytest;"
    "UID=pyuser;"
    "PWD=Test1234%^&;"
    "TrustServerCertificate=yes;"
    # PORT=1433  1433은 SQL Server가 클라이언트 연결을 수신하는 기본 포트 번호 안써도 됨
)

try:
    # 데이터베이스 연결 시도
    conn = pyodbc.connect(conn_str)
    print("✅ 데이터베이스 연결 성공!")

    # 연결 종료
    conn.close()

except Exception as e:
    # 연결 실패 시 에러 메시지 출력
    print("❌ 연결 실패:", e)