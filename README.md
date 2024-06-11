# projetoSI
Este projeto é feito em python e hospedado através do docker. É utilizada a biblioteca flask

# Primeiros passos

Criar uma instância EC2 na AWS:(Ubuntu) (Opcional, também é possível rodar localmente)

## Atualize sua instancia:

```shell
sudo apt update
```

## Intalação do Docker:

```shell
# Adicione a chave do Docker:

sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc

# Adicione o repositório:
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```

# Contruir e iniciar serviços (Backend, Frontend e banco de dados)


#### Parar e iniciar todos os serviços definidos no arquivo docker-compose.yml


```shell
docker-compose down
```


#### Construir e iniciar todos os serviços definidos no arquivo docker-compose.yml



