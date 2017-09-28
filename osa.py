import settings
import sys
import tweepy

"""
1.APIのキーは外部ファイル(settings)に下記のように記述している
##settings.py##
CONSUMER_KEY = "........"
CONSUMER_SECRET = "......."
.
.

2.引数に，ターゲットとなるユーザのIDをとる
python osa.py ユーザのID
で実行可能
"""


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

#タイムライン酒盗k
time_line = api.home_timeline()

#フォボする人のidを取得
argvs = sys.argv
user_id = argvs[1]

#ファボ魔
for tweet in time_line:
    #screen_name(id)でツイートを取得
    if tweet.user.screen_name == user_id:
        _id = tweet.id#ツイートのIDを取得
        try :
            api.create_favorite(_id)#ファボ
            print("favorite!")
        except:
            print("you have already favorited")#先にファボしてたとき
        #print(tweet.text)
