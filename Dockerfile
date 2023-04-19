FROM python:3.11.3-bullseye

###
# Copy the .lock file to only install the required deps
###
COPY Pipfile.lock .

###
# Install the deps
###
RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv requirements > requirements.txt && \
    pip install -r requirements.txt && \
    pip list


###
# Copy the application code to the image
###
COPY app app/

###
# Set the working directory to be the newly created app dir
###
WORKDIR /app

###
# Expose the port which the webserver will be running on
###
EXPOSE 8000

###
# Run the webserver
###
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
