# FROM python:3.11
#
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1
#
# RUN mkdir -p /Project
# WORKDIR ./Project
#
# RUN pip install --upgrade pip
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt
#
# COPY . .
# ENTRYPOINT ["sh -c", "python", "manage.py"]
# CMD ["migrate"]
# # ENTRYPOINT TruckSearcher/manage.py
