FROM python:3.10-slim-bullseye

WORKDIR /blockchain

EXPOSE 8000

COPY . .

RUN pip install --no-cache-dir --upgrade pipenv==2022.12.19

RUN pipenv install --deploy

CMD ["pipenv", "run", "server"]