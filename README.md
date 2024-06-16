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

## Estructura del proyecto

demo-pyday/
├── .github/
│ └── workflows/
│ └── main.yml
├── application/
│ ├── tasks/
│ │ ├── init.py
│ │ ├── config.py
│ │ └── extensions.py
├── instance/
├── migrations/
│ ├── alembic.ini
│ ├── env.py
│ ├── script.py.mako
│ └── versions/
├── tests/
│ ├── init.py
│ └── test_app.py
├── .coveragerc
├── .env
├── .flaskenv
├── README.md
├── pytest.ini
├── requirements.txt
├── run.py
└── setup.cfg


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

### Notas
- He cambiado la base de datos de postgresql por Turso.
