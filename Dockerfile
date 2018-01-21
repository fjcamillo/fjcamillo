FROM python:3
RUN mkdir /fjcamillo/
WORKDIR /fjcamillo/
COPY . .
RUN pip install -r requirements.txt