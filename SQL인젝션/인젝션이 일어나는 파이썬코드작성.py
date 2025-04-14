from flask import Flask, render_template, request
import pyodbc

# ✅ 데이터베이스 연결 및 커서 반환 함수
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

"""
SELECT 
    o.member_id, s.food_name,o.buy_count,o.buy_date, s.price,                     
    (s.price * o.buy_count) AS total_price  
FROM order_record o (NOLOCK) 
JOIN supermarket s (NOLOCK) ON s.food_no = o.food_no   
WHERE o.member_id = 'tom' ORDER BY o.buy_count DESC;

"""
# ✅ "/item_search" 경로에 대한 라우팅 처리
@app.route("/item_search", methods=["GET", "POST"])
def item_search():
    search_text = ""  # 검색어 초기화

    # POST 요청일 경우, 사용자가 입력한 검색어를 가져옴
    if request.method == "POST":
        search_text = request.form["searchText"]

    # 🔥 [보안주의] 사용자가 입력한 값을 직접 쿼리에 넣는 방식 → SQL 인젝션 취약!
    search_sql = "select o.member_id, s.food_name, o.buy_count, o.buy_date, " \
                "s.price, (s.price * o.buy_count) " \
                "total_price from order_record o(nolock) " + \
                "join supermarket s(nolock) " + \
                "on s.food_no = o.food_no " + \
                "where o.member_id  = '" + search_text + "' " + \
                "order by o.buy_count desc"

    # SQL 실행 및 결과 가져오기
    cursor.execute(search_sql)

    result_rows = cursor.fetchall()

    # HTML 템플릿 렌더링 및 결과 전달
    return render_template(
        "sql_injection.html",
        rows=result_rows,
        search_text=search_text,
        sql_query=search_sql  # 쿼리 자체도 보여주기 (디버깅 or 교육용)
    )

# ✅ Flask 웹서버 실행 설정
# - 127.0.0.1 (localhost) 주소
# - 포트 5000 사용
# - debug=True: 에러 상세 표시 및 자동 재시작 기능 활성화
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
