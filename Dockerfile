FROM python:3.9.5-slim
WORKDIR ./app
RUN pip install flask
COPY MainScores.py /app
COPY templates /app/templates
EXPOSE 8777
CMD ["python3", "/app/MainScores.py"]
