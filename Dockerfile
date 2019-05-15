FROM python:2.7-alpine3.9
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
CMD ["python","app.py"]