# MVP (Django)

## Install

* pip install django==1.8.9
* pip install psycopg2 
* pip install django-extensions
* pip install pillow
* pip install gunicorn 
* pip install dj-database-url 
* pip install whitenoise

## Steps

1. Create project
2. Create db (psql): createdb <name of db> 
3. Edit Settings.py (db settings)
4. Production/Deployment
    1. settings.py
          1. SECRET_KEY = os.environ.get(‘SECRET_KEY’)
          2. DEBUG: False 
          3. Allowed Host
    2. wsgi.py
    3. .env
    4. Procfile
    5. runtime.txt

## Heroku

1. Create Heroku App: heroku create 
2. Set Environment Variables on Heroku 
      1. heroku config:add SECRET_KEY=**[secret key]**
      2. heroku config:set DJANGO_SETTINGS_MODULE=**[name of app]**.settings.production 
3. Disable Collectstatic: heroku config:set DISABLE_COLLECTSTATIC=1
4. Push to Heroku: git push heroku master
5. Commit initial migration on the Heroku App: heroku run python manage.py migrate
6. Create Superuser on the Heroku App: heroku run python manage.py createsuperuser
7. Open the Heroku App: heroku open  --app <insert your heroku app name>
8. Database
      1. heroku addons 
      2. heroku pg:info 
      3. Back up local DB: pg_dump -U pg-user **[name of local db]** -f **[path to dump file]**
      4. Restore the DB in heroku: heroku pg:psql -a **[name of heroku app]** <  **[path to dump file]**
      5. Establish a psql session: $ heroku pg: psql


## Links/References

1. General 
      1. https://devcenter.heroku.com/articles/deploying-python
      2. https://devcenter.heroku.com/articles/django-app-configuration
      3. https://github.com/heroku/python-getting-started 
      4. https://ultimatedjango.com/learn-django/lessons/push-to-heroku/
2. Postgres
      1. http://www.marinamele.com/2014/01/how-to-set-django-app-on-heroku-part-iii.html
      2. https://devcenter.heroku.com/articles/managing-add-ons
      3. http://stackoverflow.com/questions/35446607/cant-push-database-to-heroku-because-database-is-not-empty-error
