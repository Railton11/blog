# Blog

Esse projeto foi criado para o aprendizado do framework Django.


Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.


Pré-requisitos para rodar o projeto.

```
Necessário ter o Visual Studio Code instalado, ou Pycharm ou qualquer editor de código fonte
```


Supondo que já tenha o ambiente de desenvolvimento preparado, instale os requisitos.

Instale as dependências:

```
pip install -r requirements.txt
```

Crie o arquivo .env e o configure:

```
SECRET_KEY= Digite uma chave secreta
DEBUG=True
ALLOWED_HOSTS="*"
EMAIL_USE_TLS=False
EMAIL_HOST=localhost
EMAIL_HOST_USER= Digite um e-mail
EMAIL_HOST_PASSWORD= Digite uma senha
EMAIL_PORT=1025
```

Rode as migrações no terminal:

```
python manage.py makemigrations
python manage.py migrate
```

Crie um super usuário:

```
python manage.py createsuperuser
```

Demonstração:

```
python manage.py runserver
```

Abra o browser e acesse:

```
localhost:8000
```


Para executar os testes automatizados, abra o terminal e digite:

```
python manage.py test
```


Todas as ferramentas que foram usados para o desenvolvimento desse projeto.

* [Django](https://www.djangoproject.com/) - O framework web usado