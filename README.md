# Klarna Math API exercise

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
git clone https://github.com/ochirkov/klarna_repo.git
cd klarna_repo
```

Start Klarna env

```bash
docker-compose up -d
```

Make sure that you have next ports exposed on your host instance:
 * 5000 - Klarna API port
 * 5601 - Kibana port
 
## Monitoring
There is filebeat in docker-compose which has access to **/var/lib/docker** folder which contains logs for 
all containers on OS. 
Main idea that Klarna API write logs to stdout and **Filebeat** reads them and sends to **Elasticsearch**.

It is the same approach how K8S centralized logging commonly organized.
As other possible workarounds could be:
 * send jsonified logs by TCP/UDP to Logstash and Logstash injects them to Elasticsearch
 * send StatsD metrics to StatsD server and Grafana reads those metrics and alerts if needed.... 
 * many possible solutions could be implemented here.
 

Klarna API requests examples:
```bash
curl 'http://127.0.0.1:5000/?func=fibonacci&n=5'
{
  "data": 5, 
  "message": "fibonacci counted successfully"
}

curl 'http://127.0.0.1:5000/?func=fibonacci&n=-3'
{
  "data": "", 
  "message": "n value should be greater or equal zero"
}

curl 'http://127.0.0.1:5000/?func=factorial&n=5'
{
  "data": 120, 
  "message": "factorial counted successfully"
}

curl 'http://127.0.0.1:5000/?func=factorial&n=-4'
{
  "data": "", 
  "message": "n value should be greater or equal zero"
}

curl 'http://127.0.0.1:5000/?func=ackermann&m=1&n=1'
{
  "data": 3, 
  "message": "ackermann counted successfully"
}
```

Navigate Kibana saved objects on http://20.105.251.86:5601/app/kibana#/management/kibana/objects?_g=()  or 
http://127.0.0.1:5601/app/kibana#/management/kibana/objects?_g=() if you work on local instance.

Press import and choose export.ndjson file from sources and press import.

It will add predefined Kibana dashboard with visuailizations.

## Tests

Run flake8 and unit tests:
```bash
docker build -t klarna .
docker run klarna flake8
docker run klarna nose2
```

## Deploy in AWS Cloud
Simplest way to deploy this App into AWS is to use Lambda and API Gateway.
If we have no huge load on our API it is reasonable to use Lambda.
 * In case of Lambda we pay only for run time.
 * Lambda allows us to use runtime which we are comfortable (one team can use Python for Fibonacci endpoint and another  team PHP for Factorial. )
 * API Gateway allows us avoid different frameworks and solve REST approach by infra tools only
