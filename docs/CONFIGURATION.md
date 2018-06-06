### Settings production & docker
* Create a new file : .env (anywhere on the server. just point to it using docker run)
* Put all the settings in it (depending on the environment)
```
DEBUG=True
SECRET_KEY=<secret_key>
DB_NAME=luuna
DB_USER=<username>
DB_PASSWORD=<password>
DB_HOST=<localhost>
DB_PORT=3306
LANGUAGE_CODE=es-mx
TIME_ZONE=America/Mexico_City
REDIS_URL=redis://:<password>@<host>:<port>
BROKER_URL=amqp://<user>:<password>@<host>/<vhost>
```

### Settings Local
* Create a new file : web/config/settings/{.local_env|.develop_env}
* Put all the settings in it (depending on the environment)
```
DEBUG=True
SECRET_KEY=<secret_key>
DATABASE_URL=mysql://root:rohitrawat@localhost:3306/luuna_new
LANGUAGE_CODE=es-mx
TIME_ZONE=America/Mexico_City
REDIS_DATABASE_URL=redis://:<password>@<host>:<port>
```

### Database migrations
* Run python manage.py migrate
**Note**
* Needs mysql/mariadb installed along with database created.
* Might also need

## Execute the app
* python manage.py runserver

## Seed local database
* to get custom data
* python manage.py seed <app> --number=<int>
