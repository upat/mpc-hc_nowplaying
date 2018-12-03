import ctypes, sys, os, json
sys.path.append(os.environ.get('py_func'))
from requests_oauthlib import OAuth1Session
from twitter_key import *

def tweet(text):
	CK = CONSUMER_KEY
	CS = CONSUMER_SECRET
	AT = ACCESS_TOKEN
	ATS = ACCESS_TOKEN_SECRET
	twitter = OAuth1Session(CK, CS, AT, ATS)

	# TwitterAPIエンドポイントの取得
	url_text = "https://api.twitter.com/1.1/statuses/update.json"
	url_media = "https://upload.twitter.com/1.1/media/upload.json"

	text = {'status' : text} # 本文のみの場合

	# ツイートする
	req_media = twitter.post(url_text, params = text)

	# ツイート確認
	if req_media.status_code == 200:
		print('Tweet Succeed.')
	else:
		print("ERROR: %d" % req_media.status_code)

# callback用配列生成関数
def enum_child_windows_proc(handle, list):
	list.append(handle)
	return 1

# 指定したウィンドウハンドルから要素を取得
def buff_proc(handle):
	length = ctypes.windll.user32.GetWindowTextLengthW(handle)
	buffer = ctypes.create_unicode_buffer(length + 1)
	ctypes.windll.user32.GetWindowTextW(handle, buffer, length + 1)
	
	return buffer.value

# mpc-hcのウィンドウハンドル取得(無い場合は0が返る)
phandle = ctypes.windll.user32.FindWindowW('MediaPlayerClassicW', 0)
# 子ウィンドウハンドルを格納する配列の定義
chandle = []

if phandle != 0:
	# mpc-hcのウィンドウタイトル(ファイル名)を取得
	ptext = buff_proc(phandle)
	
	# 音楽プレーヤー起動のみ、再生を行っていない場合の判定
	if ptext != 'Media Player Classic Home Cinema':
		# 先頭のトラック番号、末尾の拡張子を除去
		ptext = ptext[(ptext.find(' ') + 1):ptext.rfind('.')]

		# mpc-hcの子ウィンドウハンドルの一覧取得
		ENUM_CHILD_WINDOWS = ctypes.WINFUNCTYPE(ctypes.c_int, ctypes.c_int, ctypes.py_object) # callback定義
		ctypes.windll.user32.EnumChildWindows(phandle, ENUM_CHILD_WINDOWS(enum_child_windows_proc), ctypes.py_object(chandle))

		# mpc-hcの子ウィンドウに含まれるアーティスト名を取得
		ctext = buff_proc(chandle[16])
		
		# tweet
		if(0 < len(ptext) and 0 < len(ctext)):
			tweet(ptext + ' / ' + ctext + ' #nowplaying')
