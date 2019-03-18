FROM python:3.7-slim

RUN apt-get clean \
  && apt-get -y update

RUN pip install --upgrade pip

COPY requirements.txt /auth/requirements.txt
WORKDIR /auth
RUN pip install -r requirements.txt --src /usr/local/src

COPY . /auth/

EXPOSE 5000

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
