FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt . 

RUN pip install -r requirements.txt

COPY . . 

EXPOSE "your port"

CMD ["python3","manage.py","runserver", "your port"]
