FROM python:3.13-slim

WORKDIR /app

RUN pip install --upgrade pip && pip install uv

COPY requirements.txt .
RUN uv pip install -r requirements.txt --system --no-cache-dir

COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
