FROM python:3.9.2-alpine3.13

COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

COPY * /app/

RUN pip install -r requirements.txt


# ENTRYPOINT [ "python", "app.py" ]
CMD python app.py
