import requests
import pandas as pd
import os
from fpdf import FPDF

headers = {"x-cg-demo-api-key": os.getenv("API_KEY")}

criptos = ['bitcoin', 'ethereum', 'solana', 'xrp']

params = {
    'vs_currency': 'usd',
    'days': 365
}

tabelas = []

for cripto in criptos:
    url = f"https://api.coingecko.com/api/v3/coins/{cripto}/ohlc"
    response = requests.get(url, headers=headers, params=params)
    dados = response.json()
    df_ohlc = pd.DataFrame(dados, columns=['data', 'open', 'high', 'low', 'close'])
    df_ohlc["data"] = pd.to_datetime(df_ohlc["data"], unit='ms')
    df_ohlc["cripto"] = cripto
    tabelas.append(df_ohlc)

ohlc_data = pd.concat(tabelas)