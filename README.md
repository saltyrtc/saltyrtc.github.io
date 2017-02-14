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

Simply use the following command to push the local version of the website to
the `master` branch on Github:

    make github
