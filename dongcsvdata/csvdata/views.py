from django.shortcuts import render
import csv
import json
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


# Create your views here.

def datamain(request):
    f1 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190401.csv', 'r', encoding='utf-8')
    f2 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190402.csv', 'r', encoding='utf-8')
    f3 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190403.csv', 'r', encoding='utf-8')
    f4 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190404.csv', 'r', encoding='utf-8')
    f5 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190405.csv', 'r', encoding='utf-8')
    f6 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190406.csv', 'r', encoding='utf-8')
    f7 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190407.csv', 'r', encoding='utf-8')
    f8 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190408.csv', 'r', encoding='utf-8')
    f9 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190409.csv', 'r', encoding='utf-8')
    f10 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190410.csv', 'r', encoding='utf-8')
    f11 = open(r'C:\Users\Ahn\Documents\카카오톡 받은 파일\dongcsvdata\dongcsvdata\csvdata\datafile\d20190411.csv', 'r', encoding='utf-8')

    rdr1 = csv.reader(f1, delimiter=',')
    rdr2 = csv.reader(f2, delimiter=',')
    rdr3 = csv.reader(f3, delimiter=',')
    rdr4 = csv.reader(f4, delimiter=',')
    rdr5 = csv.reader(f5, delimiter=',')
    rdr6 = csv.reader(f6, delimiter=',')
    rdr7 = csv.reader(f7, delimiter=',')
    rdr8 = csv.reader(f8, delimiter=',')
    rdr9 = csv.reader(f9, delimiter=',')
    rdr10 = csv.reader(f10, delimiter=',')
    rdr11 = csv.reader(f11, delimiter=',')

    rdrfin = [rdr1,rdr2,rdr3,rdr4,rdr5,rdr6,rdr7,rdr8,rdr9,rdr10,rdr11]

    #'짜장면', '탕수육', '짬뽕', '훠궈', '팔보채','찌개', '비빔밥', '볶음', '수육', '나물', '국밥','우동', '규동', '돈가스', '카레', '초밥', '스시'
    #메뉴
    datafood01 = []
    datafood02 = []
    datafood03 = []
    datafood04 = []
    datafood05 = []
    datafood06 = []
    datafood07 = []
    datafood08 = []
    datafood09 = []
    datafood10 = []
    datafood11 = []
    datafood12 = []
    datafood13 = []
    datafood14 = []
    datafood15 = []
    datafood16 = []
    datafood17 = []

    #시간대별
    food01datatime00 = []
    food01datatime01 = []
    food01datatime02 = []
    food01datatime03 = []
    food01datatime04 = []
    food01datatime05 = []
    food01datatime06 = []
    food01datatime07 = []
    food01datatime08 = []
    food01datatime09 = []
    food01datatime10 = []
    food01datatime11 = []
    food01datatime12 = []
    food01datatime13 = []
    food01datatime14 = []
    food01datatime15 = []
    food01datatime16 = []
    food01datatime17 = []
    food01datatime18 = []
    food01datatime19 = []
    food01datatime20 = []
    food01datatime21 = []
    food01datatime22 = []
    food01datatime23 = []
    

    food02datatime01 = []
    food02datatime02 = []
    food02datatime03 = []
    food02datatime04 = []
    food02datatime05 = []
    food02datatime06 = []
    food02datatime07 = []
    food02datatime08 = []
    food02datatime09 = []
    food02datatime10 = []
    food02datatime11 = []
    food02datatime12 = []
    food02datatime13 = []
    food02datatime14 = []
    food02datatime15 = []
    food02datatime16 = []
    food02datatime17 = []
    food02datatime18 = []
    food02datatime19 = []
    food02datatime20 = []
    food02datatime21 = []
    food02datatime22 = []
    food02datatime23 = []
    food02datatime00 = []

    food03datatime01 = []
    food03datatime02 = []
    food03datatime03 = []
    food03datatime04 = []
    food03datatime05 = []
    food03datatime06 = []
    food03datatime07 = []
    food03datatime08 = []
    food03datatime09 = []
    food03datatime10 = []
    food03datatime11 = []
    food03datatime12 = []
    food03datatime13 = []
    food03datatime14 = []
    food03datatime15 = []
    food03datatime16 = []
    food03datatime17 = []
    food03datatime18 = []
    food03datatime19 = []
    food03datatime20 = []
    food03datatime21 = []
    food03datatime22 = []
    food03datatime23 = []
    food03datatime00 = []

    food04datatime01 = []
    food04datatime02 = []
    food04datatime03 = []
    food04datatime04 = []
    food04datatime05 = []
    food04datatime06 = []
    food04datatime07 = []
    food04datatime08 = []
    food04datatime09 = []
    food04datatime10 = []
    food04datatime11 = []
    food04datatime12 = []
    food04datatime13 = []
    food04datatime14 = []
    food04datatime15 = []
    food04datatime16 = []
    food04datatime17 = []
    food04datatime18 = []
    food04datatime19 = []
    food04datatime20 = []
    food04datatime21 = []
    food04datatime22 = []
    food04datatime23 = []
    food04datatime00 = []

    food05datatime01 = []
    food05datatime02 = []
    food05datatime03 = []
    food05datatime04 = []
    food05datatime05 = []
    food05datatime06 = []
    food05datatime07 = []
    food05datatime08 = []
    food05datatime09 = []
    food05datatime10 = []
    food05datatime11 = []
    food05datatime12 = []
    food05datatime13 = []
    food05datatime14 = []
    food05datatime15 = []
    food05datatime16 = []
    food05datatime17 = []
    food05datatime18 = []
    food05datatime19 = []
    food05datatime20 = []
    food05datatime21 = []
    food05datatime22 = []
    food05datatime23 = []
    food05datatime00 = []

    food06datatime01 = []
    food06datatime02 = []
    food06datatime03 = []
    food06datatime04 = []
    food06datatime05 = []
    food06datatime06 = []
    food06datatime07 = []
    food06datatime08 = []
    food06datatime09 = []
    food06datatime10 = []
    food06datatime11 = []
    food06datatime12 = []
    food06datatime13 = []
    food06datatime14 = []
    food06datatime15 = []
    food06datatime16 = []
    food06datatime17 = []
    food06datatime18 = []
    food06datatime19 = []
    food06datatime20 = []
    food06datatime21 = []
    food06datatime22 = []
    food06datatime23 = []
    food06datatime00 = []

    food07datatime01 = []
    food07datatime02 = []
    food07datatime03 = []
    food07datatime04 = []
    food07datatime05 = []
    food07datatime06 = []
    food07datatime07 = []
    food07datatime08 = []
    food07datatime09 = []
    food07datatime10 = []
    food07datatime11 = []
    food07datatime12 = []
    food07datatime13 = []
    food07datatime14 = []
    food07datatime15 = []
    food07datatime16 = []
    food07datatime17 = []
    food07datatime18 = []
    food07datatime19 = []
    food07datatime20 = []
    food07datatime21 = []
    food07datatime22 = []
    food07datatime23 = []
    food07datatime00 = []

    food08datatime01 = []
    food08datatime02 = []
    food08datatime03 = []
    food08datatime04 = []
    food08datatime05 = []
    food08datatime06 = []
    food08datatime07 = []
    food08datatime08 = []
    food08datatime09 = []
    food08datatime10 = []
    food08datatime11 = []
    food08datatime12 = []
    food08datatime13 = []
    food08datatime14 = []
    food08datatime15 = []
    food08datatime16 = []
    food08datatime17 = []
    food08datatime18 = []
    food08datatime19 = []
    food08datatime20 = []
    food08datatime21 = []
    food08datatime22 = []
    food08datatime23 = []
    food08datatime00 = []

    food09datatime01 = []
    food09datatime02 = []
    food09datatime03 = []
    food09datatime04 = []
    food09datatime05 = []
    food09datatime06 = []
    food09datatime07 = []
    food09datatime08 = []
    food09datatime09 = []
    food09datatime10 = []
    food09datatime11 = []
    food09datatime12 = []
    food09datatime13 = []
    food09datatime14 = []
    food09datatime15 = []
    food09datatime16 = []
    food09datatime17 = []
    food09datatime18 = []
    food09datatime19 = []
    food09datatime20 = []
    food09datatime21 = []
    food09datatime22 = []
    food09datatime23 = []
    food09datatime00 = []

    food10datatime01 = []
    food10datatime02 = []
    food10datatime03 = []
    food10datatime04 = []
    food10datatime05 = []
    food10datatime06 = []
    food10datatime07 = []
    food10datatime08 = []
    food10datatime09 = []
    food10datatime10 = []
    food10datatime11 = []
    food10datatime12 = []
    food10datatime13 = []
    food10datatime14 = []
    food10datatime15 = []
    food10datatime16 = []
    food10datatime17 = []
    food10datatime18 = []
    food10datatime19 = []
    food10datatime20 = []
    food10datatime21 = []
    food10datatime22 = []
    food10datatime23 = []
    food10datatime00 = []

    food11datatime01 = []
    food11datatime02 = []
    food11datatime03 = []
    food11datatime04 = []
    food11datatime05 = []
    food11datatime06 = []
    food11datatime07 = []
    food11datatime08 = []
    food11datatime09 = []
    food11datatime10 = []
    food11datatime11 = []
    food11datatime12 = []
    food11datatime13 = []
    food11datatime14 = []
    food11datatime15 = []
    food11datatime16 = []
    food11datatime17 = []
    food11datatime18 = []
    food11datatime19 = []
    food11datatime20 = []
    food11datatime21 = []
    food11datatime22 = []
    food11datatime23 = []
    food11datatime00 = []

    food12datatime01 = []
    food12datatime02 = []
    food12datatime03 = []
    food12datatime04 = []
    food12datatime05 = []
    food12datatime06 = []
    food12datatime07 = []
    food12datatime08 = []
    food12datatime09 = []
    food12datatime10 = []
    food12datatime11 = []
    food12datatime12 = []
    food12datatime13 = []
    food12datatime14 = []
    food12datatime15 = []
    food12datatime16 = []
    food12datatime17 = []
    food12datatime18 = []
    food12datatime19 = []
    food12datatime20 = []
    food12datatime21 = []
    food12datatime22 = []
    food12datatime23 = []
    food12datatime00 = []

    food13datatime01 = []
    food13datatime02 = []
    food13datatime03 = []
    food13datatime04 = []
    food13datatime05 = []
    food13datatime06 = []
    food13datatime07 = []
    food13datatime08 = []
    food13datatime09 = []
    food13datatime10 = []
    food13datatime11 = []
    food13datatime12 = []
    food13datatime13 = []
    food13datatime14 = []
    food13datatime15 = []
    food13datatime16 = []
    food13datatime17 = []
    food13datatime18 = []
    food13datatime19 = []
    food13datatime20 = []
    food13datatime21 = []
    food13datatime22 = []
    food13datatime23 = []
    food13datatime00 = []

    food14datatime01 = []
    food14datatime02 = []
    food14datatime03 = []
    food14datatime04 = []
    food14datatime05 = []
    food14datatime06 = []
    food14datatime07 = []
    food14datatime08 = []
    food14datatime09 = []
    food14datatime10 = []
    food14datatime11 = []
    food14datatime12 = []
    food14datatime13 = []
    food14datatime14 = []
    food14datatime15 = []
    food14datatime16 = []
    food14datatime17 = []
    food14datatime18 = []
    food14datatime19 = []
    food14datatime20 = []
    food14datatime21 = []
    food14datatime22 = []
    food14datatime23 = []
    food14datatime00 = []

    food15datatime01 = []
    food15datatime02 = []
    food15datatime03 = []
    food15datatime04 = []
    food15datatime05 = []
    food15datatime06 = []
    food15datatime07 = []
    food15datatime08 = []
    food15datatime09 = []
    food15datatime10 = []
    food15datatime11 = []
    food15datatime12 = []
    food15datatime13 = []
    food15datatime14 = []
    food15datatime15 = []
    food15datatime16 = []
    food15datatime17 = []
    food15datatime18 = []
    food15datatime19 = []
    food15datatime20 = []
    food15datatime21 = []
    food15datatime22 = []
    food15datatime23 = []
    food15datatime00 = []

    food16datatime01 = []
    food16datatime02 = []
    food16datatime03 = []
    food16datatime04 = []
    food16datatime05 = []
    food16datatime06 = []
    food16datatime07 = []
    food16datatime08 = []
    food16datatime09 = []
    food16datatime10 = []
    food16datatime11 = []
    food16datatime12 = []
    food16datatime13 = []
    food16datatime14 = []
    food16datatime15 = []
    food16datatime16 = []
    food16datatime17 = []
    food16datatime18 = []
    food16datatime19 = []
    food16datatime20 = []
    food16datatime21 = []
    food16datatime22 = []
    food16datatime23 = []
    food16datatime00 = []

    food17datatime01 = []
    food17datatime02 = []
    food17datatime03 = []
    food17datatime04 = []
    food17datatime05 = []
    food17datatime06 = []
    food17datatime07 = []
    food17datatime08 = []
    food17datatime09 = []
    food17datatime10 = []
    food17datatime11 = []
    food17datatime12 = []
    food17datatime13 = []
    food17datatime14 = []
    food17datatime15 = []
    food17datatime16 = []
    food17datatime17 = []
    food17datatime18 = []
    food17datatime19 = []
    food17datatime20 = []
    food17datatime21 = []
    food17datatime22 = []
    food17datatime23 = []
    food17datatime00 = []
    
    food01time = [food01datatime00, food01datatime01, food01datatime02, food01datatime03, food01datatime04, food01datatime05, food01datatime06, food01datatime07,
                    food01datatime08, food01datatime09, food01datatime10, food01datatime11, food01datatime12, food01datatime13, food01datatime14,
                    food01datatime15, food01datatime16, food01datatime17, food01datatime18, food01datatime19, food01datatime20, food01datatime21,
                    food01datatime22, food01datatime23]
    
    food02time = [food02datatime00, food02datatime01, food02datatime02, food02datatime03, food02datatime04, food02datatime05, food02datatime06, food02datatime07,
                    food02datatime08, food02datatime09, food02datatime10, food02datatime11, food02datatime12, food02datatime13, food02datatime14,
                    food02datatime15, food02datatime16, food02datatime17, food02datatime18, food02datatime19, food02datatime20, food02datatime21,
                    food02datatime22, food02datatime23]

    food03time = [food03datatime00, food03datatime01, food03datatime02, food03datatime03, food03datatime04, food03datatime05, food03datatime06, food03datatime07,
                    food03datatime08, food03datatime09, food03datatime10, food03datatime11, food03datatime12, food03datatime13, food03datatime14,
                    food03datatime15, food03datatime16, food03datatime17, food03datatime18, food03datatime19, food03datatime20, food03datatime21,
                    food03datatime22, food03datatime23 ]
    
    food04time = [food04datatime00,food04datatime01, food04datatime02, food04datatime03, food04datatime04, food04datatime05, food04datatime06, food04datatime07,
                    food04datatime08, food04datatime09, food04datatime10, food04datatime11, food04datatime12, food04datatime13, food04datatime14,
                    food04datatime15, food04datatime16, food04datatime17, food04datatime18, food04datatime19, food04datatime20, food04datatime21,
                    food04datatime22, food04datatime23]
    
    food05time = [food05datatime00, food05datatime01, food05datatime02, food05datatime03, food05datatime04, food05datatime05, food05datatime06, food05datatime07,
                    food05datatime08, food05datatime09, food05datatime10, food05datatime11, food05datatime12, food05datatime13, food05datatime14,
                    food05datatime15, food05datatime16, food05datatime17, food05datatime18, food05datatime19, food05datatime20, food05datatime21,
                    food05datatime22, food05datatime23 ]
    
    food06time = [food06datatime00, food06datatime01, food06datatime02, food06datatime03, food06datatime04, food06datatime05, food06datatime06, food06datatime07,
                    food06datatime08, food06datatime09, food06datatime10, food06datatime11, food06datatime12, food06datatime13, food06datatime14,
                    food06datatime15, food06datatime16, food06datatime17, food06datatime18, food06datatime19, food06datatime20, food06datatime21,
                    food06datatime22, food06datatime23]

    food07time = [food07datatime00, food07datatime01, food07datatime02, food07datatime03, food07datatime04, food07datatime05, food07datatime06, food07datatime07,
                    food07datatime08, food07datatime09, food07datatime10, food07datatime11, food07datatime12, food07datatime13, food07datatime14,
                    food07datatime15, food07datatime16, food07datatime17, food07datatime18, food07datatime19, food07datatime20, food07datatime21,
                    food07datatime22, food07datatime23]
    
    food08time = [food08datatime00, food08datatime01, food08datatime02, food08datatime03, food08datatime04, food08datatime05, food08datatime06, food08datatime07,
                    food08datatime08, food08datatime09, food08datatime10, food08datatime11, food08datatime12, food08datatime13, food08datatime14,
                    food08datatime15, food08datatime16, food08datatime17, food08datatime18, food08datatime19, food08datatime20, food08datatime21,
                    food08datatime22, food08datatime23 ]

    food09time = [food09datatime00, food09datatime01, food09datatime02, food09datatime03, food09datatime04, food09datatime05, food09datatime06, food09datatime07,
                    food09datatime08, food09datatime09, food09datatime10, food09datatime11, food09datatime12, food09datatime13, food09datatime14,
                    food09datatime15, food09datatime16, food09datatime17, food09datatime18, food09datatime19, food09datatime20, food09datatime21,
                    food09datatime22, food09datatime23]
    
    food10time = [food10datatime00, food10datatime01, food10datatime02, food10datatime03, food10datatime04, food10datatime05, food10datatime06, food10datatime07,
                    food10datatime08, food10datatime09, food10datatime10, food10datatime11, food10datatime12, food10datatime13, food10datatime14,
                    food10datatime15, food10datatime16, food10datatime17, food10datatime18, food10datatime19, food10datatime20, food10datatime21,
                    food10datatime22, food10datatime23]
    
    food11time = [food11datatime00, food11datatime01, food11datatime02, food11datatime03, food11datatime04, food11datatime05, food11datatime06, food11datatime07,
                    food11datatime08, food11datatime09, food11datatime10, food11datatime11, food11datatime12, food11datatime13, food11datatime14,
                    food11datatime15, food11datatime16, food11datatime17, food11datatime18, food11datatime19, food11datatime20, food11datatime21,
                    food11datatime22, food11datatime23]
    
    food12time = [food12datatime00, food12datatime01, food12datatime02, food12datatime03, food12datatime04, food12datatime05, food12datatime06, food12datatime07,
                    food12datatime08, food12datatime09, food12datatime10, food12datatime11, food12datatime12, food12datatime13, food12datatime14,
                    food12datatime15, food12datatime16, food12datatime17, food12datatime18, food12datatime19, food12datatime20, food12datatime21,
                    food12datatime22, food12datatime23]
    
    food13time = [food13datatime00, food13datatime01, food13datatime02, food13datatime03, food13datatime04, food13datatime05, food13datatime06, food13datatime07,
                    food13datatime08, food13datatime09, food13datatime10, food13datatime11, food13datatime12, food13datatime13, food13datatime14,
                    food13datatime15, food13datatime16, food13datatime17, food13datatime18, food13datatime19, food13datatime20, food13datatime21,
                    food13datatime22, food13datatime23]
    
    food14time = [food14datatime00,food14datatime01, food14datatime02, food14datatime03, food14datatime04, food14datatime05, food14datatime06, food14datatime07,
                    food14datatime08, food14datatime09, food14datatime10, food14datatime11, food14datatime12, food14datatime13, food14datatime14,
                    food14datatime15, food14datatime16, food14datatime17, food14datatime18, food14datatime19, food14datatime20, food14datatime21,
                    food14datatime22, food14datatime23]

    food15time = [food15datatime00, food15datatime01, food15datatime02, food15datatime03, food15datatime04, food15datatime05, food15datatime06, food15datatime07,
                    food15datatime08, food15datatime09, food15datatime10, food15datatime11, food15datatime12, food15datatime13, food15datatime14,
                    food15datatime15, food15datatime16, food15datatime17, food15datatime18, food15datatime19, food15datatime20, food15datatime21,
                    food15datatime22, food15datatime23]
    
    food16time = [food16datatime00,food16datatime01, food16datatime02, food16datatime03, food16datatime04, food16datatime05, food16datatime06, food16datatime07,
                    food16datatime08, food16datatime09, food16datatime10, food16datatime11, food16datatime12, food16datatime13, food16datatime14,
                    food16datatime15, food16datatime16, food16datatime17, food16datatime18, food16datatime19, food16datatime20, food16datatime21,
                    food16datatime22, food16datatime23]
    
    food17time = [food17datatime00, food17datatime01, food17datatime02, food17datatime03, food17datatime04, food17datatime05, food17datatime06, food17datatime07,
                    food17datatime08, food17datatime09, food17datatime10, food17datatime11, food17datatime12, food17datatime13, food17datatime14,
                    food17datatime15, food17datatime16, food17datatime17, food17datatime18, food17datatime19, food17datatime20, food17datatime21,
                    food17datatime22, food17datatime23]

    #종류별 시간대별 단어수

    #중식 '짜장면', '탕수육', '짬뽕', '훠궈', '팔보채',
    #한식 '찌개', '비빔밥', '볶음', '수육', '나물', '국밥',
    #일식 '우동', '규동', '돈가스', '카레', '초밥', '스시'
    

    for line in rdrfin:
        for dataline in line:
            data = '\t'.join(dataline)
            data1 = data.split(' ')
            if '짜장면' in data1:
                datafood01.append(data1)
            if '탕수육' in data1:
                datafood02.append(data1)
            if "짬뽕" in data1:
                datafood03.append(data1)
            if "훠궈" in data1:
                datafood04.append(data1)
            if "팔보채" in data1:
                datafood05.append(data1)
            if "찌개" in data1:
                datafood06.append(data1)
            if "비빔밥" in data1:
                datafood07.append(data1)
            if "볶음" in data1:
                datafood08.append(data1)
            if "수육" in data1:
                datafood09.append(data1)
            if "나물" in data1:
                datafood10.append(data1)
            if "국밥" in data1:
                datafood11.append(data1)
            if "우동" in data1:
                datafood12.append(data1)
            if "규동" in data1:
                datafood13.append(data1)
            if "돈가스" in data1:
                datafood14.append(data1)
            if "카레" in data1:
                datafood15.append(data1)
            if "초밥" in data1:
                datafood16.append(data1)
            if "스시" in data1:
                datafood17.append(data1)
    
    datafood = [datafood01,datafood02, datafood03, datafood04, datafood05,
                datafood06, datafood07, datafood08, datafood09, datafood10,
                datafood11, datafood12, datafood13, datafood14, datafood15, datafood16, datafood17]
    
    for datafoodset in datafood:
        for datatimeset in datafoodset:
            time = datatimeset[1][0:2]
            if time == '00':
                if '짜장면' in datatimeset:
                    food01time[0].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[0].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[0].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[0].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[0].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[0].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[0].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[0].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[0].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[0].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[0].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[0].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[0].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[0].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[0].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[0].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[0].append(datatimeset)

            if time == '01':
                if '짜장면' in datatimeset:
                    food01time[1].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[1].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[1].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[1].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[1].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[1].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[1].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[1].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[1].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[1].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[1].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[1].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[1].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[1].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[1].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[1].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[1].append(datatimeset)

            if time == '02':
                if '짜장면' in datatimeset:
                    food01time[2].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[2].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[2].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[2].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[2].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[2].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[2].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[2].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[2].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[2].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[2].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[2].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[2].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[2].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[2].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[2].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[2].append(datatimeset)

            if time == '03':
                if '짜장면' in datatimeset:
                    food01time[3].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[3].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[3].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[3].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[3].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[3].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[3].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[3].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[3].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[3].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[3].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[3].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[3].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[3].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[3].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[3].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[3].append(datatimeset)

            if time == '04':
                if '짜장면' in datatimeset:
                    food01time[4].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[4].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[4].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[4].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[4].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[4].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[4].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[4].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[4].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[4].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[4].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[4].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[4].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[4].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[4].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[4].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[4].append(datatimeset)

            if time == '05':
                if '짜장면' in datatimeset:
                    food01time[5].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[5].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[5].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[5].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[5].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[5].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[5].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[5].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[5].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[5].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[5].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[5].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[5].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[5].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[5].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[5].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[5].append(datatimeset)

            if time == '06':
                if '짜장면' in datatimeset:
                    food01time[6].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[6].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[6].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[6].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[6].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[6].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[6].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[6].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[6].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[6].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[6].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[6].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[6].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[6].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[6].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[6].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[6].append(datatimeset)

            if time == '07':
                if '짜장면' in datatimeset:
                    food01time[7].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[7].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[7].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[7].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[7].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[7].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[7].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[7].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[7].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[7].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[7].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[7].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[7].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[7].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[7].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[7].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[7].append(datatimeset)

            if time == '08':
                if '짜장면' in datatimeset:
                    food01time[8].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[8].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[8].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[8].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[8].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[8].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[8].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[8].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[8].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[8].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[8].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[8].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[8].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[8].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[8].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[8].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[8].append(datatimeset)

            if time == '09':
                if '짜장면' in datatimeset:
                    food01time[9].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[9].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[9].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[9].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[9].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[9].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[9].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[9].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[9].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[9].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[9].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[9].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[9].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[9].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[9].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[9].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[9].append(datatimeset)

            if time == '10':
                if '짜장면' in datatimeset:
                    food01time[10].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[10].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[10].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[10].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[10].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[10].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[10].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[10].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[10].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[10].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[10].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[10].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[10].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[10].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[10].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[10].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[10].append(datatimeset)

            if time == '11':
                if '짜장면' in datatimeset:
                    food01time[11].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[11].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[11].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[11].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[11].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[11].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[11].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[11].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[11].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[11].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[11].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[11].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[11].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[11].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[11].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[11].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[11].append(datatimeset)

            if time == '12':
                if '짜장면' in datatimeset:
                    food01time[12].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[12].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[12].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[12].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[12].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[12].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[12].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[12].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[12].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[12].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[12].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[12].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[12].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[12].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[12].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[12].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[12].append(datatimeset)

            if time == '13':
                if '짜장면' in datatimeset:
                    food01time[13].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[13].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[13].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[13].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[13].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[13].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[13].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[13].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[13].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[13].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[13].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[13].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[13].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[13].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[13].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[13].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[13].append(datatimeset)

            if time == '14':
                if '짜장면' in datatimeset:
                    food01time[14].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[14].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[14].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[14].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[14].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[14].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[14].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[14].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[14].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[14].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[14].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[14].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[14].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[14].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[14].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[14].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[14].append(datatimeset)

            if time == '15':
                if '짜장면' in datatimeset:
                    food01time[15].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[15].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[15].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[15].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[15].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[15].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[15].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[15].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[15].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[15].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[15].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[15].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[15].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[15].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[15].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[15].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[15].append(datatimeset)

            if time == '16':
                if '짜장면' in datatimeset:
                    food01time[16].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[16].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[16].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[16].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[16].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[16].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[16].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[16].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[16].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[16].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[16].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[16].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[16].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[16].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[16].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[16].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[16].append(datatimeset)

            if time == '17':
                if '짜장면' in datatimeset:
                    food01time[17].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[17].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[17].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[17].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[17].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[17].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[17].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[17].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[17].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[17].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[17].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[17].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[17].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[17].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[17].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[17].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[17].append(datatimeset)

            if time == '18':
                if '짜장면' in datatimeset:
                    food01time[18].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[18].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[18].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[18].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[18].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[18].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[18].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[18].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[18].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[18].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[18].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[18].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[18].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[18].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[18].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[18].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[18].append(datatimeset)

            if time == '19':
                if '짜장면' in datatimeset:
                    food01time[19].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[19].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[19].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[19].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[19].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[19].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[19].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[19].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[19].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[19].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[19].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[19].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[19].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[19].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[19].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[19].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[19].append(datatimeset)

            if time == '20':
                if '짜장면' in datatimeset:
                    food01time[20].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[20].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[20].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[20].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[20].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[20].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[20].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[20].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[20].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[20].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[20].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[20].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[20].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[20].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[20].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[20].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[20].append(datatimeset)

            if time == '21':
                if '짜장면' in datatimeset:
                    food01time[21].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[21].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[21].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[21].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[21].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[21].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[21].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[21].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[21].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[21].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[21].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[21].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[21].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[21].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[21].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[21].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[21].append(datatimeset)

            if time == '22':
                if '짜장면' in datatimeset:
                    food01time[22].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[22].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[22].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[22].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[22].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[22].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[22].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[22].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[22].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[22].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[22].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[22].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[22].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[22].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[22].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[22].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[22].append(datatimeset)

            if time == '23':
                if '짜장면' in datatimeset:
                    food01time[23].append(datatimeset)
                if '탕수육' in datatimeset:
                    food02time[23].append(datatimeset)
                if '짬뽕' in datatimeset:
                    food03time[23].append(datatimeset)
                if '훠궈' in datatimeset:
                    food04time[23].append(datatimeset)
                if '팔보채' in datatimeset:
                    food05time[23].append(datatimeset)
                if '찌개' in datatimeset:
                    food06time[23].append(datatimeset)
                if '비빔밥' in datatimeset:
                    food07time[23].append(datatimeset)
                if '볶음' in datatimeset:
                    food08time[23].append(datatimeset)
                if '수육' in datatimeset:
                    food09time[23].append(datatimeset)
                if '나물' in datatimeset:
                    food10time[23].append(datatimeset)
                if '국밥' in datatimeset:
                    food11time[23].append(datatimeset)
                if '우동' in datatimeset:
                    food12time[23].append(datatimeset)
                if '규동' in datatimeset:
                    food13time[23].append(datatimeset)
                if '돈가스' in datatimeset:
                    food14time[23].append(datatimeset)
                if '카레' in datatimeset:
                    food15time[23].append(datatimeset)
                if '초밥' in datatimeset:
                    food16time[23].append(datatimeset)
                if '스시' in datatimeset:
                    food17time[23].append(datatimeset)

    count = 0

    food01datasum00 = 0
    food01datasum01 = 0
    food01datasum02 = 0
    food01datasum03 = 0
    food01datasum04 = 0
    food01datasum05 = 0
    food01datasum06 = 0
    food01datasum07 = 0
    food01datasum08 = 0
    food01datasum09 = 0
    food01datasum10 = 0
    food01datasum11 = 0
    food01datasum12 = 0
    food01datasum13 = 0
    food01datasum14 = 0
    food01datasum15 = 0
    food01datasum16 = 0
    food01datasum17 = 0
    food01datasum18 = 0
    food01datasum19 = 0
    food01datasum20 = 0
    food01datasum21 = 0
    food01datasum22 = 0
    food01datasum23 = 0
    
    food02datasum00 = 0
    food02datasum01 = 0
    food02datasum02 = 0
    food02datasum03 = 0
    food02datasum04 = 0
    food02datasum05 = 0
    food02datasum06 = 0
    food02datasum07 = 0
    food02datasum08 = 0
    food02datasum09 = 0
    food02datasum10 = 0
    food02datasum11 = 0
    food02datasum12 = 0
    food02datasum13 = 0
    food02datasum14 = 0
    food02datasum15 = 0
    food02datasum16 = 0
    food02datasum17 = 0
    food02datasum18 = 0
    food02datasum19 = 0
    food02datasum20 = 0
    food02datasum21 = 0
    food02datasum22 = 0
    food02datasum23 = 0
    
    food03datasum00 = 0
    food03datasum01 = 0
    food03datasum02 = 0
    food03datasum03 = 0
    food03datasum04 = 0
    food03datasum05 = 0
    food03datasum06 = 0
    food03datasum07 = 0
    food03datasum08 = 0
    food03datasum09 = 0
    food03datasum10 = 0
    food03datasum11 = 0
    food03datasum12 = 0
    food03datasum13 = 0
    food03datasum14 = 0
    food03datasum15 = 0
    food03datasum16 = 0
    food03datasum17 = 0
    food03datasum18 = 0
    food03datasum19 = 0
    food03datasum20 = 0
    food03datasum21 = 0
    food03datasum22 = 0
    food03datasum23 = 0

    food04datasum00 = 0
    food04datasum01 = 0
    food04datasum02 = 0
    food04datasum03 = 0
    food04datasum04 = 0
    food04datasum05 = 0
    food04datasum06 = 0
    food04datasum07 = 0
    food04datasum08 = 0
    food04datasum09 = 0
    food04datasum10 = 0
    food04datasum11 = 0
    food04datasum12 = 0
    food04datasum13 = 0
    food04datasum14 = 0
    food04datasum15 = 0
    food04datasum16 = 0
    food04datasum17 = 0
    food04datasum18 = 0
    food04datasum19 = 0
    food04datasum20 = 0
    food04datasum21 = 0
    food04datasum22 = 0
    food04datasum23 = 0

    food05datasum00 = 0
    food05datasum01 = 0
    food05datasum02 = 0
    food05datasum03 = 0
    food05datasum04 = 0
    food05datasum05 = 0
    food05datasum06 = 0
    food05datasum07 = 0
    food05datasum08 = 0
    food05datasum09 = 0
    food05datasum10 = 0
    food05datasum11 = 0
    food05datasum12 = 0
    food05datasum13 = 0
    food05datasum14 = 0
    food05datasum15 = 0
    food05datasum16 = 0
    food05datasum17 = 0
    food05datasum18 = 0
    food05datasum19 = 0
    food05datasum20 = 0
    food05datasum21 = 0
    food05datasum22 = 0
    food05datasum23 = 0

    food06datasum00 = 0
    food06datasum01 = 0
    food06datasum02 = 0
    food06datasum03 = 0
    food06datasum04 = 0
    food06datasum05 = 0
    food06datasum06 = 0
    food06datasum07 = 0
    food06datasum08 = 0
    food06datasum09 = 0
    food06datasum10 = 0
    food06datasum11 = 0
    food06datasum12 = 0
    food06datasum13 = 0
    food06datasum14 = 0
    food06datasum15 = 0
    food06datasum16 = 0
    food06datasum17 = 0
    food06datasum18 = 0
    food06datasum19 = 0
    food06datasum20 = 0
    food06datasum21 = 0
    food06datasum22 = 0
    food06datasum23 = 0

    food07datasum00 = 0
    food07datasum01 = 0
    food07datasum02 = 0
    food07datasum03 = 0
    food07datasum04 = 0
    food07datasum05 = 0
    food07datasum06 = 0
    food07datasum07 = 0
    food07datasum08 = 0
    food07datasum09 = 0
    food07datasum10 = 0
    food07datasum11 = 0
    food07datasum12 = 0
    food07datasum13 = 0
    food07datasum14 = 0
    food07datasum15 = 0
    food07datasum16 = 0
    food07datasum17 = 0
    food07datasum18 = 0
    food07datasum19 = 0
    food07datasum20 = 0
    food07datasum21 = 0
    food07datasum22 = 0
    food07datasum23 = 0

    food08datasum00 = 0
    food08datasum01 = 0
    food08datasum02 = 0
    food08datasum03 = 0
    food08datasum04 = 0
    food08datasum05 = 0
    food08datasum06 = 0
    food08datasum07 = 0
    food08datasum08 = 0
    food08datasum09 = 0
    food08datasum10 = 0
    food08datasum11 = 0
    food08datasum12 = 0
    food08datasum13 = 0
    food08datasum14 = 0
    food08datasum15 = 0
    food08datasum16 = 0
    food08datasum17 = 0
    food08datasum18 = 0
    food08datasum19 = 0
    food08datasum20 = 0
    food08datasum21 = 0
    food08datasum22 = 0
    food08datasum23 = 0

    food09datasum00 = 0
    food09datasum01 = 0
    food09datasum02 = 0
    food09datasum03 = 0
    food09datasum04 = 0
    food09datasum05 = 0
    food09datasum06 = 0
    food09datasum07 = 0
    food09datasum08 = 0
    food09datasum09 = 0
    food09datasum10 = 0
    food09datasum11 = 0
    food09datasum12 = 0
    food09datasum13 = 0
    food09datasum14 = 0
    food09datasum15 = 0
    food09datasum16 = 0
    food09datasum17 = 0
    food09datasum18 = 0
    food09datasum19 = 0
    food09datasum20 = 0
    food09datasum21 = 0
    food09datasum22 = 0
    food09datasum23 = 0

    food10datasum00 = 0
    food10datasum01 = 0
    food10datasum02 = 0
    food10datasum03 = 0
    food10datasum04 = 0
    food10datasum05 = 0
    food10datasum06 = 0
    food10datasum07 = 0
    food10datasum08 = 0
    food10datasum09 = 0
    food10datasum10 = 0
    food10datasum11 = 0
    food10datasum12 = 0
    food10datasum13 = 0
    food10datasum14 = 0
    food10datasum15 = 0
    food10datasum16 = 0
    food10datasum17 = 0
    food10datasum18 = 0
    food10datasum19 = 0
    food10datasum20 = 0
    food10datasum21 = 0
    food10datasum22 = 0
    food10datasum23 = 0

    food11datasum00 = 0
    food11datasum01 = 0
    food11datasum02 = 0
    food11datasum03 = 0
    food11datasum04 = 0
    food11datasum05 = 0
    food11datasum06 = 0
    food11datasum07 = 0
    food11datasum08 = 0
    food11datasum09 = 0
    food11datasum10 = 0
    food11datasum11 = 0
    food11datasum12 = 0
    food11datasum13 = 0
    food11datasum14 = 0
    food11datasum15 = 0
    food11datasum16 = 0
    food11datasum17 = 0
    food11datasum18 = 0
    food11datasum19 = 0
    food11datasum20 = 0
    food11datasum21 = 0
    food11datasum22 = 0
    food11datasum23 = 0

    food12datasum00 = 0
    food12datasum01 = 0
    food12datasum02 = 0
    food12datasum03 = 0
    food12datasum04 = 0
    food12datasum05 = 0
    food12datasum06 = 0
    food12datasum07 = 0
    food12datasum08 = 0
    food12datasum09 = 0
    food12datasum10 = 0
    food12datasum11 = 0
    food12datasum12 = 0
    food12datasum13 = 0
    food12datasum14 = 0
    food12datasum15 = 0
    food12datasum16 = 0
    food12datasum17 = 0
    food12datasum18 = 0
    food12datasum19 = 0
    food12datasum20 = 0
    food12datasum21 = 0
    food12datasum22 = 0
    food12datasum23 = 0

    food13datasum00 = 0
    food13datasum01 = 0
    food13datasum02 = 0
    food13datasum03 = 0
    food13datasum04 = 0
    food13datasum05 = 0
    food13datasum06 = 0
    food13datasum07 = 0
    food13datasum08 = 0
    food13datasum09 = 0
    food13datasum10 = 0
    food13datasum11 = 0
    food13datasum12 = 0
    food13datasum13 = 0
    food13datasum14 = 0
    food13datasum15 = 0
    food13datasum16 = 0
    food13datasum17 = 0
    food13datasum18 = 0
    food13datasum19 = 0
    food13datasum20 = 0
    food13datasum21 = 0
    food13datasum22 = 0
    food13datasum23 = 0

    food14datasum00 = 0
    food14datasum01 = 0
    food14datasum02 = 0
    food14datasum03 = 0
    food14datasum04 = 0
    food14datasum05 = 0
    food14datasum06 = 0
    food14datasum07 = 0
    food14datasum08 = 0
    food14datasum09 = 0
    food14datasum10 = 0
    food14datasum11 = 0
    food14datasum12 = 0
    food14datasum13 = 0
    food14datasum14 = 0
    food14datasum15 = 0
    food14datasum16 = 0
    food14datasum17 = 0
    food14datasum18 = 0
    food14datasum19 = 0
    food14datasum20 = 0
    food14datasum21 = 0
    food14datasum22 = 0
    food14datasum23 = 0

    food15datasum00 = 0
    food15datasum01 = 0
    food15datasum02 = 0
    food15datasum03 = 0
    food15datasum04 = 0
    food15datasum05 = 0
    food15datasum06 = 0
    food15datasum07 = 0
    food15datasum08 = 0
    food15datasum09 = 0
    food15datasum10 = 0
    food15datasum11 = 0
    food15datasum12 = 0
    food15datasum13 = 0
    food15datasum14 = 0
    food15datasum15 = 0
    food15datasum16 = 0
    food15datasum17 = 0
    food15datasum18 = 0
    food15datasum19 = 0
    food15datasum20 = 0
    food15datasum21 = 0
    food15datasum22 = 0
    food15datasum23 = 0

    food16datasum00 = 0
    food16datasum01 = 0
    food16datasum02 = 0
    food16datasum03 = 0
    food16datasum04 = 0
    food16datasum05 = 0
    food16datasum06 = 0
    food16datasum07 = 0
    food16datasum08 = 0
    food16datasum09 = 0
    food16datasum10 = 0
    food16datasum11 = 0
    food16datasum12 = 0
    food16datasum13 = 0
    food16datasum14 = 0
    food16datasum15 = 0
    food16datasum16 = 0
    food16datasum17 = 0
    food16datasum18 = 0
    food16datasum19 = 0
    food16datasum20 = 0
    food16datasum21 = 0
    food16datasum22 = 0
    food16datasum23 = 0

    food17datasum00 = 0
    food17datasum01 = 0
    food17datasum02 = 0
    food17datasum03 = 0
    food17datasum04 = 0
    food17datasum05 = 0
    food17datasum06 = 0
    food17datasum07 = 0
    food17datasum08 = 0
    food17datasum09 = 0
    food17datasum10 = 0
    food17datasum11 = 0
    food17datasum12 = 0
    food17datasum13 = 0
    food17datasum14 = 0
    food17datasum15 = 0
    food17datasum16 = 0
    food17datasum17 = 0
    food17datasum18 = 0
    food17datasum19 = 0
    food17datasum20 = 0
    food17datasum21 = 0
    food17datasum22 = 0
    food17datasum23 = 0

    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1
    
    for strfood1 in food01time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food01datasum01 = food01datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food01datasum02 = food01datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food01datasum03 = food01datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food01datasum04 = food01datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food01datasum05 = food01datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food01datasum06 = food01datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food01datasum07 = food01datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food01datasum08 = food01datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food01datasum09 = food01datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food01datasum10 = food01datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food01datasum11 = food01datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food01datasum12 = food01datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food01datasum13 = food01datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food01datasum14 = food01datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food01datasum15 = food01datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food01datasum16 = food01datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food01datasum17 = food01datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food01datasum18 = food01datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food01datasum19 = food01datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food01datasum20 = food01datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food01datasum21 = food01datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food01datasum22 = food01datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food01datasum23 = food01datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food01datasum00 = food01datasum00 + len(data3)
                count0 = count0+1
                
    food01datasum00 = round(food01datasum00/count0, 2)
    food01datasum01 = round(food01datasum01/count1, 2) 
    food01datasum02 = round(food01datasum02/count2, 2) 
    food01datasum03 = round(food01datasum03/count3, 2) 
    food01datasum04 = round(food01datasum04/count4, 2) 
    food01datasum05 = round(food01datasum05/count5, 2) 
    food01datasum06 = round(food01datasum06/count6, 2) 
    food01datasum07 = round(food01datasum07/count7, 2) 
    food01datasum08 = round(food01datasum08/count8, 2) 
    food01datasum09 = round(food01datasum09/count9, 2) 
    food01datasum10 = round(food01datasum10/count10, 2) 
    food01datasum11 = round(food01datasum11/count11, 2)
    food01datasum12 = round(food01datasum12/count12, 2)
    food01datasum13 = round(food01datasum13/count13, 2)
    food01datasum14 = round(food01datasum14/count14, 2)
    food01datasum15 = round(food01datasum15/count15, 2)
    food01datasum16 = round(food01datasum16/count16, 2)
    food01datasum17 = round(food01datasum17/count17, 2)
    food01datasum18 = round(food01datasum18/count18, 2)
    food01datasum19 = round(food01datasum19/count19, 2)
    food01datasum20 = round(food01datasum20/count20, 2)
    food01datasum21 = round(food01datasum21/count21, 2)
    food01datasum22 = round(food01datasum22/count22, 2)
    food01datasum23 = round(food01datasum23/count23, 2)
    food01datasum = [food01datasum00,food01datasum01,food01datasum02,food01datasum03,food01datasum04,food01datasum05,food01datasum06,food01datasum07,
                    food01datasum08,food01datasum09,food01datasum10,food01datasum11,food01datasum12,food01datasum13,food01datasum14,food01datasum15,
                    food01datasum16,food01datasum17,food01datasum18,food01datasum19,food01datasum20,food01datasum21,food01datasum22,food01datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food02time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food02datasum01 = food02datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food02datasum02 = food02datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food02datasum03 = food02datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food02datasum04 = food02datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food02datasum05 = food02datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food02datasum06 = food02datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food02datasum07 = food02datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food02datasum08 = food02datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food02datasum09 = food02datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food02datasum10 = food02datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food02datasum11 = food02datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food02datasum12 = food02datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food02datasum13 = food02datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food02datasum14 = food02datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food02datasum15 = food02datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food02datasum16 = food02datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food02datasum17 = food02datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food02datasum18 = food02datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food02datasum19 = food02datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food02datasum20 = food02datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food02datasum21 = food02datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food02datasum22 = food02datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food02datasum23 = food02datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food02datasum00 = food02datasum00 + len(data3)
                count0 = count0+1

    food02datasum00 = round(food02datasum00/count0, 2)
    food02datasum01 = round(food02datasum01/count1, 2) 
    food02datasum02 = round(food02datasum02/count2, 2) 
    food02datasum03 = round(food02datasum03/count3, 2) 
    food02datasum04 = round(food02datasum04/count4, 2) 
    food02datasum05 = round(food02datasum05/count5, 2) 
    food02datasum06 = round(food02datasum06/count6, 2) 
    food02datasum07 = round(food02datasum07/count7, 2) 
    food02datasum08 = round(food02datasum08/count8, 2) 
    food02datasum09 = round(food02datasum09/count9, 2) 
    food02datasum10 = round(food02datasum10/count10, 2) 
    food02datasum11 = round(food02datasum11/count11, 2)
    food02datasum12 = round(food02datasum12/count12, 2)
    food02datasum13 = round(food02datasum13/count13, 2)
    food02datasum14 = round(food02datasum14/count14, 2)
    food02datasum15 = round(food02datasum15/count15, 2)
    food02datasum16 = round(food02datasum16/count16, 2)
    food02datasum17 = round(food02datasum17/count17, 2)
    food02datasum18 = round(food02datasum18/count18, 2)
    food02datasum19 = round(food02datasum19/count19, 2)
    food02datasum20 = round(food02datasum20/count20, 2)
    food02datasum21 = round(food02datasum21/count21, 2)
    food02datasum22 = round(food02datasum22/count22, 2)
    food02datasum23 = round(food02datasum23/count23, 2)
    food02datasum = [food02datasum00,food02datasum01,food02datasum02,food02datasum03,food02datasum04,food02datasum05,food02datasum06,food02datasum07,
                    food02datasum08,food02datasum09,food02datasum10,food02datasum11,food02datasum12,food02datasum13,food02datasum14,food02datasum15,
                    food02datasum16,food02datasum17,food02datasum18,food02datasum19,food02datasum20,food02datasum21,food02datasum22,food02datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food03time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food03datasum01 = food03datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food03datasum02 = food03datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food03datasum03 = food03datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food03datasum04 = food03datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food03datasum05 = food03datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food03datasum06 = food03datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food03datasum07 = food03datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food03datasum08 = food03datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food03datasum09 = food03datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food03datasum10 = food03datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food03datasum11 = food03datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food03datasum12 = food03datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food03datasum13 = food03datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food03datasum14 = food03datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food03datasum15 = food03datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food03datasum16 = food03datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food03datasum17 = food03datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food03datasum18 = food03datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food03datasum19 = food03datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food03datasum20 = food03datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food03datasum21 = food03datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food03datasum22 = food03datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food03datasum23 = food03datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food03datasum00 = food03datasum00 + len(data3)
                count0 = count0+1

    food03datasum00 = round(food03datasum00/count0, 2)
    food03datasum01 = round(food03datasum01/count1, 2) 
    food03datasum02 = round(food03datasum02/count2, 2) 
    food03datasum03 = round(food03datasum03/count3, 2) 
    food03datasum04 = round(food03datasum04/count4, 2) 
    food03datasum05 = round(food03datasum05/count5, 2) 
    food03datasum06 = round(food03datasum06/count6, 2) 
    food03datasum07 = round(food03datasum07/count7, 2) 
    food03datasum08 = round(food03datasum08/count8, 2) 
    food03datasum09 = round(food03datasum09/count9, 2) 
    food03datasum10 = round(food03datasum10/count10, 2) 
    food03datasum11 = round(food03datasum11/count11, 2)
    food03datasum12 = round(food03datasum12/count12, 2)
    food03datasum13 = round(food03datasum13/count13, 2)
    food03datasum14 = round(food03datasum14/count14, 2)
    food03datasum15 = round(food03datasum15/count15, 2)
    food03datasum16 = round(food03datasum16/count16, 2)
    food03datasum17 = round(food03datasum17/count17, 2)
    food03datasum18 = round(food03datasum18/count18, 2)
    food03datasum19 = round(food03datasum19/count19, 2)
    food03datasum20 = round(food03datasum20/count20, 2)
    food03datasum21 = round(food03datasum21/count21, 2)
    food03datasum22 = round(food03datasum22/count22, 2)
    food03datasum23 = round(food03datasum23/count23, 2)
    food03datasum = [food03datasum00,food03datasum01,food03datasum02,food03datasum03,food03datasum04,food03datasum05,food03datasum06,food03datasum07,
                    food03datasum08,food03datasum09,food03datasum10,food03datasum11,food03datasum12,food03datasum13,food03datasum14,food03datasum15,
                    food03datasum16,food03datasum17,food03datasum18,food03datasum19,food03datasum20,food03datasum21,food03datasum22,food03datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food04time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food04datasum01 = food04datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food04datasum02 = food04datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food04datasum03 = food04datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food04datasum04 = food04datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food04datasum05 = food04datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food04datasum06 = food04datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food04datasum07 = food04datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food04datasum08 = food04datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food04datasum09 = food04datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food04datasum10 = food04datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food04datasum11 = food04datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food04datasum12 = food04datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food04datasum13 = food04datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food04datasum14 = food04datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food04datasum15 = food04datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food04datasum16 = food04datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food04datasum17 = food04datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food04datasum18 = food04datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food04datasum19 = food04datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food04datasum20 = food04datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food04datasum21 = food04datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food04datasum22 = food04datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food04datasum23 = food04datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food04datasum00 = food04datasum00 + len(data3)
                count0 = count0+1

    food04datasum00 = round(food04datasum00/count0, 2)
    food04datasum01 = round(food04datasum01/count1, 2)
    food04datasum02 = round(food04datasum02/count2, 2) 
    food04datasum03 = round(food04datasum03/count3, 2) 
    food04datasum04 = round(food04datasum04/count4, 2) 
    food04datasum05 = round(food04datasum05/count5, 2) 
    food04datasum06 = round(food04datasum06/count6, 2) 
    food04datasum07 = round(food04datasum07/count7, 2) 
    food04datasum08 = round(food04datasum08/count8, 2) 
    food04datasum09 = round(food04datasum09/count9, 2) 
    food04datasum10 = round(food04datasum10/count10, 2) 
    food04datasum11 = round(food04datasum11/count11, 2)
    food04datasum12 = round(food04datasum12/count12, 2)
    food04datasum13 = round(food04datasum13/count13, 2)
    food04datasum14 = round(food04datasum14/count14, 2)
    food04datasum15 = round(food04datasum15/count15, 2)
    food04datasum16 = round(food04datasum16/count16, 2)
    food04datasum17 = round(food04datasum17/count17, 2)
    food04datasum18 = round(food04datasum18/count18, 2)
    food04datasum19 = round(food04datasum19/count19, 2)
    food04datasum20 = round(food04datasum20/count20, 2)
    food04datasum21 = round(food04datasum21/count21, 2)
    food04datasum22 = round(food04datasum22/count22, 2)
    food04datasum23 = round(food04datasum23/count23, 2)
    food04datasum = [food04datasum00,food04datasum01,food04datasum02,food04datasum03,food04datasum04,food04datasum05,food04datasum06,food04datasum07,
                    food04datasum08,food04datasum09,food04datasum10,food04datasum11,food04datasum12,food04datasum13,food04datasum14,food04datasum15,
                    food04datasum16,food04datasum17,food04datasum18,food04datasum19,food04datasum20,food04datasum21,food04datasum22,food04datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food05time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food05datasum01 = food05datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food05datasum02 = food05datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food05datasum03 = food05datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food05datasum04 = food05datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food05datasum05 = food05datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food05datasum06 = food05datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food05datasum07 = food05datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food05datasum08 = food05datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food05datasum09 = food05datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food05datasum10 = food05datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food05datasum11 = food05datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food05datasum12 = food05datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food05datasum13 = food05datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food05datasum14 = food05datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food05datasum15 = food05datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food05datasum16 = food05datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food05datasum17 = food05datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food05datasum18 = food05datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food05datasum19 = food05datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food05datasum20 = food05datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food05datasum21 = food05datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food05datasum22 = food05datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food05datasum23 = food05datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food05datasum00 = food05datasum00 + len(data3)
                count0 = count0+1

    food05datasum00 = round(food05datasum00/count0, 2)
    food05datasum01 = round(food05datasum01/count1, 2) 
    food05datasum02 = round(food05datasum02/count2, 2) 
    food05datasum03 = round(food05datasum03/count3, 2) 
    food05datasum04 = round(food05datasum04/count4, 2) 
    food05datasum05 = round(food05datasum05/count5, 2) 
    food05datasum06 = round(food05datasum06/count6, 2) 
    food05datasum07 = round(food05datasum07/count7, 2) 
    food05datasum08 = round(food05datasum08/count8, 2) 
    food05datasum09 = round(food05datasum09/count9, 2) 
    food05datasum10 = round(food05datasum10/count10, 2) 
    food05datasum11 = round(food05datasum11/count11, 2)
    food05datasum12 = round(food05datasum12/count12, 2)
    food05datasum13 = round(food05datasum13/count13, 2)
    food05datasum14 = round(food05datasum14/count14, 2)
    food05datasum15 = round(food05datasum15/count15, 2)
    food05datasum16 = round(food05datasum16/count16, 2)
    food05datasum17 = round(food05datasum17/count17, 2)
    food05datasum18 = round(food05datasum18/count18, 2)
    food05datasum19 = round(food05datasum19/count19, 2)
    food05datasum20 = round(food05datasum20/count20, 2)
    food05datasum21 = round(food05datasum21/count21, 2)
    food05datasum22 = round(food05datasum22/count22, 2)
    food05datasum23 = round(food05datasum23/count23, 2)
    food05datasum = [food05datasum00,food05datasum01,food05datasum02,food05datasum03,food05datasum04,food05datasum05,food05datasum06,food05datasum07,
                    food05datasum08,food05datasum09,food05datasum10,food05datasum11,food05datasum12,food05datasum13,food05datasum14,food05datasum15,
                    food05datasum16,food05datasum17,food05datasum18,food05datasum19,food05datasum20,food05datasum21,food05datasum22,food05datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food06time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food06datasum01 = food06datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food06datasum02 = food06datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food06datasum03 = food06datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food06datasum04 = food06datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food06datasum05 = food06datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food06datasum06 = food06datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food06datasum07 = food06datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food06datasum08 = food06datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food06datasum09 = food06datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food06datasum10 = food06datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food06datasum11 = food06datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food06datasum12 = food06datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food06datasum13 = food06datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food06datasum14 = food06datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food06datasum15 = food06datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food06datasum16 = food06datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food06datasum17 = food06datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food06datasum18 = food06datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food06datasum19 = food06datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food06datasum20 = food06datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food06datasum21 = food06datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food06datasum22 = food06datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food06datasum23 = food06datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food06datasum00 = food06datasum00 + len(data3)
                count0 = count0+1

    food06datasum00 = round(food06datasum00/count0, 2)
    food06datasum01 = round(food06datasum01/count1, 2) 
    food06datasum02 = round(food06datasum02/count2, 2) 
    food06datasum03 = round(food06datasum03/count3, 2) 
    food06datasum04 = round(food06datasum04/count4, 2) 
    food06datasum05 = round(food06datasum05/count5, 2) 
    food06datasum06 = round(food06datasum06/count6, 2) 
    food06datasum07 = round(food06datasum07/count7, 2) 
    food06datasum08 = round(food06datasum08/count8, 2) 
    food06datasum09 = round(food06datasum09/count9, 2) 
    food06datasum10 = round(food06datasum10/count10, 2) 
    food06datasum11 = round(food06datasum11/count11, 2)
    food06datasum12 = round(food06datasum12/count12, 2)
    food06datasum13 = round(food06datasum13/count13, 2)
    food06datasum14 = round(food06datasum14/count14, 2)
    food06datasum15 = round(food06datasum15/count15, 2)
    food06datasum16 = round(food06datasum16/count16, 2)
    food06datasum17 = round(food06datasum17/count17, 2)
    food06datasum18 = round(food06datasum18/count18, 2)
    food06datasum19 = round(food06datasum19/count19, 2)
    food06datasum20 = round(food06datasum20/count20, 2)
    food06datasum21 = round(food06datasum21/count21, 2)
    food06datasum22 = round(food06datasum22/count22, 2)
    food06datasum23 = round(food06datasum23/count23, 2)
    food06datasum = [food06datasum00,food06datasum01,food06datasum02,food06datasum03,food06datasum04,food06datasum05,food06datasum06,food06datasum07,
                    food06datasum08,food06datasum09,food06datasum10,food06datasum11,food06datasum12,food06datasum13,food06datasum14,food06datasum15,
                    food06datasum16,food06datasum17,food06datasum18,food06datasum19,food06datasum20,food06datasum21,food06datasum22,food06datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food07time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food07datasum01 = food07datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food07datasum02 = food07datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food07datasum03 = food07datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food07datasum04 = food07datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food07datasum05 = food07datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food07datasum06 = food07datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food07datasum07 = food07datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food07datasum08 = food07datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food07datasum09 = food07datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food07datasum10 = food07datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food07datasum11 = food07datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food07datasum12 = food07datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food07datasum13 = food07datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food07datasum14 = food07datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food07datasum15 = food07datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food07datasum16 = food07datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food07datasum17 = food07datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food07datasum18 = food07datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food07datasum19 = food07datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food07datasum20 = food07datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food07datasum21 = food07datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food07datasum22 = food07datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food07datasum23 = food07datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food07datasum00 = food07datasum00 + len(data3)
                count0 = count0+1

    food07datasum00 = round(food07datasum00/count0, 2)
    food07datasum01 = round(food07datasum01/count1, 2) 
    food07datasum02 = round(food07datasum02/count2, 2) 
    food07datasum03 = round(food07datasum03/count3, 2) 
    food07datasum04 = round(food07datasum04/count4, 2) 
    food07datasum05 = round(food07datasum05/count5, 2) 
    food07datasum06 = round(food07datasum06/count6, 2) 
    food07datasum07 = round(food07datasum07/count7, 2) 
    food07datasum08 = round(food07datasum08/count8, 2) 
    food07datasum09 = round(food07datasum09/count9, 2) 
    food07datasum10 = round(food07datasum10/count10, 2) 
    food07datasum11 = round(food07datasum11/count11, 2)
    food07datasum12 = round(food07datasum12/count12, 2)
    food07datasum13 = round(food07datasum13/count13, 2)
    food07datasum14 = round(food07datasum14/count14, 2)
    food07datasum15 = round(food07datasum15/count15, 2)
    food07datasum16 = round(food07datasum16/count16, 2)
    food07datasum17 = round(food07datasum17/count17, 2)
    food07datasum18 = round(food07datasum18/count18, 2)
    food07datasum19 = round(food07datasum19/count19, 2)
    food07datasum20 = round(food07datasum20/count20, 2)
    food07datasum21 = round(food07datasum21/count21, 2)
    food07datasum22 = round(food07datasum22/count22, 2)
    food07datasum23 = round(food07datasum23/count23, 2)
    food07datasum = [food07datasum00,food07datasum01,food07datasum02,food07datasum03,food07datasum04,food07datasum05,food07datasum06,food07datasum07,
                    food07datasum08,food07datasum09,food07datasum10,food07datasum11,food07datasum12,food07datasum13,food07datasum14,food07datasum15,
                    food07datasum16,food07datasum17,food07datasum18,food07datasum19,food07datasum20,food07datasum21,food07datasum22,food07datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food08time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food08datasum01 = food08datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food08datasum02 = food08datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food08datasum03 = food08datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food08datasum04 = food08datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food08datasum05 = food08datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food08datasum06 = food08datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food08datasum07 = food08datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food08datasum08 = food08datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food08datasum09 = food08datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food08datasum10 = food08datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food08datasum11 = food08datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food08datasum12 = food08datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food08datasum13 = food08datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food08datasum14 = food08datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food08datasum15 = food08datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food08datasum16 = food08datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food08datasum17 = food08datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food08datasum18 = food08datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food08datasum19 = food08datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food08datasum20 = food08datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food08datasum21 = food08datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food08datasum22 = food08datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food08datasum23 = food08datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food08datasum00 = food08datasum00 + len(data3)
                count0 = count0+1

    food08datasum00 = round(food08datasum00/count0, 2)
    food08datasum01 = round(food08datasum01/count1, 2) 
    food08datasum02 = round(food08datasum02/count2, 2) 
    food08datasum03 = round(food08datasum03/count3, 2) 
    food08datasum04 = round(food08datasum04/count4, 2) 
    food08datasum05 = round(food08datasum05/count5, 2) 
    food08datasum06 = round(food08datasum06/count6, 2) 
    food08datasum07 = round(food08datasum07/count7, 2) 
    food08datasum08 = round(food08datasum08/count8, 2) 
    food08datasum09 = round(food08datasum09/count9, 2) 
    food08datasum10 = round(food08datasum10/count10, 2) 
    food08datasum11 = round(food08datasum11/count11, 2)
    food08datasum12 = round(food08datasum12/count12, 2)
    food08datasum13 = round(food08datasum13/count13, 2)
    food08datasum14 = round(food08datasum14/count14, 2)
    food08datasum15 = round(food08datasum15/count15, 2)
    food08datasum16 = round(food08datasum16/count16, 2)
    food08datasum17 = round(food08datasum17/count17, 2)
    food08datasum18 = round(food08datasum18/count18, 2)
    food08datasum19 = round(food08datasum19/count19, 2)
    food08datasum20 = round(food08datasum20/count20, 2)
    food08datasum21 = round(food08datasum21/count21, 2)
    food08datasum22 = round(food08datasum22/count22, 2)
    food08datasum23 = round(food08datasum23/count23, 2)
    food08datasum = [food08datasum00,food08datasum01,food08datasum02,food08datasum03,food08datasum04,food08datasum05,food08datasum06,food08datasum07,
                    food08datasum08,food08datasum09,food08datasum10,food08datasum11,food08datasum12,food08datasum13,food08datasum14,food08datasum15,
                    food08datasum16,food08datasum17,food08datasum18,food08datasum19,food08datasum20,food08datasum21,food08datasum22,food08datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food09time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food09datasum01 = food09datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food09datasum02 = food09datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food09datasum03 = food09datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food09datasum04 = food09datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food09datasum05 = food09datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food09datasum06 = food09datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food09datasum07 = food09datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food09datasum08 = food09datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food09datasum09 = food09datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food09datasum10 = food09datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food09datasum11 = food09datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food09datasum12 = food09datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food09datasum13 = food09datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food09datasum14 = food09datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food09datasum15 = food09datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food09datasum16 = food09datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food09datasum17 = food09datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food09datasum18 = food09datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food09datasum19 = food09datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food09datasum20 = food09datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food09datasum21 = food09datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food09datasum22 = food09datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food09datasum23 = food09datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food09datasum00 = food09datasum00 + len(data3)
                count0 = count0+1

    food09datasum00 = round(food09datasum00/count0, 2)
    food09datasum01 = round(food09datasum01/count1, 2)
    food09datasum02 = round(food09datasum02/count2, 2) 
    food09datasum03 = round(food09datasum03/count3, 2) 
    food09datasum04 = round(food09datasum04/count4, 2) 
    food09datasum05 = round(food09datasum05/count5, 2) 
    food09datasum06 = round(food09datasum06/count6, 2) 
    food09datasum07 = round(food09datasum07/count7, 2) 
    food09datasum08 = round(food09datasum08/count8, 2) 
    food09datasum09 = round(food09datasum09/count9, 2) 
    food09datasum10 = round(food09datasum10/count10, 2) 
    food09datasum11 = round(food09datasum11/count11, 2)
    food09datasum12 = round(food09datasum12/count12, 2)
    food09datasum13 = round(food09datasum13/count13, 2)
    food09datasum14 = round(food09datasum14/count14, 2)
    food09datasum15 = round(food09datasum15/count15, 2)
    food09datasum16 = round(food09datasum16/count16, 2)
    food09datasum17 = round(food09datasum17/count17, 2)
    food09datasum18 = round(food09datasum18/count18, 2)
    food09datasum19 = round(food09datasum19/count19, 2)
    food09datasum20 = round(food09datasum20/count20, 2)
    food09datasum21 = round(food09datasum21/count21, 2)
    food09datasum22 = round(food09datasum22/count22, 2)
    food09datasum23 = round(food09datasum23/count23, 2)
    food09datasum = [food09datasum00,food09datasum01,food09datasum02,food09datasum03,food09datasum04,food09datasum05,food09datasum06,food09datasum07,
                    food09datasum08,food09datasum09,food09datasum10,food09datasum11,food09datasum12,food09datasum13,food09datasum14,food09datasum15,
                    food09datasum16,food09datasum17,food09datasum18,food09datasum19,food09datasum20,food09datasum21,food09datasum22,food09datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food10time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food10datasum01 = food10datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food10datasum02 = food10datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food10datasum03 = food10datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food10datasum04 = food10datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food10datasum05 = food10datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food10datasum06 = food10datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food10datasum07 = food10datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food10datasum08 = food10datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food10datasum09 = food10datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food10datasum10 = food10datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food10datasum11 = food10datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food10datasum12 = food10datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food10datasum13 = food10datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food10datasum14 = food10datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food10datasum15 = food10datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food10datasum16 = food10datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food10datasum17 = food10datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food10datasum18 = food10datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food10datasum19 = food10datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food10datasum20 = food10datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food10datasum21 = food10datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food10datasum22 = food10datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food10datasum23 = food10datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food10datasum00 = food10datasum00 + len(data3)
                count0 = count0+1

    food10datasum00 = round(food10datasum00/count0, 2)
    food10datasum01 = round(food10datasum01/count1, 2) 
    food10datasum02 = round(food10datasum02/count2, 2) 
    food10datasum03 = round(food10datasum03/count3, 2) 
    food10datasum04 = round(food10datasum04/count4, 2) 
    food10datasum05 = round(food10datasum05/count5, 2) 
    food10datasum06 = round(food10datasum06/count6, 2) 
    food10datasum07 = round(food10datasum07/count7, 2) 
    food10datasum08 = round(food10datasum08/count8, 2) 
    food10datasum09 = round(food10datasum09/count9, 2) 
    food10datasum10 = round(food10datasum10/count10, 2) 
    food10datasum11 = round(food10datasum11/count11, 2)
    food10datasum12 = round(food10datasum12/count12, 2)
    food10datasum13 = round(food10datasum13/count13, 2)
    food10datasum14 = round(food10datasum14/count14, 2)
    food10datasum15 = round(food10datasum15/count15, 2)
    food10datasum16 = round(food10datasum16/count16, 2)
    food10datasum17 = round(food10datasum17/count17, 2)
    food10datasum18 = round(food10datasum18/count18, 2)
    food10datasum19 = round(food10datasum19/count19, 2)
    food10datasum20 = round(food10datasum20/count20, 2)
    food10datasum21 = round(food10datasum21/count21, 2)
    food10datasum22 = round(food10datasum22/count22, 2)
    food10datasum23 = round(food10datasum23/count23, 2)
    food10datasum = [food10datasum00,food10datasum01,food10datasum02,food10datasum03,food10datasum04,food10datasum05,food10datasum06,food10datasum07,
                    food10datasum08,food10datasum09,food10datasum10,food10datasum11,food10datasum12,food10datasum13,food10datasum14,food10datasum15,
                    food10datasum16,food10datasum17,food10datasum18,food10datasum19,food10datasum20,food10datasum21,food10datasum22,food10datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food11time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food11datasum01 = food11datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food11datasum02 = food11datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food11datasum03 = food11datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food11datasum04 = food11datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food11datasum05 = food11datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food11datasum06 = food11datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food11datasum07 = food11datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food11datasum08 = food11datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food11datasum09 = food11datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food11datasum10 = food11datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food11datasum11 = food11datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food11datasum12 = food11datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food11datasum13 = food11datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food11datasum14 = food11datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food11datasum15 = food11datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food11datasum16 = food11datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food11datasum17 = food11datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food11datasum18 = food11datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food11datasum19 = food11datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food11datasum20 = food11datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food11datasum21 = food11datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food11datasum22 = food11datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food11datasum23 = food11datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food11datasum00 = food11datasum00 + len(data3)
                count0 = count0+1

    food11datasum00 = round(food11datasum00/count0, 2)
    food11datasum01 = round(food11datasum01/count1, 2) 
    food11datasum02 = round(food11datasum02/count2, 2) 
    food11datasum03 = round(food11datasum03/count3, 2) 
    food11datasum04 = round(food11datasum04/count4, 2) 
    food11datasum05 = round(food11datasum05/count5, 2) 
    food11datasum06 = round(food11datasum06/count6, 2) 
    food11datasum07 = round(food11datasum07/count7, 2) 
    food11datasum08 = round(food11datasum08/count8, 2) 
    food11datasum09 = round(food11datasum09/count9, 2) 
    food11datasum10 = round(food11datasum10/count10, 2) 
    food11datasum11 = round(food11datasum11/count11, 2)
    food11datasum12 = round(food11datasum12/count12, 2)
    food11datasum13 = round(food11datasum13/count13, 2)
    food11datasum14 = round(food11datasum14/count14, 2)
    food11datasum15 = round(food11datasum15/count15, 2)
    food11datasum16 = round(food11datasum16/count16, 2)
    food11datasum17 = round(food11datasum17/count17, 2)
    food11datasum18 = round(food11datasum18/count18, 2)
    food11datasum19 = round(food11datasum19/count19, 2)
    food11datasum20 = round(food11datasum20/count20, 2)
    food11datasum21 = round(food11datasum21/count21, 2)
    food11datasum22 = round(food11datasum22/count22, 2)
    food11datasum23 = round(food11datasum23/count23, 2)
    food11datasum = [food11datasum00,food11datasum01,food11datasum02,food11datasum03,food11datasum04,food11datasum05,food11datasum06,food11datasum07,
                    food11datasum08,food11datasum09,food11datasum10,food11datasum11,food11datasum12,food11datasum13,food11datasum14,food11datasum15,
                    food11datasum16,food11datasum17,food11datasum18,food11datasum19,food11datasum20,food11datasum21,food11datasum22,food11datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food12time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food12datasum01 = food12datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food12datasum02 = food12datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food12datasum03 = food12datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food12datasum04 = food12datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food12datasum05 = food12datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food12datasum06 = food12datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food12datasum07 = food12datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food12datasum08 = food12datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food12datasum09 = food12datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food12datasum10 = food12datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food12datasum11 = food12datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food12datasum12 = food12datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food12datasum13 = food12datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food12datasum14 = food12datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food12datasum15 = food12datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food12datasum16 = food12datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food12datasum17 = food12datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food12datasum18 = food12datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food12datasum19 = food12datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food12datasum20 = food12datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food12datasum21 = food12datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food12datasum22 = food12datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food12datasum23 = food12datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food12datasum00 = food12datasum00 + len(data3)
                count0 = count0+1

    food12datasum00 = round(food12datasum00/count0, 2)
    food12datasum01 = round(food12datasum01/count1, 2) 
    food12datasum02 = round(food12datasum02/count2, 2) 
    food12datasum03 = round(food12datasum03/count3, 2) 
    food12datasum04 = round(food12datasum04/count4, 2) 
    food12datasum05 = round(food12datasum05/count5, 2)
    food12datasum06 = round(food12datasum06/count6, 2) 
    food12datasum07 = round(food12datasum07/count7, 2) 
    food12datasum08 = round(food12datasum08/count8, 2) 
    food12datasum09 = round(food12datasum09/count9, 2)
    food12datasum10 = round(food12datasum10/count10, 2) 
    food12datasum11 = round(food12datasum11/count11, 2)
    food12datasum12 = round(food12datasum12/count12, 2)
    food12datasum13 = round(food12datasum13/count13, 2)
    food12datasum14 = round(food12datasum14/count14, 2)
    food12datasum15 = round(food12datasum15/count15, 2)
    food12datasum16 = round(food12datasum16/count16, 2)
    food12datasum17 = round(food12datasum17/count17, 2)
    food12datasum18 = round(food12datasum18/count18, 2)
    food12datasum19 = round(food12datasum19/count19, 2)
    food12datasum20 = round(food12datasum20/count20, 2)
    food12datasum21 = round(food12datasum21/count21, 2)
    food12datasum22 = round(food12datasum22/count22, 2)
    food12datasum23 = round(food12datasum23/count23, 2)
    food12datasum = [food12datasum00,food12datasum01,food12datasum02,food12datasum03,food12datasum04,food12datasum05,food12datasum06,food12datasum07,
                    food12datasum08,food12datasum09,food12datasum10,food12datasum11,food12datasum12,food12datasum13,food12datasum14,food12datasum15,
                    food12datasum16,food12datasum17,food12datasum18,food12datasum19,food12datasum20,food12datasum21,food12datasum22,food12datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food13time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food13datasum01 = food13datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food13datasum02 = food13datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food13datasum03 = food13datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food13datasum04 = food13datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food13datasum05 = food13datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food13datasum06 = food13datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food13datasum07 = food13datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food13datasum08 = food13datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food13datasum09 = food13datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food13datasum10 = food13datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food13datasum11 = food13datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food13datasum12 = food13datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food13datasum13 = food13datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food13datasum14 = food13datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food13datasum15 = food13datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food13datasum16 = food13datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food13datasum17 = food13datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food13datasum18 = food13datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food13datasum19 = food13datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food13datasum20 = food13datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food13datasum21 = food13datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food13datasum22 = food13datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food13datasum23 = food13datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food13datasum00 = food13datasum00 + len(data3)
                count0 = count0+1

    food13datasum00 = round(food13datasum00/count0, 2)
    food13datasum01 = round(food13datasum01/count1, 2)
    food13datasum02 = round(food13datasum02/count2, 2) 
    food13datasum03 = round(food13datasum03/count3, 2) 
    food13datasum04 = round(food13datasum04/count4, 2) 
    food13datasum05 = round(food13datasum05/count5, 2) 
    food13datasum06 = round(food13datasum06/count6, 2) 
    food13datasum07 = round(food13datasum07/count7, 2) 
    food13datasum08 = round(food13datasum08/count8, 2) 
    food13datasum09 = round(food13datasum09/count9, 2) 
    food13datasum10 = round(food13datasum10/count10, 2) 
    food13datasum11 = round(food13datasum11/count11, 2)
    food13datasum12 = round(food13datasum12/count12, 2)
    food13datasum13 = round(food13datasum13/count13, 2)
    food13datasum14 = round(food13datasum14/count14, 2)
    food13datasum15 = round(food13datasum15/count15, 2)
    food13datasum16 = round(food13datasum16/count16, 2)
    food13datasum17 = round(food13datasum17/count17, 2)
    food13datasum18 = round(food13datasum18/count18, 2)
    food13datasum19 = round(food13datasum19/count19, 2)
    food13datasum20 = round(food13datasum20/count20, 2)
    food13datasum21 = round(food13datasum21/count21, 2)
    food13datasum22 = round(food13datasum22/count22, 2)
    food13datasum23 = round(food13datasum23/count23, 2)
    food13datasum = [food13datasum00,food13datasum01,food13datasum02,food13datasum03,food13datasum04,food13datasum05,food13datasum06,food13datasum07,
                    food13datasum08,food13datasum09,food13datasum10,food13datasum11,food13datasum12,food13datasum13,food13datasum14,food13datasum15,
                    food13datasum16,food13datasum17,food13datasum18,food13datasum19,food13datasum20,food13datasum21,food13datasum22,food13datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food14time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food14datasum01 = food14datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food14datasum02 = food14datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food14datasum03 = food14datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food14datasum04 = food14datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food14datasum05 = food14datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food14datasum06 = food14datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food14datasum07 = food14datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food14datasum08 = food14datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food14datasum09 = food14datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food14datasum10 = food14datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food14datasum11 = food14datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food14datasum12 = food14datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food14datasum13 = food14datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food14datasum14 = food14datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food14datasum15 = food14datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food14datasum16 = food14datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food14datasum17 = food14datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food14datasum18 = food14datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food14datasum19 = food14datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food14datasum20 = food14datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food14datasum21 = food14datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food14datasum22 = food14datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food14datasum23 = food14datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food14datasum00 = food14datasum00 + len(data3)
                count0 = count0+1

    food14datasum00 = round(food14datasum00/count0, 2)
    food14datasum01 = round(food14datasum01/count1, 2) 
    food14datasum02 = round(food14datasum02/count2, 2) 
    food14datasum03 = round(food14datasum03/count3, 2) 
    food14datasum04 = round(food14datasum04/count4, 2) 
    food14datasum05 = round(food14datasum05/count5, 2) 
    food14datasum06 = round(food14datasum06/count6, 2) 
    food14datasum07 = round(food14datasum07/count7, 2) 
    food14datasum08 = round(food14datasum08/count8, 2) 
    food14datasum09 = round(food14datasum09/count9, 2) 
    food14datasum10 = round(food14datasum10/count10, 2) 
    food14datasum11 = round(food14datasum11/count11, 2)
    food14datasum12 = round(food14datasum12/count12, 2)
    food14datasum13 = round(food14datasum13/count13, 2)
    food14datasum14 = round(food14datasum14/count14, 2)
    food14datasum15 = round(food14datasum15/count15, 2)
    food14datasum16 = round(food14datasum16/count16, 2)
    food14datasum17 = round(food14datasum17/count17, 2)
    food14datasum18 = round(food14datasum18/count18, 2)
    food14datasum19 = round(food14datasum19/count19, 2)
    food14datasum20 = round(food14datasum20/count20, 2)
    food14datasum21 = round(food14datasum21/count21, 2)
    food14datasum22 = round(food14datasum22/count22, 2)
    food14datasum23 = round(food14datasum23/count23, 2)
    food14datasum = [food14datasum00,food14datasum01,food14datasum02,food14datasum03,food14datasum04,food14datasum05,food14datasum06,food14datasum07,
                    food14datasum08,food14datasum09,food14datasum10,food14datasum11,food14datasum12,food14datasum13,food14datasum14,food14datasum15,
                    food14datasum16,food14datasum17,food14datasum18,food14datasum19,food14datasum20,food14datasum21,food14datasum22,food14datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food15time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food15datasum01 = food15datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food15datasum02 = food15datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food15datasum03 = food15datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food15datasum04 = food15datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food15datasum05 = food15datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food15datasum06 = food15datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food15datasum07 = food15datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food15datasum08 = food15datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food15datasum09 = food15datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food15datasum10 = food15datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food15datasum11 = food15datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food15datasum12 = food15datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food15datasum13 = food15datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food15datasum14 = food15datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food15datasum15 = food15datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food15datasum16 = food15datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food15datasum17 = food15datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food15datasum18 = food15datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food15datasum19 = food15datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food15datasum20 = food15datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food15datasum21 = food15datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food15datasum22 = food15datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food15datasum23 = food15datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food15datasum00 = food15datasum00 + len(data3)
                count0 = count0+1

    food15datasum00 = round(food15datasum00/count0, 2)
    food15datasum01 = round(food15datasum01/count1, 2) 
    food15datasum02 = round(food15datasum02/count2, 2) 
    food15datasum03 = round(food15datasum03/count3, 2) 
    food15datasum04 = round(food15datasum04/count4, 2) 
    food15datasum05 = round(food15datasum05/count5, 2) 
    food15datasum06 = round(food15datasum06/count6, 2) 
    food15datasum07 = round(food15datasum07/count7, 2) 
    food15datasum08 = round(food15datasum08/count8, 2) 
    food15datasum09 = round(food15datasum09/count9, 2) 
    food15datasum10 = round(food15datasum10/count10, 2) 
    food15datasum11 = round(food15datasum11/count11, 2)
    food15datasum12 = round(food15datasum12/count12, 2)
    food15datasum13 = round(food15datasum13/count13, 2)
    food15datasum14 = round(food15datasum14/count14, 2)
    food15datasum15 = round(food15datasum15/count15, 2)
    food15datasum16 = round(food15datasum16/count16, 2)
    food15datasum17 = round(food15datasum17/count17, 2)
    food15datasum18 = round(food15datasum18/count18, 2)
    food15datasum19 = round(food15datasum19/count19, 2)
    food15datasum20 = round(food15datasum20/count20, 2)
    food15datasum21 = round(food15datasum21/count21, 2)
    food15datasum22 = round(food15datasum22/count22, 2)
    food15datasum23 = round(food15datasum23/count23, 2)
    food15datasum = [food15datasum00,food15datasum01,food15datasum02,food15datasum03,food15datasum04,food15datasum05,food15datasum06,food15datasum07,
                    food15datasum08,food15datasum09,food15datasum10,food15datasum11,food15datasum12,food15datasum13,food15datasum14,food15datasum15,
                    food15datasum16,food15datasum17,food15datasum18,food15datasum19,food15datasum20,food15datasum21,food15datasum22,food15datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food16time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food16datasum01 = food16datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food16datasum02 = food16datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food16datasum03 = food16datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food16datasum04 = food16datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food16datasum05 = food16datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food16datasum06 = food16datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food16datasum07 = food16datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food16datasum08 = food16datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food16datasum09 = food16datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food16datasum10 = food16datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food16datasum11 = food16datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food16datasum12 = food16datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food16datasum13 = food16datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food16datasum14 = food16datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food16datasum15 = food16datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food16datasum16 = food16datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food16datasum17 = food16datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food16datasum18 = food16datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food16datasum19 = food16datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food16datasum20 = food16datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food16datasum21 = food16datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food16datasum22 = food16datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food16datasum23 = food16datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food16datasum00 = food16datasum00 + len(data3)
                count0 = count0+1

    food16datasum00 = round(food16datasum00/count0, 2)
    food16datasum01 = round(food16datasum01/count1, 2) 
    food16datasum02 = round(food16datasum02/count2, 2) 
    food16datasum03 = round(food16datasum03/count3, 2) 
    food16datasum04 = round(food16datasum04/count4, 2) 
    food16datasum05 = round(food16datasum05/count5, 2) 
    food16datasum06 = round(food16datasum06/count6, 2) 
    food16datasum07 = round(food16datasum07/count7, 2) 
    food16datasum08 = round(food16datasum08/count8, 2) 
    food16datasum09 = round(food16datasum09/count9, 2) 
    food16datasum10 = round(food16datasum10/count10, 2) 
    food16datasum11 = round(food16datasum11/count11, 2)
    food16datasum12 = round(food16datasum12/count12, 2)
    food16datasum13 = round(food16datasum13/count13, 2)
    food16datasum14 = round(food16datasum14/count14, 2)
    food16datasum15 = round(food16datasum15/count15, 2)
    food16datasum16 = round(food16datasum16/count16, 2)
    food16datasum17 = round(food16datasum17/count17, 2)
    food16datasum18 = round(food16datasum18/count18, 2)
    food16datasum19 = round(food16datasum19/count19, 2)
    food16datasum20 = round(food16datasum20/count20, 2)
    food16datasum21 = round(food16datasum21/count21, 2)
    food16datasum22 = round(food16datasum22/count22, 2)
    food16datasum23 = round(food16datasum23/count23, 2)
    food16datasum = [food16datasum00,food16datasum01,food16datasum02,food16datasum03,food16datasum04,food16datasum05,food16datasum06,food16datasum07,
                    food16datasum08,food16datasum09,food16datasum10,food16datasum11,food16datasum12,food16datasum13,food16datasum14,food16datasum15,
                    food16datasum16,food16datasum17,food16datasum18,food16datasum19,food16datasum20,food16datasum21,food16datasum22,food16datasum23]
    count0 = 1
    count1 = 1
    count2 = 1
    count3 = 1
    count4 = 1
    count5 = 1
    count6 = 1
    count7 = 1
    count8 = 1
    count9 = 1
    count10 = 1
    count11 = 1
    count12 = 1
    count13 = 1
    count14 = 1
    count15 = 1
    count16 = 1
    count17 = 1
    count18 = 1
    count19 = 1
    count20 = 1
    count21 = 1
    count22 = 1
    count23 = 1

    for strfood1 in food17time:
        for strfood2 in strfood1:
            data = ''.join(strfood2[1:2])
            data2 = data[0:2]
            if data2 == '01':
                data3 = ''.join(strfood2[2:])
                food17datasum01 = food17datasum01 + len(data3)
                count1 = count1+1
            elif data2 == '02':
                data3 = ''.join(strfood2[2:])
                food17datasum02 = food17datasum02 + len(data3)
                count2 = count2+1
            elif data2 == '03':
                data3 = ''.join(strfood2[2:])
                food17datasum03 = food17datasum03 + len(data3)
                count3 = count3+1
            elif data2 == '04':
                data3 = ''.join(strfood2[2:])
                food17datasum04 = food17datasum04 + len(data3)
                count4 = count4+1
            elif data2 == '05':
                data3 = ''.join(strfood2[2:])
                food17datasum05 = food17datasum05 + len(data3)
                count5 = count5+1
            elif data2 == '06':
                data3 = ''.join(strfood2[2:])
                food17datasum06 = food17datasum06 + len(data3)
                count6 = count6+1
            elif data2 == '07':
                data3 = ''.join(strfood2[2:])
                food17datasum07 = food17datasum07 + len(data3)
                count7 = count7+1
            elif data2 == '08':
                data3 = ''.join(strfood2[2:])
                food17datasum08 = food17datasum08 + len(data3)
                count8 = count8+1
            elif data2 == '09':
                data3 = ''.join(strfood2[2:])
                food17datasum09 = food17datasum09 + len(data3)
                count9 = count9+1
            elif data2 == '10':
                data3 = ''.join(strfood2[2:])
                food17datasum10 = food17datasum10 + len(data3)
                count10 = count10+1
            elif data2 == '11':
                data3 = ''.join(strfood2[2:])
                food17datasum11 = food17datasum11 + len(data3)
                count11 = count11+1
            elif data2 == '12':
                data3 = ''.join(strfood2[2:])
                food17datasum12 = food17datasum12 + len(data3)
                count12 = count12+1
            elif data2 == '13':
                data3 = ''.join(strfood2[2:])
                food17datasum13 = food17datasum13 + len(data3)
                count13 = count13+1
            elif data2 == '14':
                data3 = ''.join(strfood2[2:])
                food17datasum14 = food17datasum14 + len(data3)
                count14 = count14+1
            elif data2 == '15':
                data3 = ''.join(strfood2[2:])
                food17datasum15 = food17datasum15 + len(data3)
                count15 = count15+1
            elif data2 == '16':
                data3 = ''.join(strfood2[2:])
                food17datasum16 = food17datasum16 + len(data3)
                count16 = count16+1
            elif data2 == '17':
                data3 = ''.join(strfood2[2:])
                food17datasum17 = food17datasum17 + len(data3)
                count17 = count17+1
            elif data2 == '18':
                data3 = ''.join(strfood2[2:])
                food17datasum18 = food17datasum18 + len(data3)
                count18 = count18+1
            elif data2 == '19':
                data3 = ''.join(strfood2[2:])
                food17datasum19 = food17datasum19 + len(data3)
                count19 = count19+1
            elif data2 == '20':
                data3 = ''.join(strfood2[2:])
                food17datasum20 = food17datasum20 + len(data3)
                count20 = count20+1
            elif data2 == '21':
                data3 = ''.join(strfood2[2:])
                food17datasum21 = food17datasum21 + len(data3)
                count21 = count21+1
            elif data2 == '22':
                data3 = ''.join(strfood2[2:])
                food17datasum22 = food17datasum22 + len(data3)
                count22 = count22+1
            elif data2 == '23':
                data3 = ''.join(strfood2[2:])
                food17datasum23 = food17datasum23 + len(data3)
                count23 = count23+1
            elif data2 == '00':
                data3 = ''.join(strfood2[2:])
                food17datasum00 = food17datasum00 + len(data3)
                count0 = count0+1

    food17datasum00 = round(food17datasum00/count0, 2)
    food17datasum01 = round(food17datasum01/count1, 2) 
    food17datasum02 = round(food17datasum02/count2, 2) 
    food17datasum03 = round(food17datasum03/count3, 2) 
    food17datasum04 = round(food17datasum04/count4, 2) 
    food17datasum05 = round(food17datasum05/count5, 2) 
    food17datasum06 = round(food17datasum06/count6, 2) 
    food17datasum07 = round(food17datasum07/count7, 2) 
    food17datasum08 = round(food17datasum08/count8, 2) 
    food17datasum09 = round(food17datasum09/count9, 2) 
    food17datasum10 = round(food17datasum10/count10, 2) 
    food17datasum11 = round(food17datasum11/count11, 2)
    food17datasum12 = round(food17datasum12/count12, 2)
    food17datasum13 = round(food17datasum13/count13, 2)
    food17datasum14 = round(food17datasum14/count14, 2)
    food17datasum15 = round(food17datasum15/count15, 2)
    food17datasum16 = round(food17datasum16/count16, 2)
    food17datasum17 = round(food17datasum17/count17, 2)
    food17datasum18 = round(food17datasum18/count18, 2)
    food17datasum19 = round(food17datasum19/count19, 2)
    food17datasum20 = round(food17datasum20/count20, 2)
    food17datasum21 = round(food17datasum21/count21, 2)
    food17datasum22 = round(food17datasum22/count22, 2)
    food17datasum23 = round(food17datasum23/count23, 2)
    print(food17datasum16)
    menu_list = ['짜장면', '탕수육', '짬뽕', '훠궈', '팔보채','찌개', '비빔밥', '볶음', '수육', '나물', '국밥','우동', '규동', '돈가스', '카레', '초밥', '스시']
    food17datasum = [food17datasum00,food17datasum01,food17datasum02,food17datasum03,food17datasum04,food17datasum05,food17datasum06,food17datasum07,
                    food17datasum08,food17datasum09,food17datasum10,food17datasum11,food17datasum12,food17datasum13,food17datasum14,food17datasum15,
                    food17datasum16,food17datasum17,food17datasum18,food17datasum19,food17datasum20,food17datasum21,food17datasum22,food17datasum23]
    x = [food01datasum, food02datasum, food03datasum,food04datasum,food05datasum,
    food06datasum,food07datasum,food08datasum,food09datasum, food10datasum,
    food11datasum,food12datasum,food13datasum,food14datasum,food15datasum, food16datasum, food17datasum]
  
    datas = { h : { menu_list[n] : 0 for n in range(17)} for h in range(24) }
    for i, sublist in enumerate(x):
        for idx, data in enumerate(sublist):
            datas[idx][menu_list[i]] = sublist[idx]
        

    return render(request, 'csvdata/datapage.html', {'data' : json.dumps(datas) })