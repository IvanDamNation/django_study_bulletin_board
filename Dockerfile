FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt ./
EXPOSE 8000
COPY . /app
RUN pip install -r requirements.txt
