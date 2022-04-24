'''
4) Faça um algoritmo que leia a idade de uma pessoa expressa em anos, meses e
dias e escreva a idade dessa pessoa expressa apenas em dias. Considerar ano com
365 dias e mês com 30 dias.
'''

ano = int(input("Qual a idade? "))
meses = int(input("Quantos meses? "))
dias = int(input("Quantos dias? "))

ano = ano * 365
meses = meses * 30

print("A pessoa tem", ano + meses + dias,"dias de vida")
