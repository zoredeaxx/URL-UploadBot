FROM python:3.10-slim-buster

WORKDIR .
COPY . .
RUN apt install git curl python3-pip ffmpeg -y 
RUN pip3 install -r requirements.txt
ENV PORT 8080
EXPOSE 8080 
CMD ["python3", "bot.py"]
