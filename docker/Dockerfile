ARG PYTHON_VERSION="3.12.4"

FROM python:${PYTHON_VERSION}-slim AS base

# DO NOT WRITE .pyc | DO NOT BUFFER LOGS | DO NOT CHECK PIP VERSION
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1


FROM base AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM builder AS runner

COPY . .

ENTRYPOINT ["python", "-m", "app"]
