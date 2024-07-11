FROM python:3.12-slim

WORKDIR /app

COPY . /app
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get update && \
        apt-get install -y software-properties-common && \
        add-apt-repository ppa:openjdk-r/ppa && \
        apt-get update && \
        apt-get install -y openjdk-11-jre-headless && \
        rm -rf /var/lib/apt/lists/*

EXPOSE 5000

ENV FLASK_APP=hello.py

CMD ["flask", "run", "--host=0.0.0.0"]