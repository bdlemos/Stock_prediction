import yfinance as yf
import pandas as pd

def obter_precos_abertura(ticker, inicio, fim):
    # Baixa os dados históricos das ações
    dados_acoes = yf.download(ticker, start=inicio, end=fim)
    
    # Seleciona apenas o preço de abertura
    precos_abertura = dados_acoes[['Open', 'Close']]
    
    return precos_abertura

def salvar_csv(ticker, precos_abertura):
    # Cria um DataFrame pandas com os dados
    df = pd.DataFrame(precos_abertura)
    
    # Salva o DataFrame em um arquivo CSV
    nome_arquivo = f'{ticker}_precos_abertura.csv'
    df.to_csv(nome_arquivo)

if __name__ == "__main__":
    ticker = 'AAPL'  # Símbolo da empresa (exemplo: AAPL para Apple Inc.)
    inicio = '2019-01-01'  # Data de início dos dados históricos
    fim = '2024-02-21'  # Data de fim dos dados históricos
    
    # Obtém os preços de abertura das ações
    precos_abertura = obter_precos_abertura(ticker, inicio, fim)
    
    # Salva os preços de abertura em um arquivo CSV
    salvar_csv(ticker, precos_abertura)
