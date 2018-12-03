@echo off
setlocal

rem pythonの実行バイナリのパス(インストーラで導入した場合は不要？)
set python=python.exe

rem np_tweet.pyを配置したパスを指定
set py_func=

rem np_tweet.pyをフルパスで指定
set np=%py_func%\np_tweet.py


%python% %np%

pause
