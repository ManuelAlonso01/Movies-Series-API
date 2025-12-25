# 🎬 Movie & Series API (Django)

Este es un proyecto de backend para gestionar un catálogo de películas y series, desarrollado con **Django Rest Framework**.

## 🚀 Funcionalidades
- **CRUD Completo:** Listar, crear, actualizar y eliminar películas/series.
- **Filtros:** Búsqueda por ID.
- **Seguridad:** Implementación de `permission_classes` para proteger los endpoints.

## 🛠️ Instalación
1. Clona el repositorio.
2. Crea un entorno virtual: `python -m venv venv`.
3. Activa el entorno:
```bash
   - Windows: `.\venv\Scripts\activate`
   - Linux/Mac: `source venv/bin/activate`
```
4. Instala las dependencias: `pip install django djangorestframework`.
5. Ejecuta las migraciones: `python manage.py migrate`.
6. Crea un usuario administrador: `python manage.py createsuperuser`.
7. Ejecuta el servidor: `python manage.py runserver`.

## 📌 Endpoints Principales
- ```GET /movies/```: Lista todas las películas.
- ```GET /series/```: Lista todas las series.
- ```GET /movies/<id>/```: Muestra la película con ese id.
- ```GET /series/<id>/```: Muestra la serie con ese id.
- **SOLO ADMIN**
- ```POST /movies/create/```: Crea una pelicula con los datos enviados en el JSON.
- ```POST /series/create/```: Crea una serie con los datos enviados en el JSON.
- ```PATCH /movies/update/<id>/```: Actualiza una película.
- ```PATCH /series/update/<id>/```: Actualiza una serie.
- ```DELETE /movies/delete/<id>/```: Elimina la película con ese id.
- ```DELETE /series/delete/<id>/```: Elimina la serie con ese id.

## ✒️ Autor
- Manuel - (https://github.com/ManuelAlonso01)