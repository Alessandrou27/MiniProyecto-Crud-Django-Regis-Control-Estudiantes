# Grupo 2 - CRUD / Control Estudiantes

## 🎯 Product Backlog
Desarrollar un sistema de gestión de estudiantes que permita:

- Listar todos los estudiantes registrados.
- Registrar nuevos estudiantes con validaciones adecuadas.
- Editar la información de los estudiantes existentes.
- Eliminar estudiantes del sistema.
- Buscar estudiantes por nombre.
- Garantizar una experiencia de usuario clara y sin errores en el flujo principal.

## 🎯 Sprint Goal
Desarrollar e implementar, utilizando el framework Django, un sistema de gestión de estudiantes que permita al usuario listar, registrar, editar y eliminar estudiantes de manera sencilla y eficiente. El objetivo es garantizar que todas las funcionalidades básicas estén operativas, con una experiencia de usuario clara, validaciones adecuadas y sin errores en el flujo principal.

## 👥 Roles Scrum
| Rol            | Integrante           | Función principal                                                                                                 |
|----------------|---------------------|------------------------------------------------------------------------------------------------------------------|
| Scrum Master   | Sebastian Perez     | Facilita el proceso Scrum, elimina impedimentos y asegura que el equipo siga los principios ágiles.              |
| Product Owner  | Gabriel Tuñoque     | Define Historias de usuario, prioriza funcionalidades y establece las metas del proyecto.                        |
| Developer 1    | Piero Aguilar       | Desarrolla la estructura de las plantillas HTML para la interfaz de usuario.                                     |
| Developer 2    | Josue Castillo      | Diseña y desarrolla los estilos CSS personalizados en la carpeta static/css.                                     |
| Developer 3    | Sebastian Gonzales  | Se encarga de la creación y configuración del proyecto Django, así como de la lógica principal del backend.      |
---

## 🗂️ Estructura del Proyecto

```
control_estudiantes/
│
├── control_estudiantes/         # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
├── estudiantes/                 # Aplicación principal: gestión de estudiantes
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                 # Formularios y validaciones
│   ├── migrations/              # Migraciones de la base de datos
│   ├── models.py                # Modelo Estudiante
│   ├── static/
│   │   └── css/                 # Hojas de estilo personalizadas
│   ├── templates/
│   │   └── estudiantes/         # Plantillas HTML para CRUD
│   ├── tests.py
│   ├── urls.py
│   └── views.py                 # Vistas basadas en clases para CRUD
│
├── db.sqlite3                   # Base de datos SQLite
├── manage.py                    # Script de gestión de Django
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación del proyecto
```

## ⚙️ Instalación y Puesta en Marcha

1. **Clona el repositorio:**
   ```bash
   git clone <URL-del-repositorio>
   cd MiniProyecto-Crud-Django-Regis-Control-Estudiantes
   ```

2. **Crea un entorno virtual (recomendado):**
   - En Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. **Instala las dependencias:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Realiza las migraciones de la base de datos:**
   ```bash
   python manage.py migrate
   ```

5. **Inicia el servidor de desarrollo:**
   ```bash
   python manage.py runserver
   ```

6. **Accede a la aplicación:**
   Abre tu navegador y entra a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## 📋 Historias de Usuario

### Historia de Usuario 1: Listar Estudiantes
**Como** usuario,
**quiero** ver una lista de todos los estudiantes registrados en el sistema,
**para** tener una visión general y acceder fácilmente a la información de cada uno.

**Criterios de aceptación:**
- Se debe mostrar una tabla con todos los estudiantes registrados.
- La lista debe actualizarse automáticamente al agregar, editar o eliminar estudiantes.
- Si no hay estudiantes registrados, debe mostrarse un mensaje adecuado.

---

### Historia de Usuario 2: Registrar Nuevo Estudiante
**Como** usuario,
**quiero** registrar un nuevo estudiante en el sistema,
**para** poder llevar un control actualizado de los alumnos.

**Criterios de aceptación:**
- El formulario debe validar que todos los campos obligatorios estén completos.
- El correo debe tener formato válido.
- Al guardar, el estudiante debe aparecer en la lista.
- Si hay errores, deben mostrarse mensajes claros.

---

### Historia de Usuario 3: Editar Estudiante Existente
**Como** usuario,
**quiero** editar la información de un estudiante existente,
**para** corregir o actualizar sus datos cuando sea necesario.

**Criterios de aceptación:**
- Al hacer clic en "Editar", debe mostrarse el formulario con los datos actuales.
- Debe validar los campos igual que en el registro.
- Al guardar, los cambios deben reflejarse en la lista.
- Si hay errores, deben mostrarse mensajes claros.

---

### Historia de Usuario 4: Eliminar Estudiante
**Como** usuario,
**quiero** eliminar un estudiante del sistema,
**para** mantener la base de datos limpia y actualizada.

**Criterios de aceptación:**
- Debe haber un botón para eliminar en cada estudiante.
- Al eliminar, debe pedirse confirmación.
- El estudiante eliminado no debe aparecer en la lista.
- Debe mostrarse un mensaje de éxito tras la eliminación.

---

### Historia de Usuario 5: Filtrar Estudiantes por Nombre
**Como** usuario,
**quiero** filtrar la lista de estudiantes por nombre,
**para** encontrar rápidamente la información de un alumno específico.

**Criterios de aceptación:**
- Debe existir un campo de búsqueda por nombre.
- La búsqueda debe ser insensible a mayúsculas/minúsculas.
- Si no hay resultados, debe mostrarse un mensaje adecuado.

---

## 🧩 Método INVEST para las Historias de Usuario

- **I**ndependiente: Cada historia puede desarrollarse y probarse por separado.
- **N**egociable: Las historias son flexibles y pueden ajustarse según las necesidades del usuario.
- **V**aliosa: Cada historia aporta valor real al usuario final.
- **E**stimable: Es posible estimar el esfuerzo necesario para completarla.
- **S**mall (Pequeña): Cada historia es lo suficientemente pequeña para completarse en un sprint.
- **T**estable: Cada historia tiene criterios de aceptación claros y verificables.
