from airflow.decorators import dag, task
from datetime import datetime
from include.extract import extract_df
from include.transform import transform_cepea
from include.load import load_boi_gordo, load_dataframe_parquet
import pandas as pd


@dag(
    dag_id='Pipeline_dataset_boi_gordo',
    description='ETL do processo de engenharia de dados',
    schedule='*/5 * * * *',
    start_date=datetime(2025, 5, 17),
    catchup=False,
    is_paused_upon_creation=False
)
def pipeline():
    @task
    def task_extract_cepea_archive():
        extract_dtf = extract_df()
        df = extract_dtf.extract_dataframes(
            arquivo='./archive/CEPEA-20250416134013.xlsx',
            extencao='xlsx',
            skips_=3,
        )
        return df.to_dict()

    @task
    def task_transform_dataframe(df_dict):
        df = pd.DataFrame(df_dict)
        t_cpea = transform_cepea()
        df = t_cpea.transform_dataframe(df)
        return df.to_dict()

    @task
    def task_transform_ipca(df_dict):
        df = pd.DataFrame(df_dict)
        t_cpea = transform_cepea()
        df = t_cpea.transform_ipca(df)
        return df.to_dict()

    @task
    def task_load_boi_gordo(df_dict):
        df = pd.DataFrame(df_dict)
        return load_boi_gordo(df).to_dict()

    @task
    def task_load_dataframe_parquet(df_dict):
        df = pd.DataFrame(df_dict)
        load_dataframe_parquet(df)

    # Encadeamento de funções
    extracted = task_extract_cepea_archive()
    transformed_extracted = task_transform_dataframe(extracted)
    transformed_ipca = task_transform_ipca(transformed_extracted)
    loaded = task_load_boi_gordo(transformed_ipca)
    task_load_dataframe_parquet(loaded)


pipeline()
