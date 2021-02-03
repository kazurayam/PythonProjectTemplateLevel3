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

# greetingをコマンドラインで実行できるようにする。
# テスト用のTestPyPIレポジトリからパッケージをダウンロードする
RUN pip install --index-url https://test.pypi.org/simple/ mypkg-kazurayam

# イメージを起動した直後にbashを実行するように指示
CMD bash
