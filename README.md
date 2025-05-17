![Python](https://img.shields.io/badge/Python-3.11.5-blue?logo=python&logoColor=white)
![Airflow](https://img.shields.io/badge/Airflow-2.8+-brightgreen?logo=apache-airflow)
![Poetry](https://img.shields.io/badge/Poetry-managed-8c8c8c?logo=python)

📊 Projeto de Eng de Dados Ponta

Opa bão? 😉

Este projeto tem como objetivo implementar uma pipeline de ETL utilizando Apache Airflow orquestrado via Astronomer, com containers Docker e controle de ambiente virtual via Poetry.

Este projeto foi feito no ambiente linux

🔧 Tecnologias Utilizadas

    - Python 3.11.5
    - Apache Airflow
    - Astronomer CLI
    - Docker
    - Poetry
    - Pytest

⚙️ Execução e Orquestração

Todo o pipeline foi orquestrado com:

    Apache Airflow, utilizando o Astronomer CLI para facilitar a execução local com Docker.

    Docker para conteinerização do ambiente completo (Airflow + dependências).

    Poetry para gestão de dependências e ambiente virtual.

    Pytest para execução de testes unitários garantindo a qualidade das funções críticas.

📦 Como rodar o projeto localmente

    1. Clone o repositório

        - git clone https://github.com/FernandoMS4/projeto_de_dados.git

        - cd projeto_de_dados

        - code .

🚀 Rodando com Astronomer + Docker
    
    1. Instale o Astronomer CLI
        
        > No linux: curl -sSL install.astronomer.io | sudo bash -s  
    
        > Verifique a versão do astronomer: astro version
    
        > Caso esteja no Windows utilize o WSL para configurar o ambiente ou installe pelo comandod choco install astronomer
        
        OBS: Requer Chocolatey

    2. Inicie o ambiente local com Docker

        - astro dev start

    3. Caso queia visualizar ou baixar o arquivo parquet:
        1. Para identificar seus containers
        - docker ps

        2. Para entrar no ambiente 
        - docker exec -it processo-dados2_5c5e37-scheduler-1 /bin/bash

        3. Para identificar o arquivo gerado
        - cd archive && ls

        Você vai identificar o arquivo no seguinte formato
        - boi_gordo_YYYY-MM-DD.parquet

        4. Para copiar o arquivo para o ambiente local
        - docker cp <ID do container>:/usr/local/airflow/archive/boi_gordo.parquet .


📁 Estrutura de arquivos

    ├── airflow_settings.yaml
    ├── archive
    │   ├── boi_gordo_base.csv
    │   ├── boi_gordo.parquet
    │   └── CEPEA-20250416134013.xlsx
    ├── dags
    │   ├── etl_boigordo.py
    │   ├── exampledag.py
    │   ├── __init__.py
    │   └── __pycache__
    ├── Dockerfile
    ├── include
    │   ├── extract.py
    │   ├── __init__.py
    │   ├── load.py
    │   ├── main.py
    │   ├── __pycache__
    │   └── transform.py
    ├── packages.txt
    ├── plugins
    ├── poetry.lock
    ├── pyproject.toml
    ├── README.md
    ├── requirements.txt
    └── tests
        ├── dags
        └── etl


Um pouco do processo rodando:

        ![alt text](/archive/images/image.png)