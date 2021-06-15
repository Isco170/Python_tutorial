salario_minimo1 = 100
salario_minimo2 = 120
salario_total = 0
carro = 14000.00

quantCaros = int(input("Quantos carros vendeu? "))
comissaoCarro = 4000.00 * quantCaros
venda = 14000.00 * quantCaros
comissaoVenda = venda * 0.5

salario_total = (salario_minimo1 + salario_minimo2 + comissaoCarro + comissaoVenda)

print(salario_total)
