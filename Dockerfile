FROM python:3.10-slim-buster

#RUN apt-get update && apt-get install -y software-properties-common

RUN add-apt-repository ppa:mc3man/trusty-media
RUN apt-get update && apt-get install -y ffmpeg

WORKDIR .
COPY . .

RUN pip3 install -r requirements.txt

ENV PORT 8080
EXPOSE 8080 

CMD ["python3", "bot.py"]
