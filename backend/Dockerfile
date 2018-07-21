FROM python:3
# RUN mkdir /fjcamillo
WORKDIR /app
COPY . .
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install flask request python-dotenv
# RUN pip install -r /app/requirements.txt
EXPOSE 5000
CMD ["pipenv","run","python", "/app/run.py --host=0.0.0.0"]