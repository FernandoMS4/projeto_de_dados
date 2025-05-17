FROM astrocrpublic.azurecr.io/runtime:3.0-2

COPY . /usr/local/airflow/

WORKDIR /usr/local/airflow/

RUN pip install --upgrade pip && pip install -r requirements.txt

ENV PYTHONPATH="/usr/local/airflow:${PYTHONPATH}"
