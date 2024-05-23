"""
   Importe o módulo `datetime` e crie uma variável `data_atual` com a data e hora atuais. Use uma f-string para imprimir a data no formato "DD/MM/AAAA".
"""
from datetime import datetime

data_atual = datetime.now()

print(f'{data_atual.day:02}/{data_atual.month:02}/{data_atual.year:02}')