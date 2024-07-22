FROM python:3.12

WORKDIR /app

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install tensorflow
RUN pip install -r requirements.txt

COPY . . 

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
