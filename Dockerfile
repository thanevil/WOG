FROM python:3.9.5-slim
WORKDIR ./apps
RUN pip install flask
COPY MainScores.py /apps
COPY templates /apps/templates
EXPOSE 8777
CMD python3 /apps/MainScores.py