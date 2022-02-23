FROM python:3.6

RUN  mkdir -p /usr/src/web2py/
WORKDIR /usr/src/web2py/

RUN apt-get update \
  && apt-get install -y postgresql postgresql-contrib \
  && apt-get install sudo
  
RUN pip install psycopg2

RUN service postgresql start

RUN ln -s /tmp/.s.PGSQL.5432 /var/run/postgresql/.s.PGSQL.5432

RUN sudo -u postgres createdb postgres

COPY . /usr/src/web2py/

EXPOSE 8000 5432

CMD ["python", "web2py.py", "-a", "Window/3214789", "-i", "0.0.0.0", "-p", "8000"]