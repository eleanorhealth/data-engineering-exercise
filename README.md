# data-eng-exercise

Repo designed for interview purposes regarding the data engineering role at Eleanor Health

## Getting Started

### Prerequisites

:warning: **If you are doing a live coding interview and are using the code editor provided to you by the interviewer,
you do not need to install anything. The code editor will have everything you need.**

This repo requires the following to be installed on your machine:

- [Docker](https://docs.docker.com/get-docker/) (Easiest way to get started)
- [Python 3.9+](https://www.python.org/downloads/)
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

Each task should be completed in the `main.py` file. During the interview, you will be asked to walk through
your solution and explain your thought process. You will also be allowed to use the internet to look up
documentation and other resources. If you have any questions, please ask.

The tasks are as follows:

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
  * `Missing value in required column: CITY`
  * `Missing value in required column: STATE`
* Use the `logger` object to log the warning
* The `logger` object is already configured for you
* Continue processing the file

### 3. Add city and state to records missing them

Use zippy to query zipcodebase for the missing city and state columns on records that are without one
and add the missing data to the record.

* If the `CITY` or `STATE` column is missing, query zippy for the missing data
* Add the missing data to the record
* Continue processing the file

#### Zippy Usage

Zippy is a test service that is designed to mimic the functionality of the zipcodebase api. It is a simple
go app that will return a json response with the city and state for a given list of zipcodes. 

The service is available to you and you will be given the url and api key to use it.

##### Example Request

```bash
curl -X POST -H "Content-Type: application/json"https://{ZIPPY_URL}/locations?tempKey={API_KEY}&zipCodes=28202,90210
```

or in a web browser go to the following url: [https://{ZIPPY_URL}/locations?tempKey={API_KEY}&zipCodes=28202,90210](https://{ZIPPY_URL}/locations?tempKey={API_KEY}&zipCodes=28202,90210)

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
