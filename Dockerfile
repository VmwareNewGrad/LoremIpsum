FROM ubuntu

RUN apt-get update && apt-get install -y python python-dev python-distribute python-pip

RUN pip install Flask

VOLUME ["/data"]

WORKDIR /data

ENV FLASK_APP=lipsum.py

CMD ["lipsum.py"]

EXPOSE 5000

ENTRYPOINT ["python"]
