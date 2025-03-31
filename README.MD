# Backend FastAPI con Docker, Docker Compose, Alembic y PostgreSQL

Este proyecto es un backend desarrollado con FastAPI, utilizando Docker y Docker Compose para la contenerización, Alembic para la gestión de migraciones de base de datos y PostgreSQL como base de datos.

## Prerrequisitos

Asegúrate de tener instalados los siguientes programas:

-   Docker: [Instalación de Docker](https://docs.docker.com/get-docker/)
-   Docker Compose: [Instalación de Docker Compose](https://docs.docker.com/compose/install/)
-   Make (opcional, pero recomendado): Para ejecutar los comandos del `Makefile`.

## Configuración

1.  **Clona el repositorio:**

    ```bash
    git clone git@github.com:JorgeDircio/ecommercer-api.git
    cd ecommercer-api
    ```

2.  **Configura las variables de entorno:**
    * Crea un archivo `.env` en la raíz del proyecto.
    * Añade las siguientes variables de entorno (ajusta los valores según sea necesario):

        ```dotenv
        URL_API_BLUMON_PAY=
        URL_API_TOKEN=
        BLUMON_RAW_PASSWORD=
        BLUMON_USERNAME=
        BLUMON_CLIENT_ID=

        BASE_URL=
        BASE_URL_FRONT=

        POSTGRES_DB=payments_app
        POSTGRES_USER=user
        POSTGRES_PASSWORD=password
        POSTGRES_HOST=db
        POSTGRES_PORT=5432
        DATABASE_URL=postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_HOST}:${POSTGRES_PORT}/${POSTGRES_DB}

        API_BASE=/api/v1
        ```

        **Nota:** Asegúrate de reemplazar los valores de ejemplo (como `password`) con los valores reales. `pgdb` es el nombre del servicio de la base de datos en `docker-compose.yml`.

## Ejecución

### Usando `make` (recomendado)

El `Makefile` proporciona comandos útiles para gestionar el proyecto.

* **Levantar los contenedores:**

    ```bash
    make up
    ```

    Este comando levanta los contenedores de la aplicación y la base de datos, según lo definido en `docker-compose.yml`.

* **Bajar los contenedores:**

    ```bash
    make down
    ```

    Este comando detiene y elimina los contenedores.

* **Reiniciar los contenedores:**

    ```bash
    make restart
    ```

    Este comando baja los contenedores y los vuelve a levantar con una nueva construcción.

* **Reconstruir los contenedores sin caché:**

    ```bash
    make rebuild
    ```

    Este comando reconstruye las imágenes de Docker sin usar la caché y levanta los contenedores.

* **Construir las imágenes de Docker:**

    ```bash
    make build
    ```

    Este comando construye las imágenes de Docker sin levantar los contenedores.

* **Ejecutar migraciones de Alembic:**

    ```bash
    make migrate
    ```

    Ejecuta las migraciones de Alembic para actualizar la base de datos al estado más reciente.

* **Crear una nueva migración de Alembic:**

    ```bash
    make makemigration
    ```

    Crea una nueva migración de Alembic con autogeneración.

* **Acceder a la shell de PostgreSQL:**

    ```bash
    make psql
    ```

    Abre una shell de PostgreSQL dentro del contenedor de la base de datos.

* **Listar las tablas en PostgreSQL:**

    ```bash
    make tables
    ```

    Muestra las tablas creadas en la base de datos.

* **Acceder a la shell del contenedor de la aplicación:**

    ```bash
    make shell
    ```

    Abre una shell bash dentro del contenedor de la aplicación.

### Sin `make`

Si prefieres no usar `make`, puedes ejecutar los comandos directamente con `docker-compose`:

* **Levantar los contenedores:**

    ```bash
    docker-compose up
    ```

* **Bajar los contenedores:**

    ```bash
    docker-compose down
    ```

* **Ejecutar migraciones de Alembic:**

    ```bash
    docker exec -it fastapi_app alembic upgrade head
    ```


* **Acceder a la shell de PostgreSQL:**

    ```bash
    docker exec -it pgdb psql -U user -d payments_app
    ```