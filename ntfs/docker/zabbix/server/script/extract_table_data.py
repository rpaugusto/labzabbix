#!/usr/bin/env python

import sys
import requests
from bs4 import BeautifulSoup
import json

# Verifica se a URL foi fornecida como argumento
if len(sys.argv) != 2:
    print("Uso: python extract_table_data.py <URL>")
    sys.exit(1)

# Pega a URL da linha de comando
url = sys.argv[1]

# Faz a requisição HTTP para a página
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Faz o parse do conteúdo HTML da página
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Encontra a tabela pelo nome, classe CSS ou tag HTML, dependendo do seu caso
    # Por exemplo, para encontrar uma tabela com a classe CSS 'tabela-dados':
    table = soup.find('table', class_='tabelaListagemDados')
    
    # Inicializa listas para armazenar os dados
    headers = []
    rows = []
    
    # Extrai os cabeçalhos da tabela
    th_elements = table.find_all('th')
    headers = [th.get_text(strip=True) for th in th_elements]
    
    # Extrai as linhas da tabela
    tr_elements = table.find_all('tr')
    for tr in tr_elements[1:]:  # Ignora a primeira linha de cabeçalho
        td_elements = tr.find_all('td')
        row = []
        for td in td_elements:
            img_element = td.find('img')  # Busca o elemento <img>
            if img_element and 'bola_verde_P' in img_element['src']:
                row.append(1)  # Valor 1 para texto "bola_verde_P"
            elif img_element and 'bola_vermelho_P' in img_element['src']:
                row.append(3)  # Valor 1 para texto "bola_verde_P"
            elif img_element and 'bola_amarela_P' in img_element['src']:
                row.append(2)  # Valor 1 para texto "bola_verde_P"
            else:
                row.append(td.get_text())  # Pega o texto se não houver <img>
        rows.append(row)
    
    # Cria uma lista de dicionários para os dados
    data = []
    for row in rows:
        data_entry = {}
        for i, header in enumerate(headers):
            data_entry[header] = row[i]
        data.append(data_entry)
    
    # Converte a lista de dicionários em formato JSON
    json_data = json.dumps(data, indent=4)
    
    # Imprime os dados em formato JSON
    print(json_data)
else:
    print("Não foi possível acessar a página:", response.status_code)
