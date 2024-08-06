ARG PYTHON_VERSION=3.12.4

FROM python:${PYTHON_VERSION}-slim AS base

WORKDIR /app

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1


FROM base AS builder

RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt


FROM builder AS runner

COPY . .

ENTRYPOINT ["python", "app/app.py"]
