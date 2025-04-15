import re
import pyodbc

# 데이터베이스 연결 및 커서 반환 함수
def get_cursor():
    # DB 연결 정보 설정
    server = "localhost"
    database = "mytest"
    username = "pyuser"
    password = "Test1234%^&"

    # MSSQL 연결 문자열 구성 및 연결 시도
    mssql_conn = pyodbc.connect(
        'DRIVER={ODBC Driver 17 for SQL Server};'
        'SERVER=' + server + ';'
        'PORT=1433;'  #  1433은 SQL Server가 클라이언트 연결을 수신하는 기본 포트 번호
        'DATABASE=' + database + ';'
        'UID=' + username + ';'
        'PWD=' + password
    )

    # 커서 생성 및 반환
    cursor = mssql_conn.cursor()
    return cursor

# DB 연결 커서 생성
cursor = get_cursor()

    # 사용자 입력값 받기
user_input = input("검색할 사용자 이름을 입력하세요(한글,영문,숫자가능):")

if re.fullmatch(r"[가-힣a-zA-Z0-9]+",user_input):
    query= "select * from order_record where member_id = ?"
    cursor.execute(query,user_input)
    rows = cursor.fetchall()

    print("\n결과 출력")
    for row in rows:
        print(row)
else:
    print("\n 허용되지 않은 입력입니다. 한글,영어,숫자만 사용할수 있습니다.")

