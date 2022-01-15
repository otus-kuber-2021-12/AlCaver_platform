FROM python:3-alpine

RUN adduser -D -u 1001 -g 'user' user
RUN mkdir /app && \
    chown -R user:user /app
RUN    apk update  && \
    apk add py-pip && \
    pip install flask

USER 1001
EXPOSE 8000

COPY app.py ./
COPY app/intro.html ./app/
ENTRYPOINT ["python3", "app.py"]
