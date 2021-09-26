FROM python:3.9

COPY . /code/

WORKDIR /code

RUN pip install -r requirements.txt

ENV PYTHONUNBUFFERED=1

# EXPOSE 8000 porta para expor do APP