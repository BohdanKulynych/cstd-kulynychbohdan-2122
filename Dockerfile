FROM python:3.8-slim-buster

RUN mkdir /app

workdir /app

COPY audiogeneration /app/audiogeneration
COPY tests /app/tests
COPY requirements.txt /app/requirements.txt

RUN pip3 install -r /app/requirements.txt
RUN apt-get update && apt-get install -y timidity
RUN apt-get update && apt-get install -y abcmidi

ENV PYTHONPATH /app

workdir /app/tests/audio_generation_tests
RUN pip3 install coverage
RUN coverage run -m unittest discover
workdir /app/tests/
RUN coverage run -m unittest discover db_tests
RUN coverage report
workdir /app

CMD [ "python", "/app/audiogeneration/app.py", "flask", "run" ,"/app/audiogeneration/bin/abc2wav.sh"]
