
### 管理サイト
Adminuser: root

# 開発フロー
1. Modelの実装
  - DBのデータ構造  

1. views.pyからtemplateへの渡すデータの加工
1. templateの作成(HTML/CSS/JS)
1. URL設計
  - urls.pyの実装

## modelの実装
* DBテーブルの作成
```
$ python manage.py migrate
```

* Modelの実装
  - models.pyを編集する

* DBのマイグレーション
1. 変更の抽出
```
$ python manage.py makemigrations
```
1. DBへの反映
```
$ python manage.py migrate
```

## templateの作成
* プロジェクト直下にstaticディレクトリを作成する
```
mkdir wish/static
```

* bootstrap, jqueryを配置
```
static
├── css
│   ├── bootstrap-theme.css
│   ├── bootstrap-theme.css.map
│   ├── bootstrap-theme.min.css
│   ├── bootstrap-theme.min.css.map
│   ├── bootstrap.css
│   ├── bootstrap.css.map
│   ├── bootstrap.min.css
│   └── bootstrap.min.css.map
├── fonts
│   ├── glyphicons-halflings-regular.eot
│   ├── glyphicons-halflings-regular.svg
│   ├── glyphicons-halflings-regular.ttf
│   ├── glyphicons-halflings-regular.woff
│   └── glyphicons-halflings-regular.woff2
└── js
    ├── .jquery-3.2.1.min.js.un~
    ├── bootstrap.js
    ├── bootstrap.min.js
    ├── jquery-3.2.1.min.js
    └── npm.js
```

* settings.pyに設定を追記
```
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
)
```

* フォームHTMLのインストール
```
$ pip install django-bootstrap-form
```

* settings.pyに'bootstrapform'を追加
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrapform',
    'wishapp',
]
```
