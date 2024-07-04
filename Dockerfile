FROM python:3.10-slim
WORKDIR /app
COPY pyproject.toml poetry.lock* /
RUN pip install --no-cache-dir poetry==1.8.2 && poetry config virtualenvs.create false && poetry install
COPY . /app
RUN python manage.py collectstatic --no-input
RUN mkdir -p /static_files/static/
RUN cp -ar /app/static_files/. /static_files/static/
CMD [ "gunicorn", "--bind", "0:8000", "models.wsgi" ]