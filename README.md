# Análise da Taxa CDI com Python

Este repositório contém um script Python que realiza a extração da taxa CDI diretamente da API do Banco Central do Brasil (BCB) e gera um gráfico da variação da taxa ao longo do tempo.

## Descrição

O script combina as etapas de extração de dados e visualização gráfica em um único arquivo (`analise.py`). Ele funciona em dois passos principais:

1. **Extração da Taxa CDI**: Utiliza a biblioteca `requests` para fazer uma requisição à API do BCB e salva os dados extraídos em um arquivo CSV chamado `taxa-cdi.csv`.
2. **Geração de Gráfico**: Utiliza as bibliotecas `pandas` e `seaborn` para ler os dados do CSV e gerar um gráfico de linha da variação da taxa CDI ao longo do tempo, salvando-o como um arquivo PNG.

## Requisitos

Para executar o script, você precisará das seguintes bibliotecas Python instaladas:

- `requests`
- `pandas`
- `seaborn`

Você pode instalá-las com o comando:

```bash
pip install requests pandas seaborn
```
## Como utilizar:

### Execute o script analise.py passando o nome desejado para o gráfico como argumento:
```
python analise.py <nome-do-grafico>
```
### Substitua <nome-do-grafico> pelo nome que você deseja dar ao arquivo de saída.
### O script irá gerar um arquivo taxa-cdi.csv com os dados extraídos e um gráfico PNG com o nome especificado.
