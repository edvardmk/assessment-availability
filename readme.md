# Availability endpoint

An endpoint that provides an avaiability summary. You can optionally filter it by providing Foobar is a Python library for dealing with word pluralization.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install foobar.

```bash
pip install -r requirements.txt
```

## Usage

Spin up the endpoint by running

```bash
uvicorn main:app --reload
```

The endpoint will be accessible at [http://127.0.0.1:8000/summary](http://127.0.0.1:8000/summary). You can optionally provide the query parameters `start_date` and `end_date` in the format `dd.mm.yyyy` to filter within specific date limits.

## Testing

Two pytest tests are included with the package. You can run them by simply running

```bash
pytest
```

## License

[MIT](https://choosealicense.com/licenses/mit/)
