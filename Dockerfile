FROM ubuntu

RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip 

RUN pip install Flask

VOLUME ["/data"]

WORKDIR /data

ENV FLASK_APP=lipsum.py

CMD ["flask run --host=0.0.0.0"]

EXPOSE 5000
