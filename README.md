# Wh2-WebHook Setting
## Docker install -- centos 7이상
**자세한 설명은 [docker install](https://docs.docker.com/engine/install/centos/)에 있습니다.**

Centos는 Root를 기준으로 설명 되어 있습니다.
### Set up the repository
도커의 리포지토리를 추가합니다. 

```shell script
 yum install -y yum-utils
 yum-config-manager \
    --add-repo \
    https://download.docker.com/linux/centos/docker-ce.repo
```

### Install Docker
최신버젼으로 설치 시
```shell script
 yum install docker-ce docker-ce-cli containerd.io
```
특정 버젼으로 설치 시 
```shell script
yum install docker-ce-<VERSION_STRING> docker-ce-cli-<VERSION_STRING> containerd.io
```

### Docker Start 및 Docker 자동 실행 세팅
```shell script
systemctl start docker
systemctl enable docker
```
---

## Docker-compose
**Docker Compose는 여러개의 컨테이너를 연동시켜주는 기능을 합니다.
 자세한 설명은 [docker-compose install](https://docs.docker.com/compose/install/)에 있습니다.**


### Install Docker-cmpose
```shell script
curl -L "https://github.com/docker/compose/releases/download/1.23.1/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

### Docker-compose 설치 확인
```shell script
docker-compose --version
'docker-compose version 1.29.2, build 1110ad01'
```

---

# python Flask 설치법
모든 버젼은 최신버전이 설치 됩니다.

### C2Monster 제공 코드 다운로드
```shell script
cd /home
git clone https://github.com/wfjo852/wh2-webhook-public.git

``` 

### python의 Flask Server Run
```shell script
cd /home/wh2-webhook-public/docker
docker-compose up
``` 
### 종료를 원할때 명령어
```shell script
cd /home/wh2-webhook-public/docker
docker-compose down
```

# WebHook Check

## WebHook Test(IP)
** 웹 브라우져에 [http://{Webhook Server ip}/ip]()로 접속 하면 접속한 사람의 IP를 브라우져에 띄워 주는걸 확인 할 수 있습니다. **


## WebHook Test(Wormhole Monitor)
** 웹훅이 제대로 작동 되고 있는지 확인하는 예시 **
1. 웜홀 >> system infomation >> Webhook server에 들어가서 ADD 후 [http://{Webhook Server ip}/monitor]()를 입력
2. 트리거 세팅을 원하는 것으로 체크하고 저장 한다.  

## WebHook Test(Wormhole Hook)
** 웹훅이 작동될때 스크립트가 작동 시키는 예시 **
1. 웜홀 >> system infomation >> Webhook server에 들어가서 ADD 후 [http://{Webhook Server ip}/hook]()를 입력
2. 트리거 세팅을 원하는 것으로 체크하고 저장한다.
3. 파이썬 스크립트를 작성해서 넣는다.
4. 실행 시키면 스크립트가 실행되며 자동으로 처리된다. 
  


# Fileserver <> Mount Test

### 필요 패키지설치
```shell script
yum install cifs-utils
```

### 마운트 명령어
** 파일서버 마다 세팅이 다를 수 있음 **
```shell script
mount -t cifs {파일서버 경로} /home/wh2-webhook-public/nas_mount/ -o user='{ID}',sec=utlm,vers=1.0
```



