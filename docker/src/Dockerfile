FROM python:3.11-slim

WORKDIR /app_data

COPY Pipfile /app_data/
COPY Pipfile.lock /app_data/

RUN pip install pipenv && \
    pipenv install --deploy --system

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]

