from flask import Flask, render_template, request
import pyodbc
import re

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

# Flask 웹 애플리케이션 객체 생성
app = Flask(__name__)

# "/item_search" 경로에 대한 라우팅 처리
@app.route("/", methods=["GET", "POST"])
def item_search():
    search_text = ""  # 검색어 초기화 -> get
    result_rows = []
    message = ""
    sql_query = ""

    # POST 요청일 경우, 사용자가 입력한 검색어를 가져옴
    if request.method == "POST":
        search_text = request.form["search_text"]

        if re.fullmatch(r"[가-힣a-zA-Z0-9]+", search_text):
            query = "select * from order_record where member_id = ?"
            cursor.execute(query, search_text)
            result_rows = cursor.fetchall()

            if result_rows:
                message = "정상적으로 검색이 되었습니다"
            else:
                message = "DB에 일치하는 이름이 없습니다"


        else:
            message = "DB 오류, 허용되지 않은 입력입니다. 한글,영어,숫자만 사용할수 있습니다."

     # HTML 템플릿 렌더링 및 결과 전달
    return render_template(
        "allow_list.html",
        msg = message,
        rows=result_rows,
        query = sql_query
    )
# ',%,_,-
# Flask 웹서버 실행 설정
# - 127.0.0.1 (localhost) 주소
# - 포트 5000 사용
# - debug=True: 에러 상세 표시 및 자동 재시작 기능 활성화
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)