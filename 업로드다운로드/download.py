from flask import Flask,request,render_template,make_response
import pandas as pd # 표형태 데이터를 다루기 위한 모듈
import numpy as np # 숫자 배열 생서을 해주는 모듈
import io     # 메모리에 가상 파일 객체를 만들기 위한 모듈

app = Flask(__name__)
@app.route("/excel", methods=["GET","POST"])
def excel():
    # pandas로 데이터 프레임 객체 생성
    dataframe = pd.DataFrame({
        'A': 'fruit drink food'.split(),
        'B': 'orange soda rice'.split(),
        'C': 'banana coffee bread'.split(),
        'D': np.arange(3) # (0~3 까지 숫자 생성해주세요)
    })

    # 메모리위에 가짜파일을 만들고 이걸 바이트 스트림 다룰수 있게 해주는 라이브러리
    # 메모리 파일
    output = io.BytesIO()
    # ExcelWriter를 이용해서 엑셀파일을 메모리에 작성
    writer = pd.ExcelWriter(output)
    # 데이터프레임을 'food'라는 이름으로 엑셀파일에 작성
    dataframe.to_excel(writer,'food')
    # 작성한 내용을 실제 메모리 파일에 저장
    writer.close()

    #
    # 메모리에 작성된 엑셀 파일 내용을 http 응답으로 만들기
    response = make_response(output.getvalue())
    # attachment 다운로드 창을 띄우는 역할
    # filename=download.xlsx 저장시 기본 파일 이름을 지정
    response.headers['Content-Disposition'] = 'attachment; filename=download.xlsx'

    response.headers["Content-type"] = "text/csv"
    # response.headers["Content-Type"] = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    return response

 # 이 파일이 직접 실행되었을때 웹서버 시작
if __name__ == "__main__":
# 디버그 모드로 127.0.0.1:5000에서 실행
      app.run(debug=True)


"""
openpyxl
- 파이썬으로 엑실 파일을 읽고/쓰고/수정 하는 도구
io.BytesIO()
- 메모리에 가짜 파일 생성
Content-Disposition
- 브라우저가 '파일다운로드로 인식'하게 하는 헤더파일
Content-type
- 파일 타입 설정
"""
