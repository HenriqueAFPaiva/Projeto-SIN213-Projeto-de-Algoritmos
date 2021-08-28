# -*- coding: utf-8 -*-

#função insertion sort
def InsertionSort(array):
    
    #percorrendo o array inteiro
    for x in range(0, len(array)):
        
        while x > 0:
            #se o elemento da esquerda for maior que o atual, trocamos eles de posição
            if array[x - 1] > array[x]:
                array[x], array[x - 1] = array[x - 1], array[x]
            x -= 1
            
#abrindo o arquivo para a leitura
arquivo = open("ArquivosOrdenacao/entrada100000.txt", "r")

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

#chamamos o selection sort e calculamos o tempo
inicio = time.time()
InsertionSort(array)
fim = time.time()
tempo_total = fim - inicio

print(tempo_total)