# Importanto biblioteca própria do Yahoo Finance
import yfinance as yf

# Criação de uma função que busca os dados de cada ação (ticker) no último ano.
def carregar_dados(ticker):
   df = yf.Ticker(ticker).history("1y")
   df.reset_index(inplace=True)
   # Criando uma coluna adicional para identificar qual ticker pertence aquela linha
   df['ticker'] = ticker.split(".")[0]
   return df

# Chamando a função e passando as ações desejadas
petrobras = carregar_dados("PETR4.SA")
bb = carregar_dados("BBAS3.SA")
vale = carregar_dados("VALE3.SA")

# Checando os dataframes carregados
vale.head()


