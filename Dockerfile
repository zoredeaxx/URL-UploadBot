FROM python:3.10-slim-buster
RUN add-apt-repository ppa:jonathonf/ffmpeg-4
RUN apt install ffmpeg
WORKDIR .
COPY . .
RUN pip3 install -r requirements.txt
ENV PORT 8080
EXPOSE 8080 
CMD ["python3", "bot.py"]
