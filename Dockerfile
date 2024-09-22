FROM python:3.8-alpine
LABEL authors="stalk"

RUN apk update && apk add --no-cache gcc musl-dev libffi-dev openssl-dev make

RUN pip install --upgrade pip && pip install poetry

WORKDIR /app

COPY poetry.lock pyproject.toml /app/

RUN poetry config virtualenvs.create false && poetry install

COPY . /app

EXPOSE 8000

ENTRYPOINT ["uvicorn", "depositapi.main:app", "--host", "0.0.0.0", "--port", "8000"]