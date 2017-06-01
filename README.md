## About

	This is a program for downloading data from multiple sources and protocols to local disk.

## Prepare application

  Create virtual evnironment and install requirements:
```bash
    $ virtualenv --python=/usr/bin/python venv
    $ source activate venv/
    $ pip install -r requirements.txt
```

Configuration file placed at ./downloader/data/downloader.cfg

## Run application

1. Run `$ python run.py`
2. Input list of urls and press Enter

Default result location: `/tmp/downloader`
