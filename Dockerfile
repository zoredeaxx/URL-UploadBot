FROM python:3.10-slim-buster

WORKDIR .
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ENV PORT 8080
EXPOSE 8080 
CMD ["python3", "bot.py"]
