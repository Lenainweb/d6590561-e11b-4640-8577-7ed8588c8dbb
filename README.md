## Setting up

##### Clone the repo

```
$ git clone 
$ cd 
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

##### Create the database

```
flask init-db
```

## Running the server


#### Start Flask
```
$ export FLASK_APP=file_host_app
$ export FLASK_ENV=development
$ flask run
```