## Name
Financial Movement
## Intro

Esse App cria uma interface web onde você pode fazer o upload de um arquivo CNAB em .txt. Será retornado na tela os estabelecimentos, seus donos e o resultado final dos lançamentos de despesas e receitas.

## Criando ambiente virtual 

```shell
python3 -m venv venv

source venv/bin/activate

pip install djangorestframework black ipdb pycodestyle

pip freeze > requirements.txt

python3 manage.py makemigrations

python3 manage.py migrate

```

## Rodar o Projeto

```shell
python3 manage.py runserver
```


O projeto vai rodar no http://127.0.0.1:8000/api/upload_file/.
Abra [http://127.0.0.1:8000/api/upload_file/] no navegador para visualizar.

## Ferramentas e principais bibliotecas utilizadas

- Python3 
- Django
- HTML
