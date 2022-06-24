# Oral Experts SGCD

Sistema gestor de clínica dental realizado con django

## Instalación

Necesitarás [python](https://www.python.org/downloads/).

Una vez tengamos pip (viene con python) instalamos el entorno virtual de nuestra preferencia.

### Usando pipenv:
Instalamos pipenv:
```bash
pip install pipenv
```

Levantamos el entorno virtual ***dentro de la carpeta del proyecto***:
```bash
pipenv shell
```

Instalamos las librerías del proyecto con:
```bash
pipenv install
```

Migrando la BD del proyecto:
```bash
py manage.py migrate 
```

Creamos el administrador:
```bash
py manage.py createsuperuser
```

Ejecutamos el proyecto (local):
py manage.py runserver 

***Nota:*** *asegurarse de estar dentro del shell de pipenv al momento de realizar la compilacion del proyecto*

## Además

Más información será añadida posteriormente.