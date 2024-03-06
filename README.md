# Tercer-pre-entrega-Toro

## Un poco del proyecto
  Este proyecto lo creo como tercer pre entrega que hago en mi curso de Python en Coder House. Estoy utilziando la version de Python 3.12.1 con el framework de Django version 5.0.2

### Orden para probar mi servidor

 1. En la terminal de VSC parado en ProyectoCerveza ingreso `python manage.py makemigrations`
 2. Luego tengo que hacer la migración `python manage.py migrate`
 3. Para correr el servidor ingreso `python manage.py runserver`

### Urls diponibles en mi servidor (copiar completo, desde el 1 hasta el ultimo slash /)

#### Inicio: 
- *127.0.0.1:8000/bebidas/*

#### Buscar: 
- Cervezas: *127.0.0.1:8000/bebidas/buscar_cerveza/*
- Mezcales: *127.0.0.1:8000/bebidas/buscar_mezcal/*
- Ginebras: *127.0.0.1:8000/bebidas/buscar_ginebra/*

#### Cargar:
- Cervezas: *127.0.0.1:8000/bebidas/cargar_cerveza/*
- Mezcales: *127.0.0.1:8000/bebidas/cargar_mezcal/*
- Ginebras: *127.0.0.1:8000/bebidas/cargar_ginebra/*

#### Ver bebidas cargadas en mi BD:
- Cervezas: *127.0.0.1:8000/bebidas/resultados_cerveza/*
- Mezcales: *127.0.0.1:8000/bebidas/resultados_mezcal/*
- Ginebras: *127.0.0.1:8000/bebidas/resultados_ginebra/*
