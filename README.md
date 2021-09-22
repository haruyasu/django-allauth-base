# 画像認識システム

## django 起動コマンド

```
python3 manage.py runserver
```

## radis インストール

```
sudo apt install redis-server
```

## radis 起動コマンド

```
sudo service redis-server start
```

## celery 起動コマンド

```
celery -A mysite worker --pool solo -l info
```

## celery バックグラウンド

```
celery -A mysite worker --pool solo -l info --detach
celery -A mysite worker --pool solo -l info -f celery.log --detach
```

## celery 　動作停止

バックグラウンド制御を止める

```
ps aux|grep celery
sudo kill -9 2870
```

## データベース

.env

開発用

```
DATABASE_URL=sqlite:///db.sqlite3
```

本番環境用

```
DATABASE_URL=postgres://coloruser:colorpassword@localhost:/colordb
```

## サービス

```
sudo systemctl restart color_identifier
sudo systemctl status color_identifier
```
# django-allauth-base
