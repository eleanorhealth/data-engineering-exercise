# data-eng-exercise

Repo designed for interview purposes regarding the data engineering role at Eleanor Health

## Getting Started

### Prerequisites

This repo requires the following to be installed on your machine:

- [Docker](https://docs.docker.com/get-docker/) (Easiest way to get started)
- [Python 3.11+](https://www.python.org/downloads/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

### Installation

1. Run the following commands to install the dependencies:

    ```bash
    python -m pip install pipenv
    pipenv install --dev
    ```

### Usage

1. Run the following command to execute the python script:

    ```bash
    pipenv run python main.py ./sample/memberlist.csv
    ```

### Docker

1. Run the following command to build the docker image:

    ```bash
    docker build -t data-eng-exercise .
    ```

2. Run the following command to execute the docker image:

    ```bash
    docker run -it --rm -v ${PWD}/sample:/app/sample data-eng-exercise ./sample/memberlist.csv
    ```

## Tasks

Each task should be completed in the `main.py` file. The tasks are as follows:

### 1. Normalize the `GENDER` column

Normalize the `GENDER` column in the `memberlist.csv` file to be either `M`, `F`, or `U` (unknown).

* All values should be capitalized
* All values should be trimmed of whitespace
* All values should be one of the following:
  * `M`
  * `F`
  * `U`
* If the value is not one of the above, it should be set to `U`
* Continue processing the file

### 2. Log a warning on missing required columns for city and state

Log a warning on missing required columns for city and state.

* If the `CITY` or `STATE` column is missing, log a warning with the following message:
  * `Missing required column: CITY`
  * `Missing required column: STATE`
* Continue processing the file

### 3. Add city and state to records missing them

Use zippy to query zipcodebase for the missing city and state columns on records that are without one
and add the missing data to the record.

* If the `CITY` or `STATE` column is missing, query zippy for the missing data
* Add the missing data to the record
* Continue processing the file

#### Zippy Usage

Zippy is a test service that is designed to mimic the functionality of the zipcodebase api. It is a simple
go app that will return a json response with the city and state for a given list of zipcodes. The service
is available to you and an endpoint will be provided during the exercise.

##### Example Request

```bash
curl -X POST -H "Content-Type: application/json" https://{TEMP_ENDPOINT}/locations\?zipCodes\=28202,90210
```

or in a web browser go to the following url: [https://{TEMP_ENDPOINT}/locations?zipCodes=28202,90210](https://{TEMP_ENDPOINT}}/locations?zipCodes=28202,90210)

##### Example Response

```json
[
  {
    "city": "Charlotte",
    "state": "North Carolina",
    "stateCode": "NC",
    "zipCode": "28202",
    "country": "US"
  },
  {
    "city": "Beverly Hills",
    "state": "California",
    "stateCode": "CA",
    "zipCode": "90210",
    "country": "US"
  }
]
```

## Contributing

All code should follow PEP8 standards and be formatted with [Black](https://github.com/psf/black). This can be done by
running the following command:

```bash
pipenv run black .
```

Other tools that are used to ensure code quality are:

* [Flake8](https://flake8.pycqa.org/en/latest/)
* [Mypy](https://mypy.readthedocs.io/en/stable/)
* [isort](https://pycqa.github.io/isort/)
