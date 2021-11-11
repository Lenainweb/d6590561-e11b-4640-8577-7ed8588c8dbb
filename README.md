## Setting up

##### Clone the repo

```
$ git clone https://github.com/Lenainweb/d6590561-e11b-4640-8577-7ed8588c8dbb.git
```

##### Initialize a virtualenv

```
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Install the dependencies

```
$ pip install -r requirements.txt
```

##### Сreating a download folder

```
$ file_host_app/static/uploade
```

## Running the server


### Start Flask
```
$ export FLASK_APP=file_host_app
$ export FLASK_ENV=development
```

##### Create the database

```
$ flask init-db

$ flask run
```