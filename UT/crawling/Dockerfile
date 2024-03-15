FROM python:3.11.5


RUN pip install requests beautifulsoup4 fastapi uvicorn

COPY . /api_crawling
WORKDIR /crawling
CMD ["uvicorn", "api_craw:app", "--host", "127.0.0.1", "--port", "8080"]