FROM python

ADD . /www
WORKDIR /www

RUN python -m pip install --upgrade pip
RUN pip install requests
RUN pip install wh2api
RUN pip install Flask
RUN pip install uwsgi
RUN pip install selenium

CMD uwsgi uwsgi.ini