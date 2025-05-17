import requests
import pandas as pd


class extract_df:
    """
    Classe para abstração de leitura de arquivos diversos, caso tenha algum outro tipo de arquivo diferente basta implementar o método de leitura
    """

    def __init__(self):
        pass

    def extract_dataframes(self, arquivo: str, extencao: str) -> pd.DataFrame:
        """
        Método para leitura de arquivos
        arquivo = Diretório do arquivo
        extencao = tipo da extenção do arquivo
        """
        self.df: pd.DataFrame = pd.DataFrame
        if extencao == 'csv':
            self.df = pd.read_csv(arquivo)
        elif extencao == 'xlsx':
            self.df = pd.read_excel(arquivo)
        return df


def extract_cepea(dataframe: str) -> pd.DataFrame:
    """
    Carrega em memória os daos do dataframe CEPEA
    dataframe: meu_dataframe.xlsx
    """
    return pd.read_excel(dataframe, index_col=False, skiprows=3)


def extract_ipca(start_date: str, end_date: str) -> pd.DataFrame:
    """
    Busca dados do IPCA Banco central.

    start_date e end_date em formato 'dd/mm/yyyy'.

    headers para utilização da requisição sem barreiras

    Retorna um DataFrame com colunas: ['date', 'value'].

    """
    url = (
        'https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados'
        f'?formato=json&dataInicial={start_date}&dataFinal={end_date}'
    )

    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br, zstd',
        'Accept-Language': 'en-US,en;q=0.5',
        'Connection': 'keep-alive',
        'Host': 'api.bcb.gov.br',
        'If-None-Match': 'W/"4ef4-EbMnxZZwTmj7jo3dLClWfnKpf4o"',
        'Priority': 'u=0, i',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:138.0) Gecko/20100101 Firefox/138.0',
    }

    resp = requests.get(url, headers=headers).json()

    df = pd.DataFrame(resp)

    df['date'] = pd.to_datetime(df['data'], dayfirst=True)

    df['value'] = pd.to_numeric(df['valor'].str.replace(',', '.'))

    return df[['date', 'value']]


if __name__ == '__main__':

    df_ipca = extract_ipca('01/01/2017', '31/05/2025')
    print(df_ipca.head())
    df = extract_ipca(dataframe='./archive/CEPEA-20250416134013.xlsx')
    print(df.head())
    # df_ipca.to_csv("ipca_sgs_433.csv", index=False)
