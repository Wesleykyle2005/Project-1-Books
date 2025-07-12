# Project 1 - Biblioteca Web

Web Programming with Python and JavaScript

## Descripción

Este proyecto es una aplicación web para buscar libros, ver detalles, dejar reseñas y gestionar usuarios. Utiliza Flask, SQLAlchemy y la API de Google Books. Puedes usar una base de datos PostgreSQL (recomendado para producción) o SQLite (más sencillo para pruebas locales).

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

#### 1. Crea una cuenta en [Render.com](https://render.com/)
#### 2. Ve a "Dashboard" > "New" > "PostgreSQL"
#### 3. Ponle un nombre a tu base de datos y crea el servicio
#### 4. Copia la URL de conexión (formato: `postgresql://usuario:contraseña@host:puerto/nombre_db`)
#### 5. En tu terminal, configura la variable de entorno:

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
- Si la base de datos está vacía, se llenará automáticamente con los datos de `books.csv`.
- Puedes crear una cuenta nueva desde la web.
- Las búsquedas pueden hacerse por ISBN, título o autor.
- Solo puedes dejar una reseña por libro y no es editable.

---

## Ejemplo: Crear base de datos PostgreSQL en Render.com

1. Ingresa a [Render.com](https://render.com/).
2. Haz clic en "New" > "PostgreSQL".
3. Elige un nombre y región para tu base de datos.
4. Espera a que Render cree la base de datos.
5. Copia la URL de conexión (aparece en la sección "Connection")
6. En tu terminal, ejecuta:
   ```powershell
   $env:DATABASE_URL = "<tu_url_de_conexion>"
   ```
7. Ejecuta el proyecto normalmente. Las tablas y datos se crearán automáticamente.

---

## Notas
- Si usas SQLite, no necesitas crear nada en Render.
- Si usas PostgreSQL, asegúrate de que la URL esté bien escrita y que tu IP tenga acceso (Render lo permite por defecto).
- Si tienes problemas, revisa los mensajes de error en la terminal.

---

¿Dudas? ¡Abre un issue o pregunta! 😉

