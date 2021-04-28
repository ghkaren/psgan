FROM python:3.8

WORKDIR /app

RUN pip3 install cmake
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt && apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
EXPOSE 5000

ENTRYPOINT ["python3", "/app/manage.py"]