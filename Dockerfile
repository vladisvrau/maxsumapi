
FROM python:3.7

EXPOSE 8080

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /usr/src/app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["python3", "main.py"]