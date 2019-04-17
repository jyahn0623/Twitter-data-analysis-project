from django.shortcuts import render, HttpResponse
from tweepy import Stream, OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import json, csv
from datetime import datetime

def test():
    print("hello")
# 권한 키
c_key = '17NYW4W4x9eedwg8QywWuntm7'
c_s_key = 'LuyzvFr8m7RlsmvszuQaTQ8qYIvWmEtqW4G4ihVoJR8lhtFcoW'
a_key = '1108953758187180033-q5GhwoOGRdjo0eByNTzMUPgI0X6JPi'
a_s_key = 'VYfhk8OnyRRiUgvrMAnWosntolKlsFCMVYt4Zj4NplkoE'

# 추출 데이터 및 기초 변수
server_data = datetime.today().strftime("%Y%m%d")
datas = {
    'info' : {
        
    },
    'count' : [
        0, 0, 0
    ],
    'menu' : {

    }
}
keywords = [
    ['짜장면', '탕수육', '짬뽕', '훠궈', '팔보채'],
    ['찌개', '비빔밥', '볶음', '수육', '나물', '국밥'],
    ['우동', '규동', '돈가스', '돈카츠', '카레', '초밥', '스시']
]

track_words = ['.', '!', '?', 'ㅋ', '짜장면', '탕수육', '짜장면', '탕수육', '짬뽕', '찌개', '밥', '비빔밥', '볶음', '팔보채', '훠궈',\
            '돈가스', '우동', '규동', '짜장', '카레']

def init_on_day():
    global datas
    datas = {
        'info' : {
            'data' : server_data,
        },
        'count' : [
            0, 0, 0
        ],
        'menu' : {
        }
    }
# 파일 쓰기
def csv_write(data):
    date_str = datetime.today().strftime("%Y%m%d")
    global server_data, datas
    if date_str > server_data:
        server_data = date_str
        init_on_day()

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
        print(data.created_at, data.user.screen_name, data.id, data.text)
        for idx, key in enumerate(keywords):
            for word in key:
                if data.text.find(word) != -1:
                    dataset = [data.user.screen_name, data.id, data.text]
                    if not word in datas['menu'].keys():
                        datas['count'][idx] += 1
                        datas['menu'][word] = 1
                    else:
                        datas['menu'][word] += 1
                        datas['count'][idx] += 1
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
    try:
        twit_stream = Stream(auth, listener())
        twit_stream.filter(languages=['ko',], track=track_words, is_async=True)
    except:
        pass
    try:
        global datas
        date_str = datetime.today().strftime("%Y%m%d")
        json_data_file = open("j"+date_str+".json", "r", encoding="utf-8")
        datas = json.loads(json_data_file.read())
    except FileNotFoundError:
        pass

init()
def main(request):   
    return render(request, 'twitterAnal/index.html', {
        'datas' : json.dumps(datas, ensure_ascii=False),
    })

def getData(request):
    data = json.dumps(datas, ensure_ascii=False)
    return HttpResponse(data, content_type='json/application')
