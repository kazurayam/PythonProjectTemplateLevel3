# FROM <Dockerイメージ名>:<バージョンタグ>
# このイメージを元に使って
FROM python:3.8.7-slim

# 作業用ディレクトリを作ってそこにcdする
WORKDIR /work

# ローカルファイルをコンテナの中にコピーする
ADD flaskr flaskr
ADD requirements.txt requirements.txt
ADD setup.py setup.py
ADD MANIFEST.in MANIFEST.in

# コンテナにPythonパッケージをインストールする
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install pytest

# テスト用のTestPyPIレポジトリからflaskr-kazurayamパッケージをインストールする
# Flask本体をはじめとする外部パッケージもここでインストールする
RUN pip install --index-url https://test.pypi.org/simple/ flaskr-kazurayam

# 環境変数を指定する
ENV FLASK_APP=flaskr

# init-dbを実行してデータベースを初期化する
RUN flask init-db

# WaitressがlistenするIPポートを公開する
EXPOSE 8080

# Dockerコンテナが起動したらすぐにwaitressサーバでflaskrを起動する
CMD ["waitress-serve", "--port", "8080", "--call", "flaskr:create_app"]