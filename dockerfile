FROM python:3.8-alpine

ENV PATH="/scripts:${PATH}"
ENV DEBUG=0
ENV ALLOWED_HOSTS=127.0.0.1,localhost

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache --virtual .tmp gcc libc-dev linux-headers
RUN pip3 install --no-cache-dir -r /requirements.txt
RUN apk del .tmp

RUN mkdir -p /app
COPY ./ /app

WORKDIR /app

COPY ./scripts /scripts
RUN chmod +x /scripts/*

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static

RUN adduser -D user
RUN chown -R user:user /vol
RUN chmod -R 755 /vol/web

USER user

EXPOSE 8000

CMD ["entrypoint.sh"]