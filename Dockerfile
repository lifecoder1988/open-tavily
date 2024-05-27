FROM python:3.10.14-slim-bullseye

WORKDIR /usr/src/app

COPY requirement.txt ./
RUN pip install --no-cache-dir -r requirement.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]