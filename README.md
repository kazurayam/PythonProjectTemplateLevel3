# Pythonプロジェクトのテンプレート　レベル3

- @author kazurayam
- @date Feb 2021

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
<details>
<summary>Table of Contents</summary>

- [これは何か](#%E3%81%93%E3%82%8C%E3%81%AF%E4%BD%95%E3%81%8B)
- [前提条件](#%E5%89%8D%E6%8F%90%E6%9D%A1%E4%BB%B6)
- [達成目標](#%E9%81%94%E6%88%90%E7%9B%AE%E6%A8%99)
- [手順](#%E6%89%8B%E9%A0%86)
  - [Pipfileから仮想環境を再現する](#pipfile%E3%81%8B%E3%82%89%E4%BB%AE%E6%83%B3%E7%92%B0%E5%A2%83%E3%82%92%E5%86%8D%E7%8F%BE%E3%81%99%E3%82%8B)
  - [Flask Tutorialを写経する](#flask-tutorial%E3%82%92%E5%86%99%E7%B5%8C%E3%81%99%E3%82%8B)
    - [flaskをPython仮想環境にインストールする](#flask%E3%82%92python%E4%BB%AE%E6%83%B3%E7%92%B0%E5%A2%83%E3%81%AB%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)
    - [.flaskenv ファイルに環境変数の設定を書く](#flaskenv-%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%81%AB%E7%92%B0%E5%A2%83%E5%A4%89%E6%95%B0%E3%81%AE%E8%A8%AD%E5%AE%9A%E3%82%92%E6%9B%B8%E3%81%8F)
    - [python-dotenvをインストールする](#python-dotenv%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)
    - [Pipfileにスクリプトを書いて起動を簡単にする](#pipfile%E3%81%AB%E3%82%B9%E3%82%AF%E3%83%AA%E3%83%97%E3%83%88%E3%82%92%E6%9B%B8%E3%81%84%E3%81%A6%E8%B5%B7%E5%8B%95%E3%82%92%E7%B0%A1%E5%8D%98%E3%81%AB%E3%81%99%E3%82%8B)
    - [Courtesy Notice](#courtesy-notice)
  - [pipでライブラリ化する](#pip%E3%81%A7%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E5%8C%96%E3%81%99%E3%82%8B)
    - [setup.pyファイルを書く](#setuppy%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E6%9B%B8%E3%81%8F)
    - [Pipfileからrequirements.txtを生成する](#pipfile%E3%81%8B%E3%82%89requirementstxt%E3%82%92%E7%94%9F%E6%88%90%E3%81%99%E3%82%8B)
    - [MANIFEST.inファイルを作る](#manifestin%E3%83%95%E3%82%A1%E3%82%A4%E3%83%AB%E3%82%92%E4%BD%9C%E3%82%8B)
    - [ライブラリを作る](#%E3%83%A9%E3%82%A4%E3%83%96%E3%83%A9%E3%83%AA%E3%82%92%E4%BD%9C%E3%82%8B)
    - [distディレクトリに作られたtarをpip installしてみる](#dist%E3%83%87%E3%82%A3%E3%83%AC%E3%82%AF%E3%83%88%E3%83%AA%E3%81%AB%E4%BD%9C%E3%82%89%E3%82%8C%E3%81%9Ftar%E3%82%92pip-install%E3%81%97%E3%81%A6%E3%81%BF%E3%82%8B)
  - [PyPIにアップロードする](#pypi%E3%81%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B)
    - [Twineをインストールする](#twine%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)
    - [PyPIに自分のためのアカウントを作る。](#pypi%E3%81%AB%E8%87%AA%E5%88%86%E3%81%AE%E3%81%9F%E3%82%81%E3%81%AE%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%82%92%E4%BD%9C%E3%82%8B)
    - [ビルドしてPyPIにアップロードする](#%E3%83%93%E3%83%AB%E3%83%89%E3%81%97%E3%81%A6pypi%E3%81%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B)
  - [Dockerイメージを作る](#docker%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%82%92%E4%BD%9C%E3%82%8B)
    - [Docker Desktop for Macをインストールする](#docker-desktop-for-mac%E3%82%92%E3%82%A4%E3%83%B3%E3%82%B9%E3%83%88%E3%83%BC%E3%83%AB%E3%81%99%E3%82%8B)
    - [Dockeer Hubにアカウントを作る](#dockeer-hub%E3%81%AB%E3%82%A2%E3%82%AB%E3%82%A6%E3%83%B3%E3%83%88%E3%82%92%E4%BD%9C%E3%82%8B)
    - [Dockerイメージを作る](#docker%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%82%92%E4%BD%9C%E3%82%8B-1)
    - [自作したDockerイメージからDockerコンテナを起動する](#%E8%87%AA%E4%BD%9C%E3%81%97%E3%81%9Fdocker%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%8B%E3%82%89docker%E3%82%B3%E3%83%B3%E3%83%86%E3%83%8A%E3%82%92%E8%B5%B7%E5%8B%95%E3%81%99%E3%82%8B)
    - [Dockerイメージの保存先](#docker%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%81%AE%E4%BF%9D%E5%AD%98%E5%85%88)
    - [dockerコマンドのレファレンス](#docker%E3%82%B3%E3%83%9E%E3%83%B3%E3%83%89%E3%81%AE%E3%83%AC%E3%83%95%E3%82%A1%E3%83%AC%E3%83%B3%E3%82%B9)
  - [Docker Hubにアップロードする](#docker-hub%E3%81%AB%E3%82%A2%E3%83%83%E3%83%97%E3%83%AD%E3%83%BC%E3%83%89%E3%81%99%E3%82%8B)
    - [ローカルからイメージをpushする方法](#%E3%83%AD%E3%83%BC%E3%82%AB%E3%83%AB%E3%81%8B%E3%82%89%E3%82%A4%E3%83%A1%E3%83%BC%E3%82%B8%E3%82%92push%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)
    - [GitHub連携する方法](#github%E9%80%A3%E6%90%BA%E3%81%99%E3%82%8B%E6%96%B9%E6%B3%95)
- [pytestとcoverageを実行する](#pytest%E3%81%A8coverage%E3%82%92%E5%AE%9F%E8%A1%8C%E3%81%99%E3%82%8B)
- [まとめ](#%E3%81%BE%E3%81%A8%E3%82%81)

</details>
<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## これは何か

Python言語でプログラムを自作したい。そのために環境を作り道具を揃えて使えるようにする必要がある。アプリケーションが何であれ環境と道具は概ね同じであり、繰り返し利用しつつ磨き上げていくものだ。Python初心者のわたしがやってきた準備作業を細かく記録しつつレポジトリとして保存しよう。さまざまなPythonプロジェクトの雛形として使えるだろう。

Gitレポジトリを4つ作る。

1. [PythonProjectTemplateLevel1](https://github.com/kazurayam/PythonProjectTemplateLevel1) --- Python処理系をインストールする。pipenvで仮想環境を構築する。わたし流のディレクトリ構造を決める。IntelliJ IDEAを設定する。pytestでユニットテストする。
1. [PythonProjectTemplateLevel2](https://github.com/kazurayam/PythonProjectTemplateLevel2) --- わたしのPythonコードをpipでライブラリにしてPyPIにアップロードして共有可能にする。そのライブラリを仕込んだDockerイメージを作りDocker Hubにアップロードして共有可能にする。
1. [PythonProjectTemplateLevel3](https://github.com/kazurayam/PythonProjectTemplateLevel3) --- つまりこのレポジトリ。Flaskフレームワークを使ってWebサーバアプリケーションを作る。Dockerイメージを作る。
1. [PythonProjectTemplateLevel4](https://github.com/kazurayam/PythonProjectTemplateLevel4) --- Level3で作ったWebサーバアプリのユーザインタフェースをSeleniumでテストする。Page Objectモデルで。

このプロジェクトを最初に作るにあたっては [GitHubのレポジトリテンプレート機能](https://dev.classmethod.jp/articles/github-template-repository/) を利用した。すなわちGitHubのサイトで Level2のレポジトリを Template RepositoryとするようチェックボックスをONした。そしてLevel3のレポジトリをNewするにあたって、Level2のレポジトリをTemplate Repositoryとして指定した。するとLevel2のファイルとディレクトリがコピーされて下書きとして使えるようになっていた。便利ですね。

## 前提条件

1. マシンはMac Book Air、OSは macOS 11.1 Big Sur。
1. MacにHomebrewをインストール済み、説明は省略する
1. MacにGitをインストール済み、Git Hubに自分のアカウントを持っていて、Gitの操作に熟達していると前提するので説明は省略する。
1. MacでIntelliJ IDEAを開発環境として使う。IDEAのライセンスを持っていてPythonプラグインをインストール済みと前提する。

## 達成目標

Level3では下記のことを達成目標とする。

1. Flaskフレームワークの公式サイトにある [Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial) を参照しながら、Webアプリケーションを自作する。
1. 自作したWebアプリをpipコマンドでライブラリ化する。PyPIにアップする。
1. PyPIにアップした自作ライブラリを使ってDockerイメージを作成する。DockerイメージをDocker Hubにアップする。 

自作のWebアプリのDockerイメージを作ることができれば、それを使ってどのマシンでもそのWebアプリを起動することが簡単にできるようになる。

## 手順

Python処理系のインストール、ディレクトリ構造の決定、pipenvで仮想環境を作る、IntelliJ IDEAの設定、pytestによるユニットテストの作成と実行 --- これらについては下記のLevel1のREADMEを参照のこと。

- [PythonProjectTemplateLevel1](https://github.com/kazurayam/PythonProjectTemplateLevel1) 


またpipコマンドによるパッケージ化の作業とdockerコマンドによるDockerイメージの操作に関しては下記のLevel2のREADMEを参照のこと。

- [PythonProjectTemplateLevel2](https://github.com/kazurayam/PythonProjectTemplateLevel2)

### Pipfileから仮想環境を再現する

このLevel3プロジェクトのために専用のPython仮想環境をpipenvで作ろう。Gitレポジトリから`Pipfile`と`Pipfile.lock`をローカルに取得してあると前提する。`pipenv install`コマンド一発でPipfile.lockに基づいて仮想環境を作ることができる。

```
$repos/pyproject/ $ pipenv install
Installing dependencies from Pipfile.lock (4e9768)...
  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 0/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 1/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 2/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 3/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 4/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 5/5 — 0  🐍   ▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉▉ 5/5 — 00:00:02
To activate this project's virtualenv, run pipenv shell.
Alternatively, run a command inside the virtualenv with pipenv run.
```

これによってこのLevel3プロジェクトのために新しいPython仮想環境が自動的に作られる。

なお新しいPython仮想環境をIntelliJ IDEAの設定に繁栄すべきところが、自動的には修正されない。手作業で修正する必要がある。やり方はLevel1のREADMEを参照のこと。

### Flask Tutorialを写経する

Flaskの公式ドキュメントに含まれるチュートリアルをそのまま写経した。

- [Tutorial](https://flask.palletsprojects.com/en/1.1.x/tutorial/#tutorial) 

ここに書いてある内容にわたしか付け加えることなどない。 ただし環境がちょっと違っているところがあるので要点をメモしておく。

#### flaskをPython仮想環境にインストールする

```
$ cd PythonProjectTemplateLevel3/pyproject (master *)
$ pipenv run pip install flask
```

```
Collecting flask
  Using cached Flask-1.1.2-py2.py3-none-any.whl (94 kB)
Collecting click>=5.1
  Using cached click-7.1.2-py2.py3-none-any.whl (82 kB)
Collecting Jinja2>=2.10.1
  Downloading Jinja2-2.11.3-py2.py3-none-any.whl (125 kB)
     |██▋                             | 10 kB 1.8 MB/s eta 0:     |█████▏                          | 20 kB 1.4 MB/s eta     |███████▉                        | 30 kB 1.3 MB/s e     |██████████▍                     | 40 kB 1.3 MB/     |█████████████                   | 51 kB 1.2 M     |███████████████▋                | 61 kB 1.     |██████████████████▎             | 71 kB     |████████████████████▉           | 81      |███████████████████████▌        |      |██████████████████████████           |████████████████████████████▊     |█████████████████████████████     |████████████████████████████████| 125 kB 1.2 MB/s 
Collecting Werkzeug>=0.15
  Using cached Werkzeug-1.0.1-py2.py3-none-any.whl (298 kB)
Collecting itsdangerous>=0.24
  Using cached itsdangerous-1.1.0-py2.py3-none-any.whl (16 kB)
Collecting MarkupSafe>=0.23
  Using cached MarkupSafe-1.1.1-cp38-cp38-macosx_10_9_x86_64.whl (16 kB)
Installing collected packages: MarkupSafe, Werkzeug, Jinja2, itsdangerous, click, flask
Successfully installed Jinja2-2.11.3 MarkupSafe-1.1.1 Werkzeug-1.0.1 click-7.1.2 flask-1.1.2 itsdangerous-1.1.0
```


#### .flaskenv ファイルに環境変数の設定を書く

Flaskを起動するときに環境変数 `FLASK_APP` ほかを指定しなければならないが、コマンドラインでいちいち引数として指定するのは面倒だ。その代わり `.flaskenv` ファイルに書けばいいらしい。

- https://www.pgen.info/archives/1691

[.flaskenv](pyproject/.flaskenv) ファイルを書いた。

```
FLASK_APP=src/flaskr
FLASK_ENV=development
```

#### python-dotenvをインストールする

`flaskrun`コマンドでFlaskを起動しようとした。そうしたら

```
$ pipenv run flaskrun
Loading .env environment variables...
 * Tip: There are .env or .flaskenv files present. Do "pip install python-dotenv" to use them.
...
```
`.flaskenv`ファイルからパラメータを読み込ませるのなら python-dotenv が必要だからインストールしろと言われた。python-dotenvをインストールした。

```
$ pipenv install python-dotenv
```

#### Pipfileにスクリプトを書いて起動を簡単にする

[Pipfile](pyproject/Pipfile) に `flaskrun` という名前でスクリプトを書いた。`flask run`とタイプするだけなのだが。

```
$ pipenv run flaskrun
```

すると下記のようなメッセージが表示され、flaskrアプリケーションが立ち上がったのがわかる。ブラウザで http://127.0.0.1:5000/hello を問い合わせると `Hello, World!` と応答した。

```
 * Serving Flask app "src/flaskr" (lazy loading)
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 336-613-971
```

### pytestとcoverageを実行する

pytestを実行するには
```
$ cd github
:~/github
$ cd PythonProjectTemplateLevel3
:~/github/PythonProjectTemplateLevel3 (master *+)
$ cd pyproject/
:~/github/PythonProjectTemplateLevel3/pyproject (master *+)
$ pipenv run pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/kazuakiurayama/github/PythonProjectTemplateLevel3/pyproject, configfile: setup.cfg, testpaths: tests
collected 24 items                                                             

tests/test_auth.py ........                                              [ 33%]
tests/test_blog.py ............                                          [ 83%]
tests/test_db.py ..                                                      [ 91%]
tests/test_factory.py ..                                                 [100%]

============================== 24 passed in 1.05s ==============================
:~/github/PythonProjectTemplateLevel3/pyproject (master *+)
```

これに続いてcoverageを実行するには
```
$ pipenv run coverage run -m pytest
============================= test session starts ==============================
platform darwin -- Python 3.8.5, pytest-6.2.2, py-1.10.0, pluggy-0.13.1
rootdir: /Users/kazuakiurayama/github/PythonProjectTemplateLevel3/pyproject, configfile: setup.cfg, testpaths: tests
collected 24 items                                                             

tests/test_auth.py ........                                              [ 33%]
tests/test_blog.py ............                                          [ 83%]
tests/test_db.py ..                                                      [ 91%]
tests/test_factory.py ..                                                 [100%]

============================== 24 passed in 1.22s ==============================
:~/github/PythonProjectTemplateLevel3/pyproject (master *+)

```

coverageのレポートをみるには

```
$ pipenv run coverage report
Name                     Stmts   Miss Branch BrPart  Cover
----------------------------------------------------------
src/flaskr/__init__.py      23      0      2      0   100%
src/flaskr/auth.py          59      0     22      0   100%
src/flaskr/blog.py          58      0     16      0   100%
src/flaskr/db.py            25      0      4      0   100%
src/flaskr/hello.py          5      5      0      0     0%
----------------------------------------------------------
TOTAL                      170      5     44      0    98%
```

HTML形式のレポートを生成させるには

```
$ pipenv run coverage html
```

するとhtmlcov/index.htmlファイルが生成されるからブラウザで開け。



### pipとwheelでライブラリ化してPyPIにアップロードする

[PythonProjectTemplateLevel2](https://github.com/kazurayam/PythonProjectTemplateLevel2) では

`python setup.py sdist`　でパッケージ化した。`sdist`とは *source distribution*の意味。その名の通り、Python言語で書かれたソースコードを配布する。そのため利用者が `pip install xxxxx` を実行すると利用者側で `setup.py` の記述に基づいたビルド処理が実行される。

このビルド処理が失敗しがちだ。このビルド処理がOSによって違う（Windowsで・・・）とか、Python処理系のバージョンが合わなくて・・・とか。ソースコードを配布するのでなくビルド済みのパッケージを配布するやり方があればそっちの方が良い。ここで利用されるのが [wheel](https://pythonwheels.com/) 。
>Wheels are the new standard of Python distributio and are intended to replace eggs.

wheelをインストールしよう。
```
$ pip install wheel
```

wheelをインストールすると `bdist_wheel` が使えるようになる。`sdist`ではなくてこっちでライブラリ化する。

```
$ python setup.py bdist_wheel 
```
すると `dist` ディレクトリのなかにファイル名の末尾が `.whl` のファイルができた。これが wheel形式でのライブラリファイルである。

```
$ tree .
.
├── Dockerfile
├── MANIFEST.in
├── Pipfile
├── Pipfile.lock
├── build
├── dist
│   ├── flaskr-kazurayam-1.0.0.tar.gz
│   └── flaskr_kazurayam-1.0.0-py3-none-any.whl
```

`sdist`オプションによって作られた tar.gz ファイルは削除してしまおう。`.whl`ファイルをPyPIにアップすればいい。twineコマンドで

```
(pyproject) :~/github/PythonProjectTemplateLevel3/pyproject
$ twine upload --repository pipitest dist/*
```

flaskr-kazurayamのバージョン1.0.0がTestPyPIに登録済みの状態でもう一度 `twine upload` コマンドを実行したらエラーになった。PyPIは同一バージョンを上書きすることを許さない。へえ、そうなのか。じゃあいったん削除すればよかろう。https://stackoverflow.com/questions/20403387/how-to-remove-a-package-from-pypi によれば ブラウザで https://test.pypi.org/ を開き自分のアカウントでログインして対象を選んで削除せよ、という。やってみた。削除はできた。もう一度 バージョン 1.0.0 を twine upload した。そうしたらまたエラーになった。しょうがない、setup.pyファイルに書いてあるバージョンを1.0.1に変更した。もう一度 twine upload した。 https://test.pypi.org/project/flaskr-kazurayam/1.0.1/ にアップロードできた。こうすればいいのね。わかった。

### SECRET_KEYについて

[Flask Tutorial / Deploy to Production](https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/) に **Configure the Secret Key** と題する節がある。Flaskがセッション情報を暗号化するのに使う秘密鍵 Secret Key を指定する必要があって、[`flaskr_/__init__.py](pyproject/src/flaskr/__init__.py) に或る固定的な文字列がデフォルトとして書いてある。開発者が自分のマシンでローカルにFlaskアプリを立ち上げてデバッグする場面ならデフォルト値にままでかまわない。しかしインターネットから不特定多数からのアクセスに晒される本番環境を構築する面にいたれば、SECRET_KEYを変更しなければならない。どうやればいいのか？

Tutorialの記述を読んでもよくわからなかった。sqlite3のデータベースが `venv/var/flaskr-instance` というディレクトリの中に作られると書いてるが、なんだそりゃ？ 

`venv/var/flaskr-instance/config.py` というファイルを作ってその中にSECRET_KEYを指定せと記述されてるが、Dockerコンテナ常にconfig.pyを生成するようにDockerfileを記述するのか？

ううむ、わからない。本番環境をDockerで作るについてもっと情報を集めて試行錯誤しなければならない。また後日としよう。


### Waitress

[Waitress](https://docs.pylonsproject.org/projects/waitress/en/stable/) を使う。

Waitressが何かについては

- [bottle.py+waitressでPython飲みで動作可能なWebサーバ](https://qiita.com/yoichiwo7/items/abcd87c8a8a2e027fc12)

を参照のこと。

waitressをインストールする。

```
$ pip install waitress
```

パッケージを追加したからこの場で`requirements.txt`を更新しておけ。

```
$ pip freeze > requirements.txt
```

`waitress-serve モジュール名:オブジェクト名` コマンドでwebサーバを起動する。

```
$ cd ~/github/PythonProjectTemplateLevel3/pyproject
$ pipenv run waitress-serve --host=127.0.0.1 --port=5000 --call 'src/flaskr:create_app'
Serving on http://0.0.0.0:5000
```

waitressを止めるには Ctrl+C とやれ。

### Dockerイメージを作る

MacにDocker Desktop for Macをインストール済みであると前提する。

Docker Hubにアカウントを準備してあると前提する。

[pyproject/Dockerfile](pyproject/Dockerfile) を作った。ここにはDockerイメージをを作るのに必要なDockerコマンドを記述しておく。

docker buildコマンドを実行してDockerイメージを作ろう。

```
$repos/pyproject (master *+)
$ docker build --tag kazurayam/flaskr-kazurayam:1.0.1 .

...

Successfully built 2aee34772e1a
Successfully tagged kazurayam/flaskr-kazurayam:1.0.1
```

成功した。

>Level2では `python setup.py sdist` でライブラリ化していた。Level3では `python setup.py bdist_wheel`でwheel形式のライブラリを作った。この違いによりDockerfileの書き方が影響を受けるのだろうか？と迷ったが、やってみると成功した。ってことはDockerfileの書き方には影響しない。

Dockerイメージができたことを確認するには `docker image list` コマンドを投入する。

```
$ docker image ls
REPOSITORY                       TAG          IMAGE ID       CREATED          SIZE
kazurayam/flaskr-kazurayam       1.0.1        c8ba901cc52b   58 seconds ago   173MB
kazurayam/flaskr-kazurayam       1.0.0        d9f09bea3828   18 hours ago     141MB
...
```

#### 自作したDockerイメージからDockerコンテナを起動する

私のMac上の別の適当なディレクトリにcdしてからdocker runコマンドを実行すればそこでDockerコンテナを起動することができる。やってみよう。Dockerコンテナが起動され、

```
$ cd ~/tmp
$ docker run -it --rm kazurayam/flaskr-kazurayam:1.0.1
root@5c580d014ccf:/work# 
```

できた。ではPythonで自作した `greeting` コマンドを実行してみよう。

```
root@5c580d014ccf:/work# greeting Python
Hello, Python!
root@5c580d014ccf:/work# 
```

greetingコマンドが動いた。

どんなdockerコンテナが今動いているかを見るには、別のターミナルを起動して、docker psコマンドを打つ。

```
$ docker ps
CONTAINER ID   IMAGE                           COMMAND             CREATED          STATUS          PORTS     NAMES
d036761d3325   kazurayam/mypkg-kazurayam:1.0   "/bin/sh -c bash"   12 seconds ago   Up 10 seconds             unruffled_chaplygin
```

ではDockerコンテナを終了させよう。exitすれば良い。

```
root@5c580d014ccf:/work# exit
exit
:~/tmp
```

#### Dockerコンテナを起動したらwebアプリを自動的に起動する


#### Dockerイメージの保存先

このDockerイメージの実体としてのファイルがPC/Macのどこに保存されたかはdockerコマンドが知っている。Dockerイメージを取り出すには必ずdockerコマンドを使うので、保存場所を知っておく必要はない。

ここで作ったDockerイメージをよそでも利用したければ、イメージをいったんDocker Hubにあげて共有可能な状態にせよ。別PCでdockerコマンドを実行しDocker Hubからイメージをダウンロードせよ。

#### dockerコマンドのレファレンス

dockerコンテナの作成、起動から停止までどんなコマンドを使うかについては

- [Dockerコンテナの作成、起動〜停止まで](https://qiita.com/kooohei/items/0e788a2ce8c30f9dba53)

が役に立つ。

### Docker Hubにアップロードする

自作したDockerイメージをDocker Hubにアップする手順については下記を参考にした。

- [DockerImageをDockerHubに登録する方法](https://qiita.com/kon_yu/items/7c40f4dfbd1cce006ce7)

事前にDocker Hubに自分のためのアカウントを準備しておいた。

Docker Hubにログインする
'''
$ docker login
'''

自作したイメージをpushする
```
$ docker push kazurayam/mypkg-kazurayam:1.0
The push refers to repository [docker.io/kazurayam/mypkg-kazurayam]
eabc49849837: Pushed 
02431f26c7f4: Pushed 
a19bcd8712ef: Pushed 
b475be986c39: Pushed 
424db1bab221: Pushed 
d101a5002485: Pushed 
bb52f2ddc560: Pushed 
f001ccd77806: Pushed 
24284177bf76: Mounted from library/python 
b64b3bf8eaca: Mounted from library/python 
ba441d17b790: Mounted from library/python 
477e7db04777: Mounted from library/python 
cb42413394c4: Mounted from library/python 
1.0: digest: sha256:7f297987f71f28d6f1ad3cf839ac355118a59e623dece42b55a3dc15a5ee2774 size: 3033
:~
```

できた。ブラウザで https://hub.docker.com/ を開き、自分のアカウントでログインすれば、今アップしたDockerイメージがたしかにDocker Hubに格納されているのがわかる。

![onDockerHub](docs/images/onDockerHub.png)


## まとめ

以上でLevel3は完了。つまり

1. FlaskのTutorialを写経して flaskr アプリを作った。 
1. Tutorialには pytestによるユニットテストのサンプルコードが書いてあった。丁寧に写経した。
1. 自分のflaskrアプリをpipでライブラリ化し、PyPIにアップした。
1. Dockerイメージを作った。
   
写経したflaskrアプリがDockerコンテナで動くことを確認した。
