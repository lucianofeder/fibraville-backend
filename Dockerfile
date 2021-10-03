FROM python:3.9

WORKDIR /app
COPY . .

RUN pip install -r requirements.txt
RUN pip install psycopg2

ENV PYTHONUNBUFFERED=1

ENTRYPOINT ["./entrypoint.sh"]

EXPOSE 8000