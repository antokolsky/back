FROM python:3.10-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* /
RUN pip install --no-cache-dir poetry==1.8.2 && poetry config virtualenvs.create false && poetry install
COPY . /app
CMD [ "gunicorn", "--bind", "localhost:8000", "models.wsgi" ]