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
2. Connection **Django** project to **PostgreSQL**.\
    2.1. First, I change the engine so that it uses the postgresql_psycopg2 backend instead of the sqlite3 backend.\
        For the NAME, use the name of my  database (postgres in our example). We also need to add login credentials.\
        We need the username, password, and host to connect to.
    ```
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': 'postgres',
            'USER': 'postgres',
            'PASSWORD': 'password',
            'HOST': '127.0.0.1',
            'PORT': '5432'
        }
    }
    ```
    2.2. We can begin by creating and applying migrations to our database.
    ```
    cd Motor-website/
    python manage.py makemigrations
    python manage.py migrate
    ```
    2.3. After creating the database structure, we can create an administrative account by typing:
    ```
    python manage.py createsuperuser
    ```
3. Import data from **PostgreSQL** by **Python** to **JavaScript** and from **JavaScript** to **HTML**.
4. Advertisement's publication. For this purpose I used Form.
    4.1 Creating forms in Django, is really similar to creating a model. 
        I just need to inherit from Django class and the class attributes will be the form fields. 
        I added to a forms.py file in myapp folder SaveFormFirst Form.
    ```
        class SaveFormFirst(forms.Form):
            generation = forms.CharField(max_length=150)
            box = forms.ChoiceField(choices=BOX)
            drive = forms.ChoiceField(choices=DRIVE)
            motor = forms.ChoiceField(choices=MOTOR)
            modification = forms.CharField(max_length=150)
            color = forms.CharField(max_length=150)
            image = forms.ImageField()
            #########################
    ```
    4.2 Using Form in a View.
    ```
        from .forms import SignUpForm, LoginForm, UserpageForm, PasswordForm, SaveFormFirst
        from .models import User, AdvertiseCar

        def add_kuzov(request, car, seria, year, kuzov):
            cursor = connection.cursor()
            if request.method == 'POST':
        save_form = SaveFormFirst(request.POST, request.FILES)
        if save_form.is_valid():
            user_id = request.session.get('user_id', None)
            advertisement = AdvertiseCar()
            advertisement.GenerationCar = save_form.data.get("generation", None)
            advertisement.GearCar = save_form.data.get("box", None)
            advertisement.DriveCar = save_form.data.get('drive', None)
            ##########################################################
    ```
    4.3 The view will display the result of the Form posted through the LK.html.
    ```
        <form method="POST" enctype='multipart/form-data'>
            {% csrf_token %}
            <div class="nav-link__question">{{ car }}/{{ seria }}/{{ year }}/{{ kuzov }}</div>
            ###############################################################################
            <button type="submit" class="nav-link__button">ОПУБЛИКОВАТЬ ОБЪЯВЛЕНИЕ</button>
        </form>
    ```
        The code will display a Form and post the result to our view above. You have probably noticed the tag in the template, which is just to prevent Cross-site Request Forgery (CSRF) attack on your site.
    ```
        {% csrf_token %}
    ```
    4.4 Now, I need our URLs to get started: motor/urls.py.
    ```
        urlpatterns = [
            path('admin/', admin.site.urls),
            path('', index, name='index'),
            path('auto', auto, name='auto'),
            path('auto/<car>', add_model, name='add_model'),
            path('register', register, name='register'),
            path('login', login, name='login'),
            path('logout', logout, name='logout'),
            path('user_page', user_page, name='user_page'),
            path('change_password', change_password, name='change_password')
        ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    ```
5. Page's reload during selecting options in the dropdown lists.
6. Deployment to **Heroku**.\
    6.1. Install the dependencies and these packages: 
    ```
        pip install django gunicorn whitenoise dj-database-url psycopg2
    ```
    6.2. Create a **Procfile** and add the following line.
    ```
        web: gunicorn motor.wsgi --log-file -
    ```
    6.3. Create runtime file **runtime.txt** and add the following **python-3.7.5**.\
    6.4. Login to **Heroku** terminal by **heroku login** and create heroku app by **heroku create**.\
    6.5. Modify the **settings.py** file. Modify allowed hosts by adding **'*'**.\
    6.6. Modify **INSTALLED_APPS** by adding **whitenoise.runserver_nostatic**.\
    6.7. Modify **MIDDLEWARE** by adding **whitenoise.middleware.WhiteNoiseMiddleware**.\
    6.8. Add **STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'**.\
    6.9. Add **import dj_database_url** at the top of **settings.py**.\
    6.10. After **DATABASES** add:
    ```
        db_from_env = dj_database_url.config(conn_max_age=600)
        DATABASES['default'].update(db_from_env)
    ```
    6.11. Also ensure you file has following variables **STATIC_URL, STATIC_ROOT and STATICFILES_DIRS**:
    ```
        STATIC_URL = '/static/'

        # location where django collect all static files
        STATIC_ROOT = os.path.join(BASE_DIR,'static')

        # location where you will store your static files
        STATICFILES_DIRS = [os.path.join(BASE_DIR,'project_name/static')]
    ```
    6.12. Adding and configuring **Postgres**:

        # The following commands create postgresql database on **Heroku** and fetch its url
        heroku addons:create heroku-postgresql:hobby-dev
        heroku config -s | grep DATABASE_URL
        
        # Lets push local database to herokuDB
        push local database:PGUSER=postgres PGPASSWORD=password  heroku pg:push postgres://name_of_host/name_of_local_database nameOfHerokuDB
        

## Deployed project
https://motor-project.herokuapp.com/

## Database Schemas

#### User
![User schema](https://github.com/SimonOsipov/Motor-website/blob/dev/Support%20material/User%20DB%20schema.jpeg)