# mpc-hc_nowplaying

概要
---
MPC-HCで再生中の音声ファイルのタグ情報を使って、X(旧Twitter)でnowplayingっぽいツイートを行うスクリプト

動作に必要なもの
---
- Windows 8.1/10 x64
- Python 3.8.5 x64
    - requests_oauthlib
- MPC-HC 1.7.13 x64 または MPC-HC(clsid2版) 2.1.4 x64
- X(旧Twitter) APIキー
- タイトル、アーティスト名のタグが埋め込まれた音声ファイル(flac、mp3で確認)

使い方
---
APIキーをこのコードに転記してMPC-HCで音楽再生中に実行

使用上の注意
---
- MPC-HCのファイル情報(Ctrl+3で表示)を参照しているため、MPC-HCを起動しただけの状態ではツイートされません
- MPC-BEも対応可能ですが、タイトル名の後にリリース年が括弧書きで入るため面倒くさくなりました
- 動画ファイル、アートワーク画像の埋め込まれた音声ファイルは未検証です
- 今後のUI変更等により動作しなくなる可能性があります

参考
---
- [Qiita ctypes.windll.user32について](https://qiita.com/sireline/items/d382636532cc78f02b61)
- [【Python】ウィンドウのタイトル文字列を取得する方法(win32api user32 GetWindowText)](https://oregengo.hatenablog.com/entry/2016/10/08/171018)
- [Pythonで特定のソフトをアクティブにする方法](https://qiita.com/Romane/items/9f70dbd4313ca6bf9fff)

ライセンス
---
MIT Licence
