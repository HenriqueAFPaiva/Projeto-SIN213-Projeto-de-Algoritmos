# -*- coding: utf-8 -*-

#função shell sort
def ShellSort(array):
  
    x = len(array)
    dividido = x // 2
  
    while dividido > 0:
  
        for i in range(dividido, x):
            temp = array[i]
  
            y = i
            
            while  y >= dividido and array[y - dividido] > temp:
                array[y] = array[y - dividido]
                
                y -= dividido
  
            # put temp (the original a[i]) in its correct location
            array[y] = temp
        dividido = dividido // 2

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

#chamamos o selection sort e calculamos o tempo
inicio = time.time()
ShellSort(array)
fim = time.time()
tempo_total = fim - inicio

print(tempo_total)