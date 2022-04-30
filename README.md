# api-visie
API para avaliação de teste prático da visie feito em Flask. 

## Executar aplicação usando Docker

#### Criando a imagem
```
docker build -t api-visie . 
```
#### Executar
```
docker run -d --name api-visie -p 80:5000 api-visie
```

## Instalação e configuração manual

#### Criar o env e instalando as dependencias.
```
python3 -m venv env
pip install -r requirements.txt
```
### Crie os arquivos .env e settings.toml

#### Exemplo de .env 
```
export FLASK_ENV='production'
export FLASK_APP='./api_visie/app.py'
```
#### Exemplo de settings.toml
```
[default]
SQLALCHEMY_DATABASE_URI = 'sqlite:///./test.db'

[production]

SQLALCHEMY_DATABASE_URI = 'mariadb+pymysql://USER:PASSWORD@HOSTNAME:PORT/DATABASE'
```

## Criando o banco de dados pelo CLI

#### Criar o Banco de dados
```
flask create_db
```
#### Popular o Banco de dados
```
flask populate_db 
```
#### Deletar o Banco de dados
```
flask drop_db
```
## Executar manualmente
```
cd  api_visie
flask run
```

