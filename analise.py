import os
import time
import json
from random import random
from datetime import datetime
from sys import argv

import requests
import pandas as pd
import seaborn as sns

# URL para a API do Banco Central do Brasil
URL = 'https://api.bcb.gov.br/dados/serie/bcdata.sgs.4392/dados'

def extrair_taxa_cdi():
    """
    Extrai a taxa CDI do site do BCB e salva no arquivo 'taxa-cdi.csv'.
    """
    # Captando a taxa CDI do site do BCB
    try:
        response = requests.get(url=URL)
        response.raise_for_status()
    except requests.HTTPError:
        print("Dado não encontrado, continuando.")
        dado = None
    except Exception as exc:
        print("Erro, parando a execução.")
        raise exc
    else:
        dado = json.loads(response.text)[-1]['valor']

    # Criando a variável data e hora e salvando as informações no arquivo
    for _ in range(10):
        data_e_hora = datetime.now()
        data = datetime.strftime(data_e_hora, '%Y/%m/%d')
        hora = datetime.strftime(data_e_hora, '%H:%M:%S')

        # Gera um valor aleatório para o CDI com um pequeno ajuste
        cdi = float(dado) + (random() - 0.5)

        # Verificando se o arquivo "taxa-cdi.csv" existe
        if not os.path.exists('./taxa-cdi.csv'):
            with open(file='./taxa-cdi.csv', mode='w', encoding='utf8') as fp:
                fp.write('data,hora,taxa\n')

        # Salvando dados no arquivo "taxa-cdi.csv"
        with open(file='./taxa-cdi.csv', mode='a', encoding='utf8') as fp:
            fp.write(f'{data},{hora},{cdi}\n')

        time.sleep(1)

    print("Extração concluída com sucesso.")

def gerar_grafico(nome_do_grafico):
    """
    Gera um gráfico da taxa CDI a partir dos dados extraídos e salva no formato PNG.
    """
    # Carregando os dados
    df = pd.read_csv('./taxa-cdi.csv')

    # Criando o gráfico
    grafico = sns.lineplot(x=df['hora'], y=df['taxa'])
    grafico.set_xticklabels(labels=df['hora'], rotation=90)
    grafico.get_figure().savefig(f"{nome_do_grafico}.png")

    print(f"Gráfico salvo como {nome_do_grafico}.png.")

if __name__ == "__main__":
    # Verifica se o argumento do nome do gráfico foi passado
    if len(argv) != 2:
        print("Uso: python analise.py <nome-do-grafico>")
        exit(1)

    nome_do_grafico = argv[1]

    # Executa a extração e a geração do gráfico
    extrair_taxa_cdi()
    gerar_grafico(nome_do_grafico)
