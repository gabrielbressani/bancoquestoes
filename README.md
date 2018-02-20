# Banco de Questões

## Sobre

Pequeno projeto para cadastrar questões dos tipos Objetiva e Discursiva

## Iniciando

1. Tenha certeza de ter um interpretador do [Python](https://www.python.org/) e o [git](https://git-scm.com/) instalados.
2. No terminal, clone o repositório

    ```
    git clone https://github.com/mcmacedo/bancoquestoes.git
    ```

3. Navegue até a pasta raiz do projeto

    ```
    cd ./bancoquestoes
    ```
   
4. Crie um ambiente virtual e instale as dependências do projeto

    ```
    mkvirtualenv venv
    pip install -r requirements.txt
    ```

5. Rode o comando de migrate e o de runserver

    ```
    python manage.py migrate
    python manage.py runserver
    ```

## API

A Api responde nas seguintes urls base

- /api/v1/objetivas/ - GET, POST
- /api/v1/objetivas/pk/ - PUT, DELETE, GET
- /api/v1/dicursivas/ - GET, POST
- /api/v1/dicursivas/pk/ - PUT, DELETE, GET

Você pode utilizar o wget para realizar uma chamda à API, por exemplo:

```
    sudo apt-get update
    sudo apt-get install wget
    
    wget http://localhost:8000/api/v1/objetivas/
```

## Autenticação
Os dados já estão presentes no banco de dados

```
user = user_default
pass = django_user
```

## License
Licensed under the [Beerware license revision 43](https://pt.wikipedia.org/wiki/Beerware).
