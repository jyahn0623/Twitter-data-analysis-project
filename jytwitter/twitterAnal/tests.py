import pandas as pd
from datetime import datetime
import time, json, os
import threading
files = [
    'd20190401',
    'd20190402',
    'd20190403',
    'd20190404',
    'd20190405',
    'd20190406',
    'd20190407',
    'd20190408',
    'd20190409',
    'd20190410',
    'd20190411'
]

menu_list = [['짜장면', '탕수육', '짬뽕', '훠궈', '팔보채'],
    ['찌개', '비빔밥', '볶음', '수육', '나물', '국밥'],
    ['우동', '규동', '돈가스', '카레', '초밥', '스시']]

def avg_process_day(data, t):    
    files_data = []
    day_cnt = [ 0 for n in range(7)]
    for date in files:
        day = date[1:]
        files_data.append(day)

    for day in files_data:
        day_cnt[datetime.strptime(day, "%Y%m%d").weekday()]+=1

    if t == 2:
        for key in data['data'].keys():
            data['data'][key] = [round(val / day_cnt[key], 2) for val in data['data'][key]]
    else:
        for key in data['data'].keys():
            for data_ in data['data'][key]:
                data['data'][key][data_] = round(data['data'][key][data_] / day_cnt[key], 2)
    return data

def avg_process(data, t):
    file_len = len(files)
    if t == 2:
        for key in data['data'].keys():
            data['data'][key] = [round(val / file_len, 2) for val in data['data'][key]]
    else:
        for key in data['data'].keys():
            for data_ in data['data'][key]:
                data['data'][key][data_] = round(data['data'][key][data_] / file_len, 2)
    return data

def concat_file(*file_):
    # create empty DataFrame object
    df = pd.DataFrame()
    if type(file_) == tuple:
        file_list = file_[0]
        for index in file_list:
            # concat DataFrame objects
            df = pd.concat([df, pd.read_csv('../datafile/'+index+'.csv', names=['날짜', '닉네임', '트윗번호', '내용'])], \
                ignore_index=True)
    return df

# 날짜별 데이터 추출
# type : 1 -> 날짜별 항목 데이터 추출 (각각 개별 items)
# type : 2 -> 날짜별 종류 데이터 추출 (한중일식)
def extract_by_date(f_name, type_):
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
            if type_ == 1:
                for num in range(7):
                    datas['data'][num][item] = 0
            else:
                for num in range(7):
                    datas['data'][num]= [0, 0, 0]
    for hour in csv.iterrows():
        time = None
        try:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S.%f')
        except:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S')
        if type_ == 1:
            for idx, menus in enumerate(menu_list):
                for item in menus:
                    if str(hour[1][3]).find(item) != -1:
                        datas['count']['total'][idx] += 1
                        datas['data'][time.weekday()][item] += 1
        else:
            for idx, menus in enumerate(menu_list):
                for item in menus:
                    if str(hour[1][3]).find(item) != -1:
                        datas['count']['total'][idx] += 1
                        datas['data'][time.weekday()][idx] += 1
    return avg_process_day(datas, type_)

# 시간대별 데이터 추출
# type 날짜별과 상동
def extract_by_time(f_name, type_):
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
    for num in range(24):
        datas['data'][num] = {}
    for menu in menu_list:
        for item in menu:
            if type_ == 1:
                for num in range(24):
                    datas['data'][num][item] = 0
            else:
                for num in range(24):
                    datas['data'][num]= [0, 0, 0]
    for hour in csv.iterrows():
        time = None
        try:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S.%f')
        except:
            time = datetime.strptime(hour[1][0], '%Y-%m-%d %H:%M:%S')
        if type_ == 1:
            for idx, menus in enumerate(menu_list):
                for item in menus:
                    if str(hour[1][3]).find(item) != -1:
                        datas['count']['total'][idx] += 1
                        datas['data'][time.hour][item] += 1
        else:
            for idx, menus in enumerate(menu_list):
                for item in menus:
                    if str(hour[1][3]).find(item) != -1:
                        datas['count']['total'][idx] += 1
                        datas['data'][time.hour][idx] += 1           
    return avg_process(datas, type_)


# 총 언급량, 종류별 데이터
def getOverall(files):
    datas = {}
    csv = concat_file(files)
    for d in files: 
        month = d[-4:-2]
        day = d[-2:]
        datas.update({
            '{0}-{1}'.format(month, day) : [0, 0, 0],
        })
        
    for data in csv.iterrows():
        time = None
        try:
            time = datetime.strptime(data[1][0], '%Y-%m-%d %H:%M:%S.%f')
        except:
            time = datetime.strptime(data[1][0], '%Y-%m-%d %H:%M:%S')
        for idx, step in enumerate(menu_list):
            for menu in step:
                if str(data[1][3]).find(menu) != -1:
                    datas['{0}-{1}'.format(str(time.month).zfill(2), str(time.day).zfill(2))][idx] += 1
    return datas

dic = extract_by_time(files, 2)
f = open("시간대별3_2.json", 'w')
f.write(json.dumps(dic))

dic = extract_by_time(files, 1)
f = open("시간대별3_1.json", 'w')
f.write(json.dumps(dic))

dic = extract_by_date(files, 1)
f = open("요일별3_1.json", 'w')
f.write(json.dumps(dic))

dic = extract_by_date(files, 2)
f = open("요일별3_2.json", 'w')
f.write(json.dumps(dic))

dic = getOverall(files)
f = open("종류별3_1.json", 'w')
f.write(json.dumps(dic))

'''
dic = getOverall(files)
print(dic)
_f = open("종류별.json", "w")
_f.write(json.dumps(dic))

#print(dic)
#for f in files:
    #data = test(f)
    #print(data)
'''

