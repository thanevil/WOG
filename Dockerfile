FROM python:3.9.5-slim
WORKDIR ./app
RUN pip install flask
RUN pip install mysql-connector-python
COPY MainScores.py /app
COPY templates /app/templates
EXPOSE 8777
CMD python3 MainScores.py