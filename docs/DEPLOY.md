## PRODUCTION
### [gunicorn](http://docs.gunicorn.org/en/stable/configure.html)
* The interface of choice to work in between nginx and django
* **configure:**
```
mkdir logs; cd logs;
touch gunicorn.access.logs;
touch gunicorn.error.logs;
cd web; gunicorn -c config.wsgi.production:application
```

### [nginx](https://www.nginx.com/resources/wiki/)
* The web server of choice
* **Install:** ```sudo apt-get install nginx```
* **configuration:**
```
sudo ln -s $(realpath nginx/production.conf) /etc/nginx/sites-enabled/
sudo touch /etc/nginx/logs/luuna.error.logs
sudo touch /etc/nginx/logs/luuna.access.logs
sudo chmod 777 /etc/nginx/logs/luuna.*
echo "127.0.0.1 luuna.mx" | sudo tee -a /etc/hosts
sudo service nginx restart
```
