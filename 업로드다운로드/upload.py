from flask import Flask,request,render_template
# 파일 이름을 안전하게 처리하기 위한 모듈
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/upload", methods=["GET","POST"])
def upload():
    return render_template('updown_upload.html')

@app.route("/upload_process", methods=["GET","POST"])
def upload_process():

    if request.method == 'POST':
        # name = "uploaded_file"
        file_object = request.files['uploaded_file']
        # 보안 처리를 통해 안전한 파일 이름으로 저장
        file_object.save(secure_filename(file_object.filename))

        return 'file upload complete!!!'

if __name__ == "__main__":
# 디버그 모드로 127.0.0.1:5000에서 실행
      app.run(debug=True)