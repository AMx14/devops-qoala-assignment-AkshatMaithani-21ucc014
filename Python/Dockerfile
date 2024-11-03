FROM python:3.9
#fixed path
WORKDIR /app
#fixed filename
COPY app.py .
#fixed package name
RUN pip install flask netifaces
#Port was in string
EXPOSE 8000
#misspelled pyhton
CMD ["python", "app.py"]
