FROM python:3.6

RUN  mkdir -p /usr/src/web2py/

WORKDIR /usr/src/web2py/

COPY . /usr/src/web2py/

EXPOSE 8000 5432

CMD ["python", "testdb.py"]

CMD ["python", "web2py.py", "-a", "Window/3214789", "-i", "0.0.0.0", "-p", "8000"]