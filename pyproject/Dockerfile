# FROM <Dockerイメージ名>:<バージョンタグ>
# このイメージを元に使って
FROM python:3.8.7-slim

# イメージの中の"cd"
WORKDIR /work

# ローカルファイルをコンテナの中にコピーする
ADD src src
ADD tests tests
ADD requirements.txt requirements.txt
ADD setup.py setup.py
ADD MANIFEST.in MANIFEST.in

# コンテナにPythonパッケージをインストールする
RUN pip install --upgrade pip && pip install -r requirements.txt && pip install pytest

# テスト用のTestPyPIレポジトリからflaskr-kazurayamパッケージをインストールする
# Flask本体をはじめとする外部パッケージもここでインストールする
RUN pip install --index-url https://test.pypi.org/simple/ flaskr-kazurayam

# 環境変数を指定する
ENV FLASK_APP=src/flaskr

# init-dbを実行してデータベースを初期化する
RUN flask init-db

# WaitressがlistenするIPポートを公開する
EXPOSE 5000

# Dockerコンテナが起動した直後にwaitressでflaskrを実行する
CMD ["waitress-serve", "--call", "flaskr:create_app"]