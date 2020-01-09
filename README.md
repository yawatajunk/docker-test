# docker-test
WordPress + MySQL + phpMyAdmin + WSGI + HTTPS on Docker

## Environments
* Mac: macOS 10.15.2 Catalina
* Docker Desktop for Mac: 2.1.0.5(40693)
* Docker Engine:  10.03.5
* Docker Compose: 1.24.1
* Homebrew: 2.2.2

## How to build docker containers
```
git clone https://github.com/yawatajunk/docker-test.git
cd docker-test
docker-compose build
```
## How to make locally-trusted certificates
```
brew install mkcert # if not installed yet
mkcert -install
mkcert -cert-file https-portal/cert/localhost.pem -key-file https-portal/cert/localhost-key.pem localhost
```

## How to launch docker containers
```
docker-compose up -d
```

## URLs
* MySQL(phpMyAdmin): http://localhost:8081/
* WordPress : https://localhost

## How to remove docker containers
```
docker-compose down
```
