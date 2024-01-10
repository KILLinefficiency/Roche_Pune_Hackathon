# FizzBuzz Rest Server

## Building:

1. Install the required packages:
```
pip3 install -r requirements.txt
```

2. Run the ``server.py`` file:

```
python3 server.py
```

3. Run tests:

**IMP NOTE: Delete the ``stats_db.db`` file before running tests!**

Run tests when the ``server.py`` file is running:
```
python3 tests.py
```

## Third party libraries used:

1. Flask

[Flask](https://flask.palletsprojects.com/en/3.0.x/api/) is used here to setup the local host server, route pages and parse URL parameters.

2. Requests

Requests is used here for tests. It is used to make GET requests to the localhost server and receive response.

## API Documentation

After running ``server.py`` file, open ``http:127.0.0.1:5000/``

1. Making request to the ``fizzbuzz`` endpoint:


URL + Endpoint Format:
```
http://127.0.0.1:5000/fizzbuzz?int1=[first_factor]&int2=[second_factor]&limit=[value_limit]&str1=[first_string]&str2=[second_string]
```

Example:
```
http://127.0.0.1:5000/fizzbuzz?int1=3&int2=5&limit=20&str1=fizz&str2=buzz
```

**Note: The query starts with ?, value is assiged to the parameter by = and the pairs are separated by &**

2. Making a request to the ``stats`` endpoint:

URL + Endpoint:
```
http://127.0.0.1:5000/stats
```

To reset the results from the ``/stats`` endpoint, simply delete the ``stats_db.db`` file.
```
rm stats_db.db
```