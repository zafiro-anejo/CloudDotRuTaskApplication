FROM python:3.12

WORKDIR ./
COPY . /

RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["python", "./server.py"]