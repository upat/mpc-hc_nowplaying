import ctypes
from requests_oauthlib import OAuth1Session

def tweet( text ):
	# X(旧Twitter) v2 エンドポイント
	ENDPOINT = 'https://api.twitter.com/2/tweets'
	# APIキー
	##### ↓↓↓使用環境により適宜編集↓↓↓ #####
	CK  = ''
	CS  = ''
	AT  = ''
	ATS = ''
	##### ↑↑↑使用環境により適宜編集↑↑↑ #####
	
	try:
		# 認証
		twitter = OAuth1Session( CK, CS, AT, ATS )
		# データ作成
		text = { 'text' : text }
		# ツイートする
		req_text = twitter.post( ENDPOINT, json = text )
	except:
		pass

class ChildWindowHandle():
	def __init__( self, parenthandle ): # 親ウィンドウハンドル
		self.__childhandle = [] # 子ウィンドウハンドル
		# mpc-hcが起動している(0ではない)時
		if parenthandle != 0:
			self.check = True
			ctypes.windll.user32.EnumChildWindows( parenthandle, ChildWindowHandle.getCallback(), ctypes.py_object( self.__childhandle ) )
		else:
			self.check = False

	@classmethod
	def getCallback( cls ):
		cls.ENUM_CHILD_WINDOWS = ctypes.WINFUNCTYPE( ctypes.c_int, ctypes.c_int, ctypes.py_object ) # コールバック関数クラス定義
		# コールバック用配列生成関数
		def callback( handle, list ):
			list.append( handle )
			return True
		return cls.ENUM_CHILD_WINDOWS( callback )
	
	# 指定した子ウィンドウハンドルからテキストを取得
	def getText( self, childhandle_index ):
		handle = self.__childhandle[childhandle_index]
		length = ctypes.windll.user32.GetWindowTextLengthW( handle ) # ウィンドウハンドルを元にテキスト長取得
		buffer = ctypes.create_unicode_buffer( length + 1 )          # テキスト長+1のunicode文字列バッファ作成
		ctypes.windll.user32.GetWindowTextW( handle, buffer, length + 1 ) # ウィンドウハンドルのテキストを取得
		return buffer.value

# mpc-hcのウィンドウハンドル取得(無い場合は0が返る)
CWH = ChildWindowHandle( ctypes.windll.user32.FindWindowW( 'MediaPlayerClassicW', 0 ) )
if CWH.check:
	# mpc-hcの子ウィンドウに含まれる情報を取得(設定で非表示にしていても取得可)
	title = CWH.getText( 14 ) # タイトル
	artist = CWH.getText( 16 ) # 作成者(アーティスト)
	# 起動直後且つ非再生時はtitleが空欄、artistがナビゲーション バーになる
	# buff_procの引数にphandleを渡すことでウィンドウのタイトルのみを取得して判定も可
	if( 0 < len( title ) and 0 < len( artist ) ):
		# tweet
		tweet( title + ' / ' + artist + ' #nowplaying' )
		# debug
		#print( title + ' / ' + artist )
