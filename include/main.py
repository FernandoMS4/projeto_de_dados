from include.extract import extract_df
from include.transform import transform_cepea
from include.load import load_boi_gordo, load_dataframe_parquet


def task_extract_cepea_archive():
    extract_dtf = extract_df()
    df = extract_dtf.extract_dataframes(
        arquivo='./archive/CEPEA-20250416134013.xlsx',
        extencao='xlsx',
        skips_=3,
    )
    return df


def task_transform_dataframe():
    t_cpea = transform_cepea()
    df = t_cpea.transform_dataframe(task_extract_cepea_archive())
    return df


def task_transform_ipca():
    t_cpea = transform_cepea()
    df = t_cpea.transform_ipca(task_transform_dataframe())
    return df


def task_load_boi_gordo():
    df = load_boi_gordo(task_transform_ipca())
    return df


def task_load_dataframe_parquet():
    load_dataframe_parquet(task_load_boi_gordo())


if __name__ == '__main__':
    print('\nP1')
    print(task_extract_cepea_archive())
    print('\nP2')
    print(task_transform_dataframe())
    print('\nP3')
    print(task_transform_ipca())
    print('\nP4')
    print(task_load_boi_gordo())
    print('\nP5')
    print(task_load_dataframe_parquet())
