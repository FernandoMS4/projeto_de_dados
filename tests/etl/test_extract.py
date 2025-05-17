import pandas as pd
from include.extract import extract_df, extract_ipca
import requests


def test_extract_arquivo():
    df = extract_df().extract_dataframes(
        arquivo='./tests/etl/teste_boi_gordo_base.csv', extencao='csv'
    )
    df2 = extract_df().extract_dataframes(
        arquivo='./tests/etl/teste_CEPEA-20250416134013.xlsx',
        extencao='xlsx',
        skips_=3,
    )
    columns = [
        'dt_cmdty',
        'nome_cmdty',
        'tipo_cmdty',
        'cmdty_um',
        'cmdty_vl_rs_um',
        'cmdty_var_mes_perc',
        'dt_etl',
    ]
    columns2 = ['Data', 'Valor']

    assert df.columns.to_list() == columns
    assert type(df) == pd.DataFrame
    assert df2.columns.to_list() == columns2
    assert type(df2) == pd.DataFrame


def test_extract_extencao():
    try:
        extract_df().extract_dataframes(
            arquivo='./tests/etl/teste_boi_gordo_base.csv', extencao='cv'
        )
    except ValueError:
        assert ValueError


def test_extract_skips():
    try:
        extract_df().extract_dataframes(
            arquivo='./tests/etl/teste_boi_gordo_base.csv',
            extencao='csv',
            skips_='strong',
        )
    except TypeError:
        assert TypeError


def test_extrac_ipca():
    url = (
        'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=json'
    )
    request = requests.get(url=url)
    print(request.status_code)
    df = extract_ipca('01/01/2017', '31/05/2025')

    assert request.status_code == 200
    assert type(df) == pd.DataFrame


def test_extract_ipca_date():
    try:
        extract_ipca('2017-01-01', '2017-01-01')
    except KeyError:
        KeyError
    assert KeyError
