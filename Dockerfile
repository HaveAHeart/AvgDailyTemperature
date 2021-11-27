FROM python:3.7-slim
WORKDIR /code
COPY . .
RUN pip install requests
ENV PATH=/root/.local:$PATH
ENTRYPOINT ["python3", "./main.py"]