# Math API exercise

## Environment
Python 3.9
Linux Ubuntu 18.04-LTS
docker-compose 3.9
Docker version 20.10.11


## Prepare env
Install docker
```bash
sudo apt-get update

sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

sudo apt-get update -y
sudo apt-get install docker-ce -y
```

Install docker-compose
```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo ln -s /usr/local/bin/docker-compose /usr/bin/docker-compose
```

Clone repo with sources

```bash
cd
git clone https://github.com/ochirkov/microservice1.git
cd microservice1
```

Start env

```bash
docker-compose up -d
```

Make sure that you have next ports exposed on your host instance:
 * 5000 - API port

## Tests

Run flake8 and unit tests:
```bash
docker build -t microservice1 .
docker run klarna flake8
docker run klarna nose2
```
