from .extract import extract_df
import pandas as pd
from datetime import datetime


def load_boi_gordo(df):
    """
    Função que faz o upset de dados do arquivo consolidado e salva o arquivo
    """

    df = df.rename(columns={'Data': 'dt_cmdty', 'real': 'cmdty_vl_rs_um'})
    df = df[['dt_cmdty', 'cmdty_vl_rs_um']]

    df_destino = extract_df().extract_dataframes(
        arquivo='./archive/boi_gordo_base.csv', extencao='csv'
    )
    df_destino['dt_cmdty'] = pd.to_datetime(df_destino['dt_cmdty'])
    df_destino = df_destino[~df_destino['dt_cmdty'].isin(df['dt_cmdty'])]

    df_destino['dt_cmdty'] = df['dt_cmdty'].astype(str)
    df_merge = pd.concat([df_destino, df], ignore_index=True)

    df_merge = df_merge.sort_values(by='dt_cmdty')

    df_merge['nome_cmdty'] = 'Boi_Gordo'
    df_merge['tipo_cmdty'] = 'Indicador do Boi Gordo CEPEA/B3'
    df_merge['cmdty_um'] = '15 Kg/carcaça'
    df_merge['cmdty_var_mes_perc'] = (
        df_merge['cmdty_vl_rs_um']
        - df_merge['cmdty_vl_rs_um'].shift(1).fillna(0)
    ) / 100

    df_merge['dt_etl'] = df_merge['dt_etl'].fillna(
        datetime.now().strftime('%Y-%m-%d')
    )
    return df_merge


def load_dataframe_parquet(df: pd.DataFrame):
    dt_ = datetime.now().strftime('%Y-%m-%d')
    df.to_parquet(f'./archive/boi_gordo_{dt_}.parquet')


if __name__ == '__main__':
    df = pd.read_parquet('archive/boi_gordo_.parquet')
    print(df.to_string(index=False))
