FROM python:3.9.19-slim
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
EXPOSE 8001
COPY . /app
CMD python ./main.py