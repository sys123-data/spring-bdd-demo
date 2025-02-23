FROM python:3.9-alpine3.21
WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
# inside test framework we can have notif for reports
CMD ["python", "run_tests.py"]
