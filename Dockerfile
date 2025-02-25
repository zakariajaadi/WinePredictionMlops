FROM python:3.12.8-bullseye

# Set the working directory
WORKDIR /app

# Caching for depandancy files
COPY pyproject.toml poetry.lock /app/


RUN pip install poetry && \
    poetry config virtualenvs.in-project true && \
    poetry install --no-root
RUN mkdir -p /app/mlruns && chmod -R 777 /app/mlruns

#Add Poetry virtual environment's bin directory to PATH
ENV PATH="/app/.venv/bin:$PATH"

COPY . /app/


EXPOSE 5000
EXPOSE 8000
EXPOSE 4200




