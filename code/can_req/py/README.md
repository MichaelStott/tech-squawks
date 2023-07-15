# Canonical Requests Example (Python)

## Instructions

First, create and activate a virtual environment for the project. Instructions can be found [here](https://docs.python.org/3/library/venv.html). To install the dependencies, run the following:

```
$ pip3 install -r requirements.txt
```

## Demo

To run the signing portion of the demo, execute the following:
```
# Provide the AWS Secret Key, region, service name, and message to encrypt
$ python3 signing.py $AWS_SECRET_KEY us-west-1 ssm "Hello World!"
```

For invoking canonical requests, run the following:
```
$ python3 request.py $AWS_ACCESS_KEY_ID $AWS_SECRET_KEY 
```