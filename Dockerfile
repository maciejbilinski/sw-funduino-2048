FROM python:3.4

WORKDIR /code

COPY . .

ENTRYPOINT [ "python3" ]