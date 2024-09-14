FROM python:3.10-slim

ENV PYTHONUNBUFFERED True

ENV APP_HOME /app

ENV PORT 8080

# This will point to the credentials in the container
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/credentials/application_default_credentials.json

WORKDIR $APP_HOME

COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080
CMD ["python", "manage.py", "runserver", "0.0.0.0:$PORT"]

