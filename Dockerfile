FROM python:3.9-alpine

WORKDIR /opt/project

COPY ./requirements.txt ./requirements-test.txt ./setup.py ./

RUN \
    pip install --no-cache-dir -U pip wheel setuptools \
    && pip install --no-cache-dir --retries 15 -r requirements-test.txt

COPY setup.py README.md ./
COPY ./src ./src
COPY ./tests ./tests/

RUN  \
    python setup.py bdist_wheel \
    && pip install --no-deps -e .[test]
