FROM python:3.8

RUN  mkdir -p /usr/src/web2py/

WORKDIR /usr/src/web2py/

COPY . /usr/src/web2py/

RUN pip3 install psycopg2

EXPOSE 8000

CMD ["python", "web2py.py", "-a", "'1'", "-i", "0.0.0.0", "-p", "8000"]