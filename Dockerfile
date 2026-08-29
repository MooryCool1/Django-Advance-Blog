FROM python:3.8-slim-buster

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app

COPY requiremets.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requiremets.txt


COPY ./core /app

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]