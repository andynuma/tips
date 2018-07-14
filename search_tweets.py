import settings
import sys
import tweepy
from collections import Counter
import re
from numpy.random import *
from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.charfilter import *
from janome.tokenfilter import *


# 環境変数から認証情報を取得する。
CONSUMER_KEY = settings.CONSUMER_KEY
CONSUMER_SECRET = settings.CONSUMER_SECRET
ACCESS_TOKEN = settings.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = settings.ACCESS_TOKEN_SECRET

# 認証情報を設定する。
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)


#APIインスタンスを作成
api = tweepy.API(auth)
#ツイートをresultに格納
result = api.search("python" ,count=100)

#janome初期化
tokenizer = Tokenizer()
char_filters=[UnicodeNormalizeCharFilter()]
token_filters=[CompoundNounFilter(),POSStopFilter("助詞"),LowerCaseFilter()]
a = Analyzer(char_filters,tokenizer,token_filters)

#ツイッターデータ処理
for i in result:
    i = i.text
    for token in a.analyze(i):
        #print(token.surface)
        if token.surface == "cool":
            print("yes,that's right")

