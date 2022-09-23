# Blog

Esse projeto foi criado para o aprendizado do framework Django.

## 🚀 Começando

Essas instruções permitirão que você obtenha uma cópia do projeto em operação na sua máquina local para fins de desenvolvimento e teste.

Consulte **[Implantação](#-implanta%C3%A7%C3%A3o)** para saber como implantar o projeto.

### 📋 Pré-requisitos

De que coisas você precisa para instalar o software e como instalá-lo?

```
Necessário ter o Visual Studio Code instalado, ou Pycharm ou qualquer editor de código fonte
```

### 🔧 Instalação

Uma série de exemplos passo-a-passo que informam o que você deve executar para ter um ambiente de desenvolvimento em execução.

Supondo que já tenha o ambiente de desenvolvimento preparado, instale as dependências com o seguinte comando:

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

## ⚙️ Executando os testes

Para executar os testes automatizados, abra o terminal e digite:

```
python manage.py test
```

## 🛠️ Construído com

Todas as ferramentas que forma usadas para o desenvolvimento desse projeto.

* [Django](https://www.djangoproject.com/) - O framework web usado