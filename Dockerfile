FROM python:3.9.5-slim
WORKDIR ./app
RUN pip install flask
COPY MainScores.py /app
COPY Scores.txt /app
COPY templates /app/templates
EXPOSE 5000
CMD ["python3", "/app/MainScores.py"]
