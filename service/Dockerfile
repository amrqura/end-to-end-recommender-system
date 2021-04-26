FROM python:3


RUN apt-get update -y && \
    apt-get install -y python-pip python-dev

COPY . /src
WORKDIR /src
RUN pip install -r requirements.txt

EXPOSE 5000

CMD cd /src && python recommender_system_service.py