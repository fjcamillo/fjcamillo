FROM python:3
# RUN mkdir /fjcamillo
WORKDIR app
COPY . .
RUN pip install --upgrade pip && pip install pipenv
RUN pipenv install --system --deploy
# RUN pip install -r /app/requirements.txt
CMD ["python", "run.py"]