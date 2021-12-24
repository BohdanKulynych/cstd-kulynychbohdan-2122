FROM python:3.8-slim-buster

RUN mkdir /app

workdir /app

copy . .

RUN apt-get update && apt-get install -y timidity
RUN apt-get update && apt-get install -y abcmidi
RUN pip3 install -r requirements.txt

ENV PYTHONPATH /app

CMD [ "python", "/app/audiogeneration/app.py", "flask", "run" ,"/app/audiogeneration/bin/abc2wav.sh"]
