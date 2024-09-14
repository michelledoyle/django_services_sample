FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

ENV PORT 5000

# This will point to the credentials in the container
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials/application_default_credentials.json

WORKDIR $APP_HOME

COPY . ./

# Copy the credentials file to the container
COPY /Users/michelle/.config/gcloud/application_default_credentials.json /app/credentials/application_default_credentials.json

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
