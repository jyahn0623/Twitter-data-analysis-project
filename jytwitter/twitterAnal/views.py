from django.shortcuts import render, HttpResponse
from tweepy import Stream, OAuthHandler
import tweepy
from tweepy.streaming import StreamListener
import json, csv, os
from datetime import datetime
import pandas as pd

files = [
    'd20190401',
    'd20190402',
    'd20190403',
    'd20190404',
    'd20190405',
    'd20190406',
    'd20190407'
]

menu_list = [['짜장면', '탕수육', '짬뽕', '훠궈', '팔보채'],
    ['찌개', '비빔밥', '볶음', '수육', '나물', '국밥'],
    ['우동', '규동', '돈가스', '카레', '초밥', '스시']]

def concat_file(*file_):
    # create empty DataFrame object
    df = pd.DataFrame()
    if type(file_) == tuple:
        file_list = file_[0]
        for index in file_list:
            # concat DataFrame objects
            df = pd.concat([df, pd.read_csv('C:\\Users\\Ahnjuyoung\\Desktop\\twitter\\jytwitter\\datafile/'+index+'.csv', names=['날짜', '닉네임', '트윗번호', '내용'])], \
                ignore_index=True)
    return df

def test(f_name):
    #file_ = open('../datafile/'+f_name+'.csv', 'r', encoding='utf-8')
    #csv = pd.read_csv(file_, names=['날짜', '닉네임', '트윗번호', '내용'])
    #time = pd.to_datetime(csv['날짜'])
    csv = concat_file(f_name)
    datas = {
        'info' : {
            'date' : f_name
        },
        'count' : {
            'total' : [0, 0, 0],
        },
        'data' : {
            
        }
    }
    # item initialize
    for num in range(7):
        datas['data'][num] = {}
    for menu in menu_list:
        for item in menu:
            for num in range(7):
                datas['data'][num][item] = 0
    for hour in csv.iterrows():
        time = None
        try:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S.%f')
        except:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S')
        for idx, menus in enumerate(menu_list):
            for item in menus:
                if str(hour[1][3]).find(item) != -1:
                    datas['count']['total'][idx] += 1
                    datas['data'][time.weekday()][item] += 1
    return datas
    
def main(request):   
    return render(request, 'twitterAnal/index.html')

def getData(request):
    path = os.getcwd()
    datas = {
        'data_days' : json.loads(open(path+'/twitterAnal/요일별1_1.json', 'r').read()),
        'data_times' : json.loads(open(path+'/twitterAnal/시간대별1_1.json', 'r').read()),
        'data_times_by_type' : json.loads(open(path+'/twitterAnal/시간대별1_2.json', 'r').read()),
        'data_days_by_type' : json.loads(open(path+'/twitterAnal/요일별1_2.json', 'r').read()),
        'data_types' : json.loads(open(path+'/twitterAnal/종류별1_2.json', 'r').read())
    }
    return HttpResponse(json.dumps(datas), content_type='application/json')
