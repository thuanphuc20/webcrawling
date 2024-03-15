# Sử dụng Python 3.9.16-slim-buster làm base image
FROM python:3.11.5

# Cài đặt MySQL client
RUN pip install fastAPI uvicorn mysql-connector

# Cài đặt thư viện Python requests
RUN pip install requests

# Set environment variable cho MySQL root password
ENV MYSQL_ROOT_PASSWORD psw123

# Thiết lập thư mục làm việc
WORKDIR /api_sql

# Copy các file cần thiết vào container
COPY . /api_mysql

# CMD để chạy ứng dụng FastAPI với Uvicorn
CMD ["uvicorn", "api_mysql:app", "--host", "127.0.0.1", "--port", "8000"]