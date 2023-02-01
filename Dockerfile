FROM python:3.10.2

WORKDIR /home/app

COPY microservice2.py .

RUN pip install Flask requests

EXPOSE 8000

ENV FLASK_APP=microservice2.py

CMD ["flask", "run", "--host=0.0.0.0", "--port=8000"]