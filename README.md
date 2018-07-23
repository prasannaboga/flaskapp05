##### Environment
```commandline
python 3.6
mongoDB
```

##### Create Virtual Environment

```commandline
virtualenv -p /usr/bin/python3.6 venv
```

##### Setup environment
```commandline
cp .env.sample .env
```
Enter respective values for environment variables

##### Install Requirements
```commandline
pip install -r requirements.txt
```

##### Freeze Requirements
```commandline
pip freeze > requirements.txt
```

##### Test
Execute all test suite
```commandline
pytest -s
```
Covragte


### TODO List

- [ ] mongoDB connections with authentication

- [ ] mongoDB transactions

- [ ] Write test cases for models

- [ ] https://github.com/hiroaki-yamamoto/mongoengine-goodjson

- [ ] https://github.com/marshmallow-code/marshmallow

- [ ] api authentication using flask-login

- [ ] Using with mongoengine_goodjson problem with pagination

___
### Reference Links

https://simpleit.rocks/managing-environment-configuration-variables-in-flask-with-dotenv/

https://damyanon.net/post/flask-series-configuration/

https://github.com/miguelgrinberg/flasky
https://github.com/achiku/sample-flask-sqlalchemy

https://simpleit.rocks/managing-environment-configuration-variables-in-flask-with-dotenv/
