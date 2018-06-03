FROM ubuntu:18.04
maintainer Dave Lawson unbrokenrabbit@gmail.com

RUN apt-get update
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install Flask

RUN mkdir -p /opt/test_flask_01
#COPY app.py /opt/test_flask_01/
ADD . /opt/test_flask_01
WORKDIR /opt/test_flask_01

ENV FLASK_APP=app.py
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

CMD flask run

