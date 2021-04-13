FROM python:3.8-alpine as app-stage

ENV PATH="/scripts:${PATH}"

COPY ./server/requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers musl-dev libffi-dev
RUN pip install -U  cffi pip setuptools
RUN pip3 install --no-cache-dir -r /requirements.txt
RUN apk del .tmp

RUN chmod +x /scripts/*

RUN mkdir -p /vol/static
RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/static

CMD ["entrypoint.sh"]