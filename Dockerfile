FROM ubuntu:16.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    python3 python3-venv libgl1 libglib2.0-0

COPY . /app/
WORKDIR /app/

RUN python3 -m venv /app/venv
ENV PATH="/app/venv/bin:$PATH"
RUN pip install pip==20.3.4
RUN pip install pipenv

ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN . ./venv/bin/activate && pipenv install

CMD /app/venv/bin/flask run --host 0.0.0.0 --port $PORT

EXPOSE 80
