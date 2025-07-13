# Project 1 - Biblioteca Web

Web Programming with Python and JavaScript

## Inspiración y diferencias

Este proyecto está inspirado en el [Project 1 de CS50W](https://docs.cs50.net/ocw/web/projects/1/project1.html).

**Diferencias principales:**
- El proyecto del enlace pide el uso de Heroku para la base de datos y la API de Goodreads para ratings externos.
- En este proyecto se utiliza Render.com para la base de datos y la API de Google Books, porque **una versión anterior del proyecto original pedía exactamente esos requisitos** (Render y Google Books). Por eso, las diferencias con esa versión son mínimas y solo afectan detalles menores de integración y presentación.

---

## Descripción

Este proyecto es una aplicación web para buscar libros, ver detalles, dejar reseñas y gestionar usuarios. Utiliza Flask, SQLAlchemy y la API de Google Books. Puedes usar una base de datos PostgreSQL (recomendado para producción) o SQLite (más sencillo para pruebas locales).

---

## Capturas de pantalla

A continuación se muestran algunas capturas de pantalla de la aplicación en diferentes vistas y modos:

- **Pantalla de búsqueda (modo claro):**
  ![Pantalla de búsqueda modo claro](static/images/search_light.png)

- **Pantalla de búsqueda (modo oscuro):**
  ![Pantalla de búsqueda modo oscuro](static/images/search_black.png)

- **Pantalla de login (modo claro):**
  ![Pantalla de login modo claro](static/images/login.png)

- **Pantalla de login (modo oscuro):**
  ![Pantalla de login modo oscuro](static/images/login_black.png)

- **Pantalla de registro:**
  ![Pantalla de registro](static/images/register.png)

---

## Estructura del proyecto

- `application.py`: Lógica principal de la aplicación Flask
- `database.py`: Modelos y configuración de la base de datos
- `import.py`: Script para importar libros desde CSV (debes ejecutarlo manualmente para cargar los datos iniciales)
- `drop_all.py`: Script para eliminar todas las tablas
- `static/`: Archivos estáticos (CSS, imágenes, JS)
- `templates/`: Plantillas HTML Jinja2
- `books.csv`: Datos de libros de ejemplo
- `requirements.txt`: Dependencias del proyecto

---

## Requisitos previos
- Python 3.x
- pip
- (Opcional) Cuenta en [Render.com](https://render.com/) para base de datos PostgreSQL gratuita

---

## 1. Crear y activar entorno virtual

```powershell
python -m venv mientorno
mientorno\Scripts\activate
```

---

## 2. Instalar dependencias

```powershell
pip install -r requirements.txt
pip install flask_wtf
```

---

## 3. Configurar variables de entorno

### Opción A: Usar SQLite (más fácil para pruebas locales)
No necesitas configurar `DATABASE_URL`. El proyecto puede configurarse para usar SQLite editando `application.py`:

```python
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///libros.db"
```

### Opción B: Usar PostgreSQL en Render.com

1. Crea una cuenta en [Render.com](https://render.com/)
2. Ve a "Dashboard" > "New" > "PostgreSQL"
3. Ponle un nombre a tu base de datos y crea el servicio
4. Copia la URL de conexión (formato: `postgresql://usuario:contraseña@host:puerto/nombre_db`)
5. En tu terminal, configura la variable de entorno:

```powershell
$env:DATABASE_URL = "<tu_url_de_conexion>"
```

---

## 4. Otras variables de entorno necesarias

```powershell
$env:API_KEY = "<tu_api_key_de_google_books>"
$env:FLASK_APP = "application.py"
$env:SECRETKEY = "clavesecreta"
$env:FLASK_DEBUG = 1
```

---

## 5. Ejecutar la aplicación

```powershell
flask run
```
O bien:
```powershell
python application.py
```

---

## 6. Primer uso
- Si la base de datos está vacía, **debes ejecutar manualmente** el script `import.py` para cargar los datos de `books.csv`:

```powershell
python import.py
```

- Puedes crear una cuenta nueva desde la web.
- Las búsquedas pueden hacerse por ISBN, título o autor.
- Solo puedes dejar una reseña por libro y no es editable.
