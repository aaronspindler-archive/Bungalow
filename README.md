# Bungalow Assessment

## Assumptions

### Setup

```
    virtualenv -p python3 BungalowEnv
    source BungalowEnv/bin/activate
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
```


### Ingesting Data
While in the virtual enviroment used to run the project run the commend 
```
    python manage.py ingesthouses --file challenge_data.csv 
```


### Using API 
With the server running in the virtual machine, navigate in a browser to http://127.0.0.1:8000/api/houses
```
    Example Queries
    http://127.0.0.1:8000/api/houses/?year_built=2017
    http://127.0.0.1:8000/api/houses/?year_built=2017&bedrooms=5&bathrooms=6.75
```