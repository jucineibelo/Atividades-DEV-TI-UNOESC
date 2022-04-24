'''
4 - Um corredor está se preparando para disputar uma competição no final deste mês, ele já realizou 3 treinos na semana passada. Faça um 
programa que seja capaz de receber as informações de cada um destes treinos: quilômetros percorridos e minutos de corrida.

Com estas informações realize os cálculos necessários para mostrar o seguinte relatório:
- Total de quilômetros percorridos;
- Média de quilômetros percorridos;
- Total de minutos de corrida;
- Média de minutos de corrida.

'''

treino1 = float(input("Quantos km o atleta percorreu no primeiro treino ? "))
tempo1 = float(input("Em quantos minutos o atleta fez o percurso? "))
treino2 = float(input("Quantos km o atleta percorreu no segundo treino ? "))
tempo2 = float(input("Em quantos minutos o atleta fez o percurso? "))
treino3 = float(input("Quantos km o atleta percorreu no terceiro treino ? "))
tempo3 = float(input("Em quantos minutos o atleta fez o percurso? "))
totalKmpercorrido = treino1 + treino2 + treino3
MediaKmpercorrido = totalKmpercorrido / 3 
totalMinPercorrido = tempo1 + tempo2 + tempo3
mediaMinPercorrido = totalMinPercorrido / 3
print("- Total de quilômetros percorridos;", round(totalKmpercorrido,2))
print("- Média de quilômetros percorridos;", round(MediaKmpercorrido,2))
print("- Total de minutos de corrida;", round(totalMinPercorrido,2))
print("- Média de minutos de corrida.", round(mediaMinPercorrido,2))



