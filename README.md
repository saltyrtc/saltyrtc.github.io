# saltyrtc.org

Our project website.

## Setup

Create a virtualenv:

    python -m venv VENV

Activate virtualenv:

    . VENV/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Development

Make sure that submodules are cloned:

    git submodule init
    git submodule update

You can build the static HTML into the `output/` directory:

    make html

Alternatively, start the development server:

    ./develop_server.sh start

## Publishing

Once you're happy with the changes, generate them via:

    make clean && make pages
    git push origin pages

The server should automatically fetch the `pages` branch.
