# -*- coding: utf-8 -*-

#função selection sort
def SelectionSort(array):
    
    #percorrendo o array inteiro
    for indice in range(0, len(array)):
        
        #seta o primeiro elemento como menor elemento
        menor_indice = indice
        
        #percorremos o resto do array à partir do menor elemento
        for right in range(indice + 1, len(array)):
            
            #quando acharmos um item menor que o anterior, vamos substitui-lo
            if array[right] < array[menor_indice]:
                menor_indice = right
                    
        #então, trocamos as posições dentro do array
        array[indice], array[menor_indice] = array[menor_indice], array[indice]

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
SelectionSort(array)
fim = time.time()
tempo_total = fim - inicio

print(tempo_total)