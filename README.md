# projetoSI
Este projeto é feito em python e hospedado através do docker. É utilizada a biblioteca flask

# Primeiros passos

## Criar uma instância Ubunto EC2 na AWS: 

Passo opcional, também é possível rodar localmente

## Atualizar o indíce de pacotes APT:

```shell
sudo apt update
```

## Intalação do Docker:

```shell

# Instala os pacotes necessários para permitir o uso de repositórios via HTTPS
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common

# Adiciona a chave GPG oficial do Docker
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

#Adicione o repositório do Docker às fontes APT
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Atualiza o índice de pacotes novamente
sudo apt-get update

# Verifica que a instalação está sendo feita a partir do repositório Docker em vez do repositório padrão do Ubuntu
apt-cache policy docker-ce 

# Instala o Docker
sudo apt-get install docker-ce 

# Verifica que o Docker está funcionando
sudo systemctl status docker 


```


## Instalação do Docker Compose

```shell

# Baixa a versão mais recente do Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep tag_name | cut -d '"' -f 4)/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose


# Aplica as permissões executáveis ao binário
sudo chmod +x /usr/local/bin/docker-compose


# Verifica a instalação
docker-compose --version


```

# Configurar e rodar o Projeto

## Clonar repositório

```shell
#instalar git, caso não tenha instalado

sudo apt-get update 
sudo apt-get install git
# Clonar repositório
git clone https://github.com/michelesm/projetoSI.git

```


# Construir e iniciar serviços (Backend, Frontend e banco de dados) 

Cada serviço pode ter sua imagem e container criados individualmente(um por vez), ou atravez do docker composer, que permite definir múltiplos serviços (cada um rodando em um contêiner) em um único arquivo docker-compose.yml

## Iniciando INDIVIDUALMENTE

### Construir e Rodar o Contêiner do Frontend

#### Navegar para o diretório do frontend e construir a imagem:

```shell
cd ./frontend
docker build -t myapp-frontend .
```

#### Rodar o contêiner do frontend:

```shell
docker run -d \
  --name myapp-frontend \
  -p 3000:8080 \
  -v $(pwd):/app \
  -e FLASK_APP=/app/server.py \
  -e FLASK_ENV=development \
  -e API_URL=http://myapp-backend:8080 \
  myapp-frontend
```

### Construir e Rodar o Contêiner do Backend

#### Navegar para o diretório do backend e construir a imagem:
```shell
cd ../backend
docker build -t myapp-backend .
```

#### Rodar o contêiner do backend:
```shell
docker run -d \
  --name myapp-backend \
  -p 5000:8080 \
  -v $(pwd):/app \
  -e FLASK_APP=/app/server.py \
  -e FLASK_ENV=development \
  -e MYSQL_HOST=myapp-db \
  -e MYSQL_ROOT_PASSWORD=myapp321 \
  -e MYSQL_USER=root \
  -e MYSQL_DATABASE=myapp \
  myapp-backend
```

### Construir e Rodar o Contêiner do MySQL

#### Navegar para o diretório do MySQL e construir a imagem:
```shell
cd ../mysql
docker build -t myapp-db .
```

#### Rodar o contêiner do MySQL:
```shell
docker run -d \
  --hostname myapp-db \
  --name myapp-db \
  --restart always \
  -e MYSQL_ROOT_PASSWORD=myapp321 \
  -e MYSQL_DATABASE=myapp \
  myapp-db
```

### Configurar a Rede

Para que os contêineres possam se comunicar uns com os outros é necessário criar uma rede Docker personalizada e conectar os contêineres a essa rede.

#### Criar uma rede personalizada:
```shell
docker network create myapp-network
```

#### Conectar os contêineres à rede personalizada:
```shell
docker network connect myapp-network myapp-frontend
docker network connect myapp-network myapp-backend
docker network connect myapp-network myapp-db
```


## Iniciando serviços via Docker compose

```shell
# Acessar diretório do projeto

cd projetoSI 

```

### Parar e remover contêineres, redes personalizadas e volumes anônimos criados anteriormente

```shell
docker-compose down
```
Este comando é útil para limpar o ambiente Docker criado por um projeto Docker Compose, garantindo que não fiquem contêineres ou redes residuais.

### Construir e iniciar todos os serviços definidos no arquivo docker-compose.yml


```shell
docker-compose up --builder
```

O comando docker-compose up --build força a reconstrução das imagens definidas no arquivo docker-compose.yml antes de criar e iniciar os contêineres correspondentes. É especialmente útil para garantir que qualquer mudança no Dockerfile ou nas dependências do projeto seja incluída nos contêineres em execução.


# Kubernets

O diretório helms possui a estruturação para que os serviços sejam executados via kubernets ao invés do docker compose
