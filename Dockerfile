FROM python:3.8
WORKDIR /flaskProject
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY src/ .
EXPOSE 5000
CMD [ "python", "./app.py","host=0.0.0.0" ]
