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

# 추출 데이터 및 기초 변수
datas = {}
keywords = ['짜장면', '탕수육', '짬뽕', '찌개', '밥', '비빔밥', '볶음', '팔보채', '훠궈',\
            '돈가스', '우동', '규동', '짜장', '카레']

track_words = ['.', '!', '?', 'ㅋ', '짜장면', '탕수육', '짜장면', '탕수육', '짬뽕', '찌개', '밥', '비빔밥', '볶음', '팔보채', '훠궈',\
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
        print(data.created_at, data.user.screen_name, data.id, data.text)
        for key in keywords:
            if data.text.find(key) != -1:
                dataset = [data.user.screen_name, data.id, data.text]
                #print(datetime.now(), data.user.screen_name, data.id, data.text)
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
'''
# 진입
if __name__ == '__main__':
    auth = OAuthHandler(c_key, c_s_key)
    auth.set_access_token(a_key, a_s_key)
    api = tweepy.API(auth)
    print(api.get_settings())
    for l in api.search("짜장면"):
        print(l.text)
    twit_stream = Stream(auth, listener())
    twit_stream.filter(track=["python"])
'''

def init():
    auth = OAuthHandler(c_key, c_s_key)
    auth.set_access_token(a_key, a_s_key)
    api = tweepy.API(auth)
    twit_stream = Stream(auth, listener())
    twit_stream.filter(languages=['ko',], track=track_words)

def main(request):   
    init()
    return render(request, 'twitterAnal/index.html', {
        'datas' : json.dumps(datas, ensure_ascii=False),
    })

