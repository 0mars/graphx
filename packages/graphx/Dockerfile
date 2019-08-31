FROM python:3.7-alpine

ENV PYTHONUNBUFFERED 1

RUN apk add --no-cache make build-base libffi-dev libressl-dev nodejs npm protobuf git zsh postgresql-dev util-linux && \
    rm -f /tmp/* /etc/apk/cache/*

RUN sh -c "$(wget https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh -O -)"

RUN npm i -g nodemon yarn
RUN pip install --upgrade pip pipenv

# set working directory
RUN mkdir -p /code/packages/graphx
WORKDIR /code/packages/graphx

# add requirements
COPY ./requirements-dev.txt /code/packages/graphx/requirements-dev.txt
COPY ./requirements.txt /code/packages/graphx/requirements.txt

# install requirements
RUN pip install -r requirements.txt
RUN pip install -r requirements-dev.txt

# add entrypoint.sh
COPY ./.docker/entrypoint.sh /code/packages/graphx/.docker/entrypoint.sh

EXPOSE 8000

# run server
CMD ["sh", "/code/packages/graphx/.docker/entrypoint.sh"]
