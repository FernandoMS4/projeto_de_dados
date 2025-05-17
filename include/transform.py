from .extract import extract_df, extract_ipca
from datetime import datetime
import pandas as pd


class transform_cepea:
    def __init__(self):
        pass

    def transform_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Este método preenche os valores vazios de data com a data corrente no formato mm/yyyy
        Atribui para os valores nulos  do campo Valor o correpondente do mes precedente
        """

        data_atual: datetime = datetime.now().strftime('%m-%Y')

        df['Data'] = pd.to_datetime(
            df['Data'], format='%m/%Y', errors='coerce'
        )

        df: pd.DataFrame = df.sort_values(by='Data')

        df.loc[df['Data'].isnull() | (df['Data'] == ''), 'Data'] = data_atual

        df['Valor'] = df['Valor'].ffill()

        df['Data'] = df['Data'].dt.strftime('%Y-%m-%d')
        return df

    def transform_ipca(self, df: pd.DataFrame) -> pd.DataFrame:
        """
        Este método realiza a captura dos dados do IPCA e faz a junção ao dataframe utilizando a data como parametro de comparação
        e retorna o dataframe unificado
        """
        min_date: str = pd.to_datetime(df['Data']).min().strftime('%d/%m/%Y')
        max_date: str = datetime.date(
            pd.to_datetime(df['Data']).max()
        ).strftime('%d/%m/%Y')

        ipca: list = extract_ipca(start_date=min_date, end_date=max_date)

        ipca['date'] = pd.to_datetime(
            ipca['date'], format='%m/%Y', errors='coerce'
        )

        ipca = dict(zip(ipca['date'], ipca['value']))

        df['ipca'] = df['Data'].map(ipca).fillna('0')

        df['ipca'] = pd.to_numeric(df['ipca'])

        df['Valor'] = pd.to_numeric(df['Valor'].str.replace(',', '.'))

        df['ipca_acumulado'] = df['ipca'].cumsum()

        df['Data'] = pd.to_datetime(df['Data']).dt.strftime('%m/%Y')

        df['real'] = df['Valor'] + (
            df['Valor']
            * (
                (
                    df.loc[df['Data'] == '03/2025', 'ipca_acumulado'].values[0]
                    - df['ipca_acumulado']
                )
                / 100
            )
        )
        df['real'] = pd.to_numeric(df['real']).round(decimals=2)

        df['Data'] = pd.to_datetime(
            df['Data'], format='%m/%Y', errors='coerce'
        ).dt.strftime('%Y-%m-%d')
        return df


if __name__ == '__main__':
    transform_teste = transform_cepea()
    df = transform_teste.transform_dataframe()
    print(df)
