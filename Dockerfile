FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN mkdir -p /Project
# WORKDIR ./Project

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

COPY . .
CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8000
# ENTRYPOINT TruckSearcher/manage.py
