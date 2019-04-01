# 가상 환경 설정
python -m venv "name"

# 가상 환경 진입
./activate.bat

# 프로젝트에 필요한 모듈 설치
pip install tweetpy, python-twitter, django

# 장고 프로젝트 생성
django-admin startproject "project_name"

# 장고 앱 생성
python manage.py startapp twitterAnal

# 장고 앱 프로젝트 설정 파일에 추가
INSTALLED_APPS = [
    'twitterAnal.apps.TwitteranalConfig',
    '''
]

# 만든 앱 urls.py 생성 후 urls.py 설정 및 프로젝트 루트 urls.py에 include
루트 프로젝트의 urls.py
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("twitterAnal.urls"))
]

생성한 앱의 urls.py
from django.urls import path
from . import views
urlpatterns = [
    path('', views.main, name="main"),
]

# 간단한 테스트 코드 작성
views.py
def main(request):
    return HttpResponse("안녕")

# localhost:8000 or 127.0.0.1:8000 테스트
안녕이 뜬다면 완료.

# 만든 app의 views.py 작성
from django.shortcuts import render, HttpResponse
from tweepy import Stream, OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import json, csv
from datetime import datetime

# 권한 키
c_key = '17NYW4W4x9eedwg8QywWuntm7'
c_s_key = 'LuyzvFr8m7RlsmvszuQaTQ8qYIvWmEtqW4G4ihVoJR8lhtFcoW'
a_key = '1108953758187180033-q5GhwoOGRdjo0eByNTzMUPgI0X6JPi'
a_s_key = 'VYfhk8OnyRRiUgvrMAnWosntolKlsFCMVYt4Zj4NplkoE'

# 추출 데이터 및 정보 저장 변수
datas = {}
keywords = ['짜장면', '탕수육', '짬뽕', '찌개', '밥', '비빔밥', '볶음', '팔보채', '훠궈',\
            '돈가스', '우동', '규동', '짜장', '카레']

# 파일 쓰기
def csv_write(data):
    date_str = datetime.today().strftime("%Y%m%d")
    # write json
    with open('j'+date_str+'.json', 'w', encoding='utf-8') as jw:
        json.dump(datas, jw)
        jw.close()

    # write csv
    with open('d'+date_str+'.csv', 'a', newline='\n', encoding='utf-8') as fw:
        w = csv.writer(fw)
        w.writerow([datetime.now(), data[0], data[1], data[2]])
        fw.close()

class listener(StreamListener):
    def on_status(self, data):
        for key in keywords:
            if data.text.find(key) != -1:
                dataset = [data.user.screen_name, data.id, data.text]
                print(datetime.now(), data.user.screen_name, data.id, data.text)
                # dictionary에 해당 키가 없으면 1로 초기화
                if not key in datas.keys():
                    datas[key] = 1
                # 있으면 그 값 증가
                else:
                    datas[key] += 1
                print(datas)
                csv_write(dataset)
         
        return True
    def on_error(self, status_code):
        if status_code == 420:
            return False
        elif status_code == 401:
            print("401 Error Occured")
            return False

def init():
    auth = OAuthHandler(c_key, c_s_key)
    auth.set_access_token(a_key, a_s_key)
    api = tweepy.API(auth)
    twit_stream = Stream(auth, listener())
    twit_stream.sample()

def main(request):
    init()
    return render(request, 'twitterAnal/index.html', {
        'datas' : json.dumps(datas, ensure_ascii=False),
    })

# templates 폴더 생성 후 .html 파일 만들고 만들어진 json 파일을 보내어
# 그래프 등으로 해결할 수 있다.\

# html에서 js로 json 객체 넘기기
render를 통해 html에 json 객체를 넘겨 주었고, 해당 객체를 js에 넘겨 morris.js 라이브러리를 통해 표를 그려보자.

<html>
<head>
 <link rel="stylesheet" href="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.css">
 <script src="//ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js"></script>
 <script src="//cdnjs.cloudflare.com/ajax/libs/raphael/2.1.0/raphael-min.js"></script>
 <script src="//cdnjs.cloudflare.com/ajax/libs/morris.js/0.5.1/morris.min.js"></script>
    <title>Twitter Analysis</title>
</head>
<body>
    <div id="datas"></div>
    <button onclick="test({{datas}});">동기화</button>
                            // 서버에서 넘어온 JSON을 바로 넘겨도
                            // OBJECT로 사용 가능하다.
<script src="http://code.jquery.com/jquery-2.0.0.js"></script>  
<script>
function test(a){
    // 여기에서 a는 datas 즉, json 객체를 그대로 가지고 와 a['항목'] 등으로 사용할 수 있다.
    $("#datas").empty();
    menu_list = [];
    datas = {};
    var menu_list = Object.keys(a); // json 객체의 길이 구하기 Object.keys(json).length;
    // length를 안 붙이면 해당 키들의 값만 배열로 반환
    
    // key, value 값 얻어내기
    for ( var menu in a){
        //alert(a[menu]);
        datas = a;
        datas['y'] = "데이터 수집가 안주영";
    }
    
    Morris.Bar({
        element: 'datas',
        data: [
            datas,
        ],
        xkey: 'y',
        ykeys: menu_list,
        labels: menu_list
    });
}
</script>
</body>
</html>