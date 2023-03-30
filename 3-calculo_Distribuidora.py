#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# ->O menor valor de faturamento ocorrido em um dia do mês;
#->O maior valor de faturamento ocorrido em um dia do mês;
#->Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.


import json

with open('dados.json', 'r') as arquivo:
    dados = json.load(arquivo)

faturamento_total = 0
for mes in dados:
    faturamento_total = faturamento_total + mes['valor']

maior_faturamento = 0
for dias in dados:
    valor = dias['valor']
    if valor > maior_faturamento:
        maior_faturamento = valor

media_mensal = sum([dia['valor']for dia in dados ]) / len(dados)

dias_acima = 0
for dia in dados:
    if dia['valor'] > media_mensal:
        dias_acima = dias_acima + 1

print(f'O faturamento total é de R$: {faturamento_total:.2}.')

print(f"O maior valor de faturamento em um dia do mês foi R$: {maior_faturamento:.2f}")

print(f"O número de dias de faturamento acima é: {dias_acima} dias.")