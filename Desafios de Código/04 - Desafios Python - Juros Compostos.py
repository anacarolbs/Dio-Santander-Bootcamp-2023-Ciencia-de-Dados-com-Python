""" DIO - Santander Bootcamp 2023 - Ciência de Dados com Python

Desafios Python: Juros Compostos

Desafio
Imagine que você está desenvolvendo um aplicativo para um banco que deseja calcular os juros compostos de um investimento. Seu objetivo é criar uma função que receba três parâmetros: o valor inicial do investimento, a taxa de juros anual e o período de tempo em anos. A função deve calcular e retornar o valor final do investimento após o período determinado, levando em consideração os juros compostos.

Entrada:
A função deve receber os seguintes parâmetros:
valor_inicial: um número inteiro ou decimal representando o valor inicial do investimento.
taxa_juros: um número decimal representando a taxa de juros anual. Por exemplo, se a taxa for de 5%, o valor passado será 0.05.
periodo: um número inteiro representando a quantidade de anos do investimento.

Saída:
A função deve retornar o valor final do investimento após o período determinado, considerando os juros compostos. O valor final deve ser arredondado para duas casas decimais.

Exemplos
A tabela abaixo apresenta exemplos com alguns dados de entrada e suas respectivas saídas esperadas. Certifique-se de testar seu programa com esses exemplos e com outros casos possíveis.

Entrada       Saída
5000
0.08          Valor final do investimento: R$ 7346.64
5

1000
0.06          Valor final do investimento: R$ 1191.02
3

20000
0.04          Valor final do investimento: R$ 29604.89
10

"""

valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial

# TODO: Iterar, baseado no período em anos, para calculo do valorFinal com os juros.
for _ in range(periodo):
    valor_final *= (1 + taxa_juros)

print("Valor final do investimento: R$", round(valor_final, 2))
