FROM python:3.10


# update packages
RUN apt-get -qq update
RUN apt-get install --yes apache2 apache2-dev
RUN pip install mod_wsgi

# copy the actual code
COPY gestão_energia/requirements.txt /code/

# copy and install requirements first to leverage caching
RUN pip install -r /code/gestão_energia/requirements.txt

RUN chown -R www-data:www-data /code

WORKDIR /code/gestão_energia
CMD mod_wsgi-express start-server --locale C.UTF-8 --url-alias /static /code/static /code/gestão_energia/gestaoEnergia/wsgi.py --user www-data --group www-data

