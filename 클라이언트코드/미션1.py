from flask import Flask,request,render_template,make_response,redirect,url_for

app = Flask(__name__)
@app.route("/", methods=["GET","POST"])
def favorite_food():
    food = ""
    saved_food = ""

    if request.method == "POST":
        food = request.form.get("food","")
        response = make_response(redirect(url_for('favorite_food')))
        response.set_cookie("favorite_food", food)
        return response

    saved_food = request.cookies.get('favorite_food')
    if not saved_food:  # 쿠키값이 없으면
        saved_food = "아직 저장된 음식이 없습니다."

    return render_template(
        'favorite_food1.html',
                    food = saved_food
                    )


 # 이 파일이 직접 실행되었을때 웹서버 시작
if __name__ == "__main__":
# 디버그 모드로 127.0.0.1:5000에서 실행
      app.run(debug=True)


