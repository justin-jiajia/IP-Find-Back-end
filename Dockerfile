FROM python:3.9

MAINTAINER jiajia6666

COPY ./requirements.txt /requirements.txt
WORKDIR /
RUN pip install -r requirements.txt
COPY . /
EXPOSE 5000
CMD  ["python", "-m", "gunicorn", "-w 3", "-b 0.0.0.0:5000", "app:api" ]