FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml requirements.lock README.md ./

RUN pip install --no-cache-dir --upgrade pip && pip install -r requirements.lock

COPY . .

EXPOSE 8001

CMD ["fastapi", "run"]