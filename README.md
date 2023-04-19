# Cakes Ahoy!

A simple API to manage some cakes.

## Running

### Requirements

- [docker](https://www.docker.com/)
- [httpie](https://httpie.io/docs/cli) (or curl)

### Procedure

1. Run the localstack and Cakes Ahoy! images found in the compose file:

   `docker compose up`

1. Navigate to http://localhost:8000/docs to confirm that the application is running and to browse the OpenAPI spec.
1. Start creating some cakes:

   `http POST :8000/v1/cakes id=1 comment="the best!" imageUrl="http://example.com" yumFactor=1 name=red`

## Contributing

Follow the steps below to get setup and ready to develop on Cakes Ahoy!

1. Install the required tools:

   - [pipenv](https://pipenv.pypa.io/en/latest/)
   - [docker](https://www.docker.com/)

1. Create the virtual env:

   `pipenv --python 3.11`

1. Rename `.test.env` to `.env`.

1. Activate the virtual env (this will also load the `.env` file):

   `pipenv shell`

1. Install the required dependencies:

   `pipenv install --dev`

1. Spin up a stand-alone localstack or connect to an AWS account:

   `docker compose -f localstack.yml up`

1. Start the webserver

   `uvicorn main:app --reload`

### Running tests

Execute the following command while in the virtual environment to run the tests

`python -m pytest -svvx tests`

## Notes

1. No authentication was required but this can easily be achieved using FastAPI dependencies.
1. Pinning the requirements would be required for a production-ready API.
1. The GET cakes endpoint is limited to 10 records when calling to DynamoDB - this can be improved using pagination.
1. Logging and metrics can be added to aid development, debugging and monitoring but this is out of scope.
