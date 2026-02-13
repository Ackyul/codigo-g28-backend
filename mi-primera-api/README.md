# Mi Primera API - Sistema de Gestión de Tareas

API REST desarrollada con Flask para la gestión de tareas con autenticación de usuarios.

## 📋 Descripción

Esta es una API RESTful que permite a los usuarios registrarse, iniciar sesión y gestionar sus tareas personales. Cada usuario puede crear, leer, actualizar y eliminar sus propias tareas de forma segura.

## 🚀 Características

- ✅ Autenticación de usuarios (registro y login)
- ✅ Gestión completa de tareas (CRUD)
- ✅ Relación entre usuarios y tareas
- ✅ Sesiones de usuario
- ✅ Contraseñas encriptadas
- ✅ Base de datos PostgreSQL
- ✅ Migraciones de base de datos con Flask-Migrate

## 🛠️ Tecnologías

- **Flask** - Framework web
- **SQLAlchemy** - ORM para base de datos
- **PostgreSQL** - Base de datos
- **Flask-Migrate** - Migraciones de base de datos
- **Werkzeug** - Encriptación de contraseñas
- **python-dotenv** - Gestión de variables de entorno

## 📦 Instalación

### 1. Clonar el repositorio

```bash
git clone <url-del-repositorio>
cd mi-primera-api
```

### 2. Crear entorno virtual

```bash
python -m venv venv
```

### 3. Activar entorno virtual

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/Mac:**

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar variables de entorno

Crear un archivo `.env` en la raíz del proyecto con las siguientes variables:

```env
DATABASE_URL=postgresql://usuario:password@localhost:5432/nombre_db
SECRET_KEY=tu_clave_secreta_aqui
```

### 6. Inicializar la base de datos

```bash
flask db init
flask db migrate -m "Migración inicial"
flask db upgrade
```

## 🏃‍♂️ Ejecutar la aplicación

```bash
python app.py
```

La API estará disponible en `http://localhost:5000`

## 📚 Endpoints

### Autenticación

#### Registro de usuario

```http
POST /api/auth/registro
Content-Type: application/json

{
  "nombre": "Juan Pérez",
  "email": "juan@example.com",
  "password": "mipassword123"
}
```

#### Iniciar sesión

```http
POST /api/auth/login
Content-Type: application/json

{
  "email": "juan@example.com",
  "password": "mipassword123"
}
```

### Tareas

#### Obtener todas las tareas del usuario

```http
GET /api/tareas
```

#### Obtener una tarea específica

```http
GET /api/tareas/{id}
```

#### Crear una nueva tarea

```http
POST /api/tareas
Content-Type: application/json

{
  "titulo": "Comprar adaptador de mouse",
  "descripcion": "Necesito un adaptador USB-C",
  "categoria": "Compras",
  "usuario_id": 1
}
```

#### Actualizar una tarea

```http
PUT /api/tareas/{id}
Content-Type: application/json

{
  "titulo": "Nuevo título",
  "completado": true
}
```

#### Eliminar una tarea

```http
DELETE /api/tareas/{id}
```

## 📊 Modelos de Datos

### Usuario

- `id` (Integer, Primary Key)
- `nombre` (String, 100)
- `email` (String, 200, Unique)
- `password` (String, 255, Hash)
- `fecha_creacion` (DateTime)

### Tarea

- `id` (Integer, Primary Key)
- `titulo` (String, 200)
- `descripcion` (Text)
- `categoria` (String, 100)
- `completado` (Boolean, default: False)
- `fecha_creacion` (DateTime)
- `usuario_id` (Integer, Foreign Key)

## 🔒 Seguridad

- Las contraseñas se almacenan encriptadas usando `werkzeug.security`
- Se utilizan sesiones para mantener el estado de autenticación
- Validación de datos en todos los endpoints

## 📝 Respuestas de la API

Todas las respuestas siguen el siguiente formato:

**Éxito:**

```json
{
  "ok": true,
  "data": { ... },
  "message": "Mensaje opcional"
}
```

**Error:**

```json
{
  "ok": false,
  "message": "Descripción del error"
}
```

## 🗂️ Estructura del Proyecto

```
mi-primera-api/
│
├── app.py              # Aplicación principal y rutas
├── models.py           # Modelos de base de datos
├── requirements.txt    # Dependencias del proyecto
├── .env               # Variables de entorno (no incluir en git)
├── migrations/        # Migraciones de base de datos
└── venv/             # Entorno virtual
```

## 🤝 Contribuir

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/nueva-funcionalidad`)
3. Commit tus cambios (`git commit -m 'Agregar nueva funcionalidad'`)
4. Push a la rama (`git push origin feature/nueva-funcionalidad`)
5. Abre un Pull Request

## 📄 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## ✨ Autor

Desarrollado como proyecto educativo para el Grupo 28 de Código.
