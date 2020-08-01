FROM python:3.7-alpine

WORKDIR /app

COPY . /app

RUN pip3 install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python3", "app.py"]
