FROM python:alpine
RUN mkdir /app
COPY boot.py /app
WORKDIR /app
RUN pip install flask
CMD python boot.py
