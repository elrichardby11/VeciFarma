# VeciFarma

### VeciFarma es una plataforma que combina la entrega de medicamentos a domicilio con la creación de empleo local, ayudando a la comunidad a acceder a la salud y generando oportunidades laborales

## Instalación

Sigue estos pasos para configurar el proyecto en tu entorno local:

### 1. Clona el Repositorio

```bash
git clone https://github.com/elrichardby11/VeciFarma.git
cd VeciFarma
```

### 2. Crea y Activa el Entorno Virtual

Para mantener las dependencias del proyecto aisladas, se recomienda utilizar un entorno virtual de Python. Sigue estos pasos para crear y activar el entorno virtual:

#### En Windows

```bash
python -m venv .venv
.\.venv\Scripts\activate
```

#### En macOS y Linux

```bash
python3 -m venv .venv
source .\.venv/bin/activate
```

### 3. Instala las Dependencias

Una vez activado el entorno virtual, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 4. Ejecuta las migraciones

Antes de ejecutar el proyecto es necesario crear la base de datos, comando para crear la base de datos:

```bash
python manage.py migrate
```

### 5. Ejecuta el Proyecto

Ahora estás listo para ejecutar el proyecto, puedes iniciar la aplicación con:

```bash
python manage.py runserver
```

## Demo
