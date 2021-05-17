import json
import random

from uuid import uuid4

temp_file = 'src/produtos/fixtures/temp.json'
final_file = 'biscoito_maizena.json'

arq_final = open(f'src/produtos/fixtures/{final_file}', 'a')
data = []

with open(temp_file) as temp_json:
    data = json.load(temp_json)

    print('Criando dicionário auxiliar')
    data_final = []
    estabelecimentos = [
        "38c550c7-23c4-4e21-8b42-40fb329e6f7b",
        "66289ac4-58c0-493a-8d54-2eda92aa1a75",
        "2bd66ad6-35e8-4b1d-aa13-631a20325750",
        "07012e3f-57d7-418d-aa26-d05c27471d58",
        "07012e3f-57d7-418d-aa26-d05c27471d58",
        "07012e3f-57d7-418d-aa26-d05c27471d59"
    ]


    print('Arquivo carregado')
    for i, _ in enumerate(data):
        del(data[i]['id'])
        del(data[i]['ncm'])
        del(data[i]['cdanp'])
        del(data[i]['distkm'])
        del(data[i]['gtin'])
        del(data[i]['nrdoc'])
        data[i]['estabelecimento'] = random.choice(estabelecimentos)

        data_final.append({
            'model': 'produtos.produto',
            'pk': str(uuid4()),
            'fields': data[i]
        })

    print('-- gerando uuids unicos')
    print('-- Limpeza das linhas realizada')

    json.dump(data_final, arq_final)
    print('-- Dados salvos no arquivo final criado')

print('Processo finalizado.')
