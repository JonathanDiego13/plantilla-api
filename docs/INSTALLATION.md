### System level
* [Python 3.6.1](https://www.python.org/downloads/)
* Pip : Comes preinstalled with Python v3.4+. Used to install libraries
* [Virtualenv](https://virtualenv.pypa.io/en/stable/): Used to install libraries locally using pip

**Note:**
* You might need to install additional dependencies depending on your operation system

### Virtualenv
* Create a new virtualenv ```virtualenv --python=python3.6 env```
* Activate it ```source env/bin/activate```
* Install predefined libraries to virtualenv (local) ```pip install -r requirements.txt```
* Install a new library ```pip install --upgrade <library name>```

**Note:**
* Alternatively virtualenvwrapper can be used
* After installation, the version and name of new libraries must be saved in relevant requirements file

### Redis
* [Basics](https://redis.io/topics/quickstart)
* Set up a password:
```
cmd: redis-cli
redis-cmd: config set requirepass <password>
redis-cmd: exit
cmd: sudo service redis restart
```
**Note**: You might also need to create keys.yaml in commons directory
