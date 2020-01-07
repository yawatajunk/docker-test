# ベースとなるDockerイメージ
FROM wordpress:5.3.2-php7.2-apache

# ホストのファイルをコンテナへコピー
COPY my-php.ini /usr/local/etc/php/conf.d/my-php.ini
COPY my-apache.conf /etc/apache2/conf-available/my-apache.conf
COPY requirements.txt /root
COPY webapp.py /var/www/wsgi/webapp.py

# Pythonとwsgi関連のパッケージをインストール
RUN apt-get update
RUN apt-get install -y python3 python3-pip libapache2-mod-wsgi-py3

# pythonモジュールをインストール
RUN pip3 install -r /root/requirements.txt

# Apacheのユーザ設定を有効化
RUN a2enconf my-apache.conf
