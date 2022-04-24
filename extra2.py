'''
2 - Escreva um programa que informe o ano atual, o nome do aluno, o dia, o mês por extenso e o ano de seu nascimento e imprima:

Olá, Fulano de Tal
No dia  XX de XXXXXXXX parabéns pelo aniversário de seus XX anos

'''

anoAtual = int(input("Digite o ano atual? "))
nome = input("Digite o nome do aluno? ")
dia = int(input("Digite qual o dia que o aluno nasceu? "))
mes = input("Digite qual foi o mês que o aluno nasceu? ")
anoNascimento = int(input("Digite em qual ano o aluno nasceu? "))





print("Olá",nome,"\n" "No dia",dia,"de",mes,"parabéns pelo seu aniversário de seus", anoAtual-anoNascimento)




