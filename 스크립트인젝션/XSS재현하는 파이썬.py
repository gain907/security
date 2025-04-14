from flask import Flask, render_template, request

# Flask 웹서버 애플리케이션 생성
app = Flask(__name__)

# 🛑 저장형(stored) XSS 시뮬레이션용: 데이터베이스에서 값을 불러온다고 가정
def fake_get_from_database():
    # 실제로는 DB에서 가져오는 값이지만, 여기선 악성 스크립트를 고정값으로 설정
    data = "<script>alert('stored xss run')</script>"
    return data

# 📍 '/xss' 경로로 GET 또는 POST 요청이 들어올 때 실행되는 함수
@app.route("/xss", methods=["GET", "POST"])
def xss():
    # reflected XSS용 사용자 입력값 초기화
    reflected_xss_string = ""
    # stored XSS용 출력값 초기화
    stored_xss_string = ""

    # GET 요청일 때만 동작 (URL에 입력값을 넣었을 경우)
    if request.method == "GET":
        # 쿼리스트링에 'inputText'라는 파라미터가 있을 경우
        if "inputText" in request.args:
            # 사용자가 입력한 값을 가져와 reflected XSS 변수에 저장
            reflected_xss_string = request.args.get("inputText", default="", type=str)
            # 저장형 XSS 시뮬레이션: DB에서 데이터를 가져온다고 가정
            stored_xss_string = fake_get_from_database()

    # HTML 템플릿에 값을 전달하여 화면에 렌더링
    return render_template("xss_has_vulnerability.html",
                           reflected_xss_string=reflected_xss_string,
                           stored_xss_string=stored_xss_string)

# Flask 웹서버 실행
# 127.0.0.1:5000에서 실행되며, debug 모드를 활성화하여 오류를 상세히 표시함
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
