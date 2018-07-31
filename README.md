# Cambia Interview Homework

#### Michael Lane  

## Overview
This is a simple script that opens a csv file, reads in the first row, sorts that row's values, and then writes that row out to a new csv file. This is written in Python 3.7 and can be run using Docker or with Python from the command line.

## Setup & Run
### Docker
1. Ensure you have Docker installed and running on your machine.
2. From the project root, build the docker container: 
    ```bash
    docker build -t cambia_homework:latest .
    ```
3. Run the docker container in interactive mode passing command line arguments as desired. For example, you can run the tests:
    ```bash
    docker run -it --rm \
    --mount src=`pwd`/csv_files/,target=/app/csv_files/,type=bind \
    --name cambia_homework \
    cambia_homework:latest \
    test
    ```
    To access the script's CLI help 
    ```bash
    docker run -it --rm \
    --mount src=`pwd`/csv_files/,target=/app/csv_files/,type=bind \
    --name cambia_homework \
    cambia_homework:latest \
    --help
    ```
    To run the script with the (optional) CLI arguments 
    ```bash
    docker run -it --rm \
    --mount src=`pwd`/csv_files/,target=/app/csv_files/,type=bind \
    --name cambia_homework \
    cambia_homework:latest \
    --infile csv_files/input.csv --outfile csv_files/output.csv
    ```
    **Note:** If you don't supply CLI arguments, the script will prompt you for the input and output filenames.

### Python
1. Ensure you have python 3.6+ installed on your machine.
2. Install and update `pip` and `pipenv`:
    ```bash
    pip3 install -U pip pipenv
    ```
3. Set up your virtual environment using `pipenv`:
    ```bash
    pipenv --three
    pipenv install --dev
    ```
4. Run the tests in the `pipenv` environment if desired:
    ```bash
    pipenv run pytest -v
    ```
5. Run the script in the `pipenv` environment. For CLI argument help, enter this:
    ```bash
    pipenv run python sort_csv.py --help
    ```
    **Note:** To see debugging output, set `LOG_LEVEL DEBUG` in your environment