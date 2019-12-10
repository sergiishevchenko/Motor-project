# Motor-website

## How to start?
Your first commands would be:
```
git clone <SSH address of this repo>
cd Motor-website/
python3 -m myenv venv
source venv\bin\activate
pip install -r requirements.txt
```
## Step-by-step description of the project
1. Creation all pages of this project by **HTML** + **SASS** + **CSS**.
2. Connection **Django** project to **PostgreSQL**.
3. Import data from **PostgreSQL** by **Python** to **JavaScript** and from **JavaScript** to **HTML**.
4. Page's reload during selecting options in the dropdown lists.
5. Deployment to **Heroku**.\
    5.1. Install the dependencies and these packages: 
    ```
        pip install django gunicorn whitenoise dj-database-url psycopg2
    ```
    5.2. Create a **Procfile** and add the following line.
    ```
        web: gunicorn motor.wsgi --log-file -
    ```
    5.3. Create runtime file **runtime.txt** and add the following **python-3.7.5**.\
    5.4. Login to **Heroku** terminal by **heroku login** and create heroku app by **heroku create**.\
    5.5. Modify the **settings.py** file. Modify allowed hosts by adding **'*'**.\
    5.6. Modify **INSTALLED_APPS** by adding **whitenoise.runserver_nostatic**.\
    5.7. Modify **MIDDLEWARE** by adding **whitenoise.middleware.WhiteNoiseMiddleware**.\
    5.8. Add **STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'**.\
    5.9. Add **import dj_database_url** at the top of **settings.py**.\
    5.10. After **DATABASES** add:
    ```
        db_from_env = dj_database_url.config(conn_max_age=600)
        DATABASES['default'].update(db_from_env)
    ```
    5.11. Also ensure you file has following variables **STATIC_URL, STATIC_ROOT and STATICFILES_DIRS**:
    ```
        STATIC_URL = '/static/'

        # location where django collect all static files
        STATIC_ROOT = os.path.join(BASE_DIR,'static')

        # location where you will store your static files
        STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')]
    ```
    5.12. Adding and configuring **Postgres**:\

        # The following commands create postgresql database on **Heroku** and fetch its url\
        ```
            heroku addons:create heroku-postgresql:hobby-dev
            heroku config -s | grep DATABASE_URL
        ```\

        # Lets push local database to herokuDB\
        ```
            push local database:PGUSER=postgres PGPASSWORD=password  heroku pg:push postgres://name_of_host/name_of_local_database nameOfHerokuDB
        ```

## Deployed project
https://motor-project.herokuapp.com/

## Database Schemas

#### User
![User schema](https://github.com/SimonOsipov/Motor-website/blob/dev/Support%20material/User%20DB%20schema.jpeg)