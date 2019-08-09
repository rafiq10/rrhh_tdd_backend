FROM python:3.7.2-alpine3.8

# set working directory
WORKDIR /usr/src/app

# add and install requirements
COPY requirements.txt /usr/src/app/requirements.txt
# RUN echo -e "http://dl-cdn.alpinelinux.org/alpine/v3.8/main" > /etc/apk/repositories
# RUN apk upgrade && apk update && apk add gcc
# RUN pip3 install  --upgrade setuptools --proxy http://TF05079@Alicia5@10.102.196.12:8080 Cython
RUN apk add --no-cache --virtual .build-deps gcc musl-dev freetds-dev

RUN pip3 install Cython
RUN pip3 install setuptools
RUN pip3 install  -r requirements.txt
# --proxy http://TF05079@Alicia5@10.102.196.12:8080 
# add app
COPY . /usr/src/app

# run server
CMD python app.py run -h 0.0.0.0