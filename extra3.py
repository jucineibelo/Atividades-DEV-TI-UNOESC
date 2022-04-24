'''
3 – (Baseado no problema 1009 do Beecrowd) Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas 
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o 
total a receber no final do mês, com duas casas decimais.

'''

nome = input("Qual o nome do vendedor? ")
salarioFixo = float(input("Qual o salario fixo do vendedor? "))
comissao = float(input("Quanto o vendedor ganhou de comissão? "))
percentualComissao = (15/100) * salarioFixo 
totalBruto = salarioFixo + percentualComissao + comissao

print("No final do mês",nome,"ganhará um total de",round(totalBruto,2) )



