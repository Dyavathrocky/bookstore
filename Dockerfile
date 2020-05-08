#pull base image
FROM python:3.7



#set environmental variables 
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory 
WORKDIR /code

#install dependices
COPY Pipfile Pipfile.lock /code/
RUN pip install pipenv && pipenv install --system

#copy project
COPY . /code/