FROM python:3.10
ENV PYTHONUNBUFFERED=1
RUN pip install poetry
WORKDIR /app/
COPY poetry.lock pyproject.toml /code/
RUN poetry config virtualenvs.create false && poetry install
COPY . /app/