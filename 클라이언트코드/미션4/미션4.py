from flask import Flask, request, render_template, make_response, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "")
        response = make_response(redirect(url_for("index")))
        response.set_cookie("user_name", name)
        return response

    name = request.cookies.get("user_name", "쿠키 없음")
    return render_template("fiddler_mission.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)
