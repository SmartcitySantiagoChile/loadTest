# NOTES

## Open file limit
If you have problems related with open file limit, please see this  [link](https://docs.locust.io/en/stable/installation.html#increasing-maximum-number-of-open-files-limit)

## Configure virtualenv
Execute next instructions:
- virtualenv --python=/usr/bin/python3 venv
- source venv/bin/activate
- pip install -r requirements.txt

## set web user

ADATRAP website require a valid user to retrieve data so we need to configure credentials. To do this we need to create an `.env` file and add the next two rows:
```
USERNAME='ADATRAP_USERNAME'
PASSWORD='ADATRAP_PASSWORD'
```

## Run test

To start process you have to run the command `locust --host=http://IP:PORT` where `IP` is ip target server and `PORT` is an optional parameter to give web site port

By default locust loads an interface at `localhost:8089` to start test