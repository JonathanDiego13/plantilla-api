# base image
FROM python:3.6-stretch


# env variables
ENV PYTHONBUFFERED 1
ENV CODE=/code
ENV WEB=$CODE/web

ADD . $CODE

RUN apt-get update \
    && apt-get upgrade --yes --allow-downgrades --allow-remove-essential --allow-change-held-packages \
    && apt-get install --yes --allow-downgrades --allow-remove-essential --allow-change-held-packages libpq-dev python3-dev default-libmysqlclient-dev \
    && apt-get clean \
    && pip install -r $CODE/requirements.txt

# working directory
WORKDIR $WEB

# PORT TO EXPOSE
EXPOSE 8001