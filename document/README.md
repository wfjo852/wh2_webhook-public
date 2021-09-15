# 실행 순서

## docker-compose up -d
docker-compose up
build 후 docker-compose 실행됨

---

# wh2_script
docker/init/flask_uwsgi/src/wh2_script : 최초 설정용
wh2_script>> wh2hook_script:/www/src/wh2_script : 볼륨으로 연결되어 있음

## python에 설치된 모듈
```
pip install requests
pip install wh2api
pip install Flask
pip install uwsgi
```
