"""Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

Nome do produto: "Camiseta",
Preço original: R$ 50.00,
Porcentagem de desconto: 20%,
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes.
"""

nome_do_produto = "camiseta"
preco_original = 50.00
porcentagem_desconto = 20
valor_do_desconto = preco_original * (porcentagem_desconto / 100)
resultado = preco_original - valor_do_desconto

print(resultado)
