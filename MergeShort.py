# -*- coding: utf-8 -*-

#função merge
def Merge(array, aux, inicio, meio, fim):

    for x in range(inicio, fim + 1):
        aux[x] = array[x]
        
    i = inicio
    y = meio + 1
    
    for x in range(inicio, fim + 1):
        if i > meio:
            array[x] = aux[y]
            y += 1
        elif y > fim:
            array[x] = aux[i]
            i += 1
        elif aux[y] < aux[i]:
            array[x] = aux[y]
            y += 1
        else:
            array[x] = aux[i]
            i += 1

#função merge sort
def MergeSort(array, aux, inicio, fim):
    if fim <= inicio:
        return
    meio = (inicio + fim) // 2

    # Ordena a primeira metade do arranjo.
    MergeSort(array, aux, inicio, meio)

    # Ordena a segunda metade do arranjo.
    MergeSort(array, aux, meio + 1, fim)

    # Combina as duas metades ordenadas anteriormente.
    Merge(array, aux, inicio, meio, fim)

#abrindo o arquivo para a leitura
arquivo = open("ArquivosOrdenacao/entrada1000000.txt", "r")

#criando um array para receber os elementos do arquivo
array = []

#preenche o array com todos os elementos do arquivo
for line in arquivo:
    array.append(int(line))
    
#fecha o arquivo
arquivo.close

#ordena o array de forma crescente
#array.sort()

#ordena o array de forma decrescente
array.sort(reverse=True)

#importando a biblioteca 'time'
import time

#definindo o auxiliar
aux = [0] * len(array)

#chamamos o selection sort e calculamos o tempo
ini = time.time()
MergeSort(array, aux, 0, len(array) - 1)
fim = time.time()
tempo_total = fim - ini

print(tempo_total)