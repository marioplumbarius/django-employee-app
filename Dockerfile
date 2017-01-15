FROM alpine:3.5

MAINTAINER Mario Luan <mariosouzaluan@gmail.com>

ENV APP_DIR /opt/app

RUN mkdir -p $APP_DIR
WORKDIR $APP_DIR

RUN apk add --update \
                python3 \
                && rm -rf /var/cache/apk/* \
                && pip3 install --upgrade pip

COPY requirements.txt $APP_DIR
RUN pip3 install -r requirements.txt

COPY requirements-test.txt $APP_DIR
RUN pip3 install -r requirements-test.txt

COPY employeemanager $APP_DIR

EXPOSE 8000
