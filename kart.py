import random

nomes = ['Kaua', 'Thiago', 'Lucas', 'Pedin', 'Marcelo', 'Saulin']
matriz = []

for lin in range(10):
    colunas = []
    for col in range(6):
        tempo = int(round(random.uniform(100,200),0))
        colunas.append(tempo)
    matriz.append(colunas) 
print(matriz)

print('\t'.join(nomes))
for lin in range(10):
    print('\t'.join(str(matriz[lin][col]) for col in range(6)))

menor_volta = matriz[0][0]
melhor_volta = (0,0)

for i,linha in enumerate(matriz):
    for j,elemento in enumerate(linha):
        if elemento < menor_volta:
            menor_volta = elemento
            melhor_volta = (i,j)

nome_melhor_volta = nomes[melhor_volta[1]]
volta_melhor_volta = melhor_volta[0] + 1 

print(f'\nA melhor volta da prova foi de {menor_volta} segundos, feita por {nome_melhor_volta} na volta {volta_melhor_volta}.')



#não consegui fazer a 'Classificação final em ordem


medias = []

for volta in matriz:
    media_volta = sum(volta) / len(volta)
    medias.append(media_volta)


volta_media_rapida = 1  
melhor_media = medias[0]

for i in range(1, len(medias)):
    if medias[i] < melhor_media:
        melhor_media = medias[i]
        volta_media_rapida = i + 1  

print(f'A volta com a média mais rápida foi a volta {volta_media_rapida}.')