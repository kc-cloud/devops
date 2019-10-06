FROM python:3.7.4-slim

RUN apt-get clean \
    && apt-get -y update

RUN apt-get install -y telnet curl

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt --src /usr/local/src

COPY UserManagement.py /app/UserManagement.py
EXPOSE 5000
CMD ["python", "UserManagement.py"]
