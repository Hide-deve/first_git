
#インストール済パッケージの一覧表示
pip list

#インストール済パッケージの個別詳細表示
pip show "Package Name"

#pip showで確認したパスがないとimportは失敗する
import sys
import pprint
pprint.pprint(sys.path)


