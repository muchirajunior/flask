FROM python:3.8

COPY . .

RUN pip3 install flask gunicorn

EXPOSE 8000

CMD [ "python", "app.py" ]

# docker run -p 5000:5000 -it flask-docker