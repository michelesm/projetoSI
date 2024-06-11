# projetoSI
Este projeto é feito em python e hospedado através do docker. É utilizada a biblioteca flask

# Primeiros passos

## Criar uma instância Ubunto EC2 na AWS: 

Passo opcional, também é possível rodar localmente

## Atualize o indíce de pacotes APT:

```shell
sudo apt update
```

## Intalação do Docker:

```shell

sudo apt-get install apt-transport-https ca-certificates curl software-properties-common # Instala os pacotes necessários para permitir o uso de repositórios via HTTPS
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add - #Adiciona a chave GPG oficial do Docker
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" # Adiciona o repositório do Docker às fontes APT
sudo apt-get update # Atualiza o índice de pacotes novamente
sudo apt-get install docker-ce #está instalando a partir do repositório Docker em vez do repositório padrão do Ubuntu
sudo systemctl status docker # Instale o Docker


```

# Contruir e iniciar serviços (Backend, Frontend e banco de dados)


#### Parar e remove contêineres, redes personalizadas e volumes anônimos criados anteriormente

Este comando é útil para limpar o ambiente Docker criado por um projeto Docker Compose, garantindo que não fiquem contêineres ou redes residuais.

```shell
docker-compose down
```


#### Construir e iniciar todos os serviços definidos no arquivo docker-compose.yml


```shell
docker-compose up --builder
```

O comando docker-compose up --build força a reconstrução das imagens definidas no arquivo docker-compose.yml antes de criar e iniciar os contêineres correspondentes. É especialmente útil para garantir que qualquer mudança no Dockerfile ou nas dependências do projeto seja incluída nos contêineres em execução.


