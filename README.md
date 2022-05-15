# Image to Pencil Sketch

## Requirements

1. Python 3

## Setup

Run following commands inside the project directory.

1. Setup virtual environment
   ```
   python3 -m venv ./venv
   ```
1. Activate virtual environment
   ```
   source ./venv/bin/activate
   ```
1. Install `pipenv`
   ```
   pip install pipenv
   ```

   While installing `pipenv`, your `pip` might be upgraded to version not supported
   by your Python version. To prevent that, redo the installation from step 1 and
   update `pip` manually to version supported by your Python.

   For example, for Python 3.5:
   ```
   pip install pip==20.3.4
   ```
1. Install packages
   ```
   pipenv install
   ```

## Usage

Run following commands inside the project directory.

1. Activate virtual environment
   ```
   source ./venv/bin/activate
   ```
1. Start web server:
   ```
   flask run
   ```
   To use different port:
   ```
   flask run --port 8080
   ```
   To run in development mode:
   ```
	FLASK_ENV=development flask run
   ```
1. Open browser and go to http://localhost:5000. Make sure to replace `5000` if you use different port.
