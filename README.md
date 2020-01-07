# docker-test
WordPress + MySQL + phpMyAdmin + WSGI on Docker

## Environments
* Mac: macOS 10.15.2 Catalina
* Docker Desktop for Mac: 2.1.0.5(40693)
* Docker Engine:  10.03.5<br>
* Docker Compose: 1.24.1<br>

## How to build docker containers
```
git clone https://github.com/yawatajunk/docker-test.git
cd docker-test
docker-compose build
```

## How to launch docker containers
```
docker-compose up -d
```

## URLs
* MySQL: http://localhost:8081/<br>
* WordPress : http://localhost:8080/<br>

## How to remove docker containers
```
docker-compose down
```
