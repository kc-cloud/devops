FROM python:3.7.4-slim

RUN apt-get clean \
    && apt-get -y update

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY test.py /app/test.py
EXPOSE 5000
CMD ["python", "test.py"]
