#!/bin/bash

# Verifica se a quantidade correta de argumentos foi fornecida
if [ $# -ne 1 ]; then
    echo "Uso: $0 <URL>"
    exit 1
fi

# Pega a URL passada como argumento
url="$1"

# Faz a requisição HTTP para a página
response=$(curl -s "$url")

# Verifica se a requisição foi bem-sucedida
if [ $? -eq 0 ]; then
    # Faz o parse do conteúdo HTML da página e extrai os dados da tabela
    table_data=$(echo "$response" | grep '<table>' -A 999999 | grep -m 1 '</table>')
    
    # Extrai valores da tabela
    values=$(echo "$table_data" | grep '<td>' | sed -e 's/<[^>]*>//g' -e 's/^\s*//g' -e 's/\s*$//g')
    
    # Loop para gerar JSON
    json_data="{"
    count=1
    for value in $values; do
        json_data="$json_data \"col$count\": \"$value\","
        count=$((count+1))
    done
    json_data="${json_data%,} }"
    
    # Saída dos dados em formato JSON
    echo "$json_data"
else
    echo "Não foi possível acessar a página: $response"
fi
