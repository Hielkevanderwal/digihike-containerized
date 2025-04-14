FROM python:3.11

WORKDIR /app

COPY requirements.txt .

COPY entrypoint.sh /entrypoint.sh

RUN pip install --no-cache-dir -r requirements.txt

COPY /source .

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]