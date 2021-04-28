FROM python:3.8

WORKDIR /app

RUN pip3 install cmake
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
EXPOSE 5000

ENTRYPOINT ["python3", "/app/manage.py"]