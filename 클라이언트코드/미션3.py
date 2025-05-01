from flask import Flask,request,render_template,make_response,redirect,url_for

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def user_info():
    name = ""
    hobby = ""

    if request.method == "POST":
        name = request.form.get("name","")
        hobby = request.form.get("hobby","")
        response = make_response(redirect(url_for('user_info')))
        response.set_cookie("user_name", name)
        response.set_cookie("user_hobby", hobby)
        return response

    name = request.cookies.get('user_name')
    hobby = request.cookies.get('user_hobby')

    if not name:  # 쿠키값이 없으면
        name = "아직 저장된 이름이 없습니다."
    if not hobby:  # 쿠키값이 없으면
        hobby = "아직 저장된 취미가 업습니다."

    return render_template(
        'user_info.html',
                    name = name,hobby = hobby)


@app.route("/delete_name", methods=["GET","POST"])
def delete_name():
    response = make_response(redirect(url_for('user_info')))
    response.delete_cookie("user_name")
    return response

@app.route("/delete_hobby", methods=["GET","POST"])
def delete_hobby():
    response = make_response(redirect(url_for('user_info')))
    response.delete_cookie("user_hobby")
    return response

# 이 파일이 직접 실행되었을때 웹서버 시작
if __name__ == "__main__":
# 디버그 모드로 127.0.0.1:5000에서 실행
      app.run(debug=True)


