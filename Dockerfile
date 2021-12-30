FROM python:3.9

ENV FLASK_ENV=development \
    FLASK_APP=app/klarna

COPY requirements.txt /tmp
RUN pip3 install -r /tmp/requirements.txt --no-cache-dir && \
    rm -f /tmp/requirements.txt

WORKDIR /opt/klarna

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host=0.0.0.0"]
