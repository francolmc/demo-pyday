# Demo PyDay

## Descripción

Este proyecto es una demostración de cómo implementar tests unitarios y su integración en un pipeline CI/CD utilizando Flask, Turso, GitHub Actions y herramientas de cobertura de código como `coverage.py` y `mutmut`.

## Tecnologías Utilizadas

- **Flask**: Microframework para construir aplicaciones web.
- **Turso**: Base de datos utilizada para almacenar las tareas.
- **SQLAlchemy**: ORM utilizado para interactuar con la base de datos.
- **GitHub Actions**: Plataforma de integración y entrega continua.
- **coverage.py**: Herramienta para medir la cobertura de código.
- **mutmut**: Herramienta para pruebas de mutaciones.

### Estructura del Proyecto

```plaintext
demo-pyday/
├── .github/
│   └── workflows/
│       └── main.yml
├── application/
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── config.py
│   │   └── extensions.py
├── migrations/
│   ├── alembic.ini
│   ├── env.py
│   ├── script.py.mako
│   └── versions/
├── tests/
│   ├── __init__.py
│   └── test_app.py
├── .coveragerc
├── .env
├── .flaskenv
├── README.md
├── pytest.ini
├── requirements.txt
├── run.py
└── setup.cfg
```

#### Explicación de los Directorios y Archivos

- **.github/workflows/**:
  - `main.yml`: Define el pipeline CI/CD utilizando GitHub Actions. Configura el entorno, instala dependencias, ejecuta tests y despliega la aplicación.

- **application/**:
  - `tasks/`: Contiene los módulos de la aplicación.
    - `__init__.py`: Inicializa el módulo `tasks`.
    - `config.py`: Configuraciones de la aplicación, incluyendo la conexión a la base de datos.
    - `extensions.py`: Inicialización de extensiones (como SQLAlchemy).

- **migrations/**:
  - `alembic.ini`: Archivo de configuración para Alembic.
  - `env.py`, `script.py.mako`: Archivos de configuración de Alembic para la gestión de migraciones.
  - `versions/`: Carpeta que contiene los scripts de migración generados por Alembic.

- **tests/**:
  - `__init__.py`: Inicializa el módulo de tests.
  - `test_app.py`: Contiene los tests unitarios de la aplicación.

- **.coveragerc**: Archivo de configuración para la herramienta de cobertura de código `coverage.py`.

- **.flaskenv**: Archivo de configuración para Flask, indicando la aplicación y el entorno de ejecución.

- **README.md**: Archivo de documentación del proyecto.

- **pytest.ini**: Archivo de configuración para Pytest.

- **requirements.txt**: Archivo que lista todas las dependencias del proyecto.

- **run.py**: Archivo principal para ejecutar la aplicación Flask.

- **setup.cfg**: Archivo de configuración adicional (puede incluir configuraciones para herramientas de linting, formateo de código, etc.).

## Configuración

1. **Clonar el repositorio:**

    ```bash
    git clone https://github.com/francolmc/demo-pyday.git
    cd demo-pyday
    ```

2. **Crear y activar el entorno virtual:**

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows: env\Scripts\activate
    ```

3. **Instalar las dependencias:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Configurar las variables de entorno:**

    Crea un archivo `.env` con el siguiente contenido:

    ```dotenv
    DATABASE_TEST_CONNECTION_STRING="sqlite:///:memory:"
    TURSO_DATABASE_URL="<URL DATABASE TURSO>"
    TURSO_AUTH_TOKEN="<TOKEN DATABASE TURSO>"
    ```

    Crea un archivo `.flaskenv` con el siguiente contenido:

    ```dotenv
    FLASK_APP=run.py
    FLASK_ENV=development
    ```

5. **Inicializar la base de datos:**

    ```bash
    flask db init
    flask db upgrade
    ```

## Ejecución

Para ejecutar la aplicación localmente:

```bash
flask run
```

## Tests

Para ejecutar los tests con cobertura:

```bash
coverage run -m pytest
coverage report
coverage html
```

Para ejecutar pruebas de mutación:

```shell
mutmut run
mutmut results
```

## CI/CD

Este proyecto utiliza GitHub Actions para CI/CD. El archivo de configuración del workflow se encuentra en .github/workflows/main.yml y realiza las siguientes acciones:

- Configura el entorno con Python y Turso.
- Instala las dependencias.
- Ejecuta los tests unitarios y genera informes de cobertura.
- Realiza el despliegue si todos los tests pasan.

### Explicación del archivo de GitHub Actions

```yaml
name: CI/CD Pipeline

on:
  push:
    branches:
      - main

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v2

      - name: Set up Python
        uses: actions/setup-python@v2
        with:
          python-version: "3.9"

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Set environment variables
        run: |
          echo "DATABASE_TEST_CONNECTION_STRING=sqlite:///:memory:" >> $GITHUB_ENV
          echo "FLASK_APP=run.py" >> $GITHUB_ENV
          echo "FLASK_ENV=development" >> $GITHUB_ENV

      - name: Run tests
        run: |
          pytest

  deploy:
    runs-on: ubuntu-latest
    needs: test

    steps:
      - name: Check out code
        uses: actions/checkout@v2

      - name: Install dependencies
        run: |
          python -m pip install --upgrade pip
          pip install -r requirements.txt

      - name: Deploy to Render
        env:
          RENDER_API_KEY: ${{ secrets.RENDER_API_KEY }}
          RENDER_SERVICE_ID: ${{ secrets.RENDER_SERVICE_ID }}
        run: |
          curl -X POST \
          -H "Authorization: Bearer $RENDER_API_KEY" \
          -H "Accept: application/json" \
          -H "Content-Type: application/json" \
          --data '{"serviceId": "${RENDER_SERVICE_ID}"}' \
          https://api.render.com/v1/services/${RENDER_SERVICE_ID}/deploys
```

### Explicación del flujo de trabajo de GitHub Actions

Este archivo de flujo de trabajo (`.github/workflows/main.yml`) define un pipeline CI/CD para el proyecto:

- **Eventos de activación**: El pipeline se activa en cada `push` a la rama `main`.
- **Trabajo de prueba (test)**: Se ejecuta en un entorno Ubuntu.
  - **Pasos**:
    1. `Check out code`: Clona el repositorio.
    2. `Set up Python`: Configura Python 3.9.
    3. `Install dependencies`: Instala las dependencias del proyecto.
    4. `Set environment variables`: Configura las variables de entorno.
    5. `Run tests`: Ejecuta los tests usando `pytest`.
- **Trabajo de despliegue (deploy)**: Se ejecuta después de que el trabajo de prueba pasa.
  - **Pasos**:
    1. `Check out code`: Clona el repositorio.
    2. `Install dependencies`: Instala las dependencias del proyecto.
    3. `Deploy to Render`: Realiza el despliegue en Render usando la API de Render.

### Notas
- He cambiado la base de datos de postgresql por Turso.
