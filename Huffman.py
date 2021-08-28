# -*- coding: utf-8 -*-

class Huffman:
        
    class NoHeap:
        def __init__(self, char, freq):
            self.char = char
            self.freq = freq
            self.esq = None
            self.dir = None
            
        def __lt__(self, other):
            return self.freq < other.freq
        
        def __eq__(self, other):
            if(other == None):
                return False
            
            if(not isinstance(other, self.NoHeap)):
                return False
            return self.freq == other.freq
        
    def __init__(self, caminho):
        self.caminho = caminho
        self.heap = []
        self.cod = {}
        self.mapeamento_reverso = {}
        
    #cria a lista de frequencia
    def criar_frequencia(self, texto):
        
        #cria um array para armazenar a frequencia
        frequencia = {}
        
        #percorre cada letra do texto
        for char in texto:
            
            #se o caractere não estiver no array, iniciamos ele com 0. 
            #caso estiver no array, incrementamos a sua frequencia.
            if not char in frequencia:
                frequencia[char] = 0
            frequencia[char] += 1
            
        return frequencia
            
    #função para fazer o heap push
    def heapPush(self, valor):
        self.heap.append(valor)
        
        posinicio = 0
        pos = len(self.heap) - 1
        
        novoitem = self.heap[pos]
        while pos > posinicio:
            pospai = (pos - 1) >> 1
            pai = self.heap[pospai]
            if novoitem < pai:
                self.heap[pos] = pai
                pos = pospai
                continue
            break
        self.heap[pos] = novoitem
            
    #função para fazer o heap pop
    def heapPop(self):
        ultimolt = self.heap.pop()
        if self.heap:
            itemderetorno = self.heap[0]
            self.heap[0] = ultimolt
            
            pos = 0
            posfinal = len(self.heap)
            posinicial = pos
            novoitem = self.heap[pos]
            posfilho = 2*pos + 1
            while posfilho < posfinal:
                posdireita = posfilho + 1
                if posdireita < posfinal and not self.heap[posfilho] < self.heap[posdireita]:
                    posfilho = posdireita
                self.heap[pos] = self.heap[posfilho]
                pos = posfilho
                posfilho = 2*pos + 1
            self.heap[pos] = novoitem
            
            novoitem = self.heap[pos]
            while pos > posinicial:
                parentpos = (pos - 1) >> 1
                parent = self.heap[parentpos]
                if novoitem < parent:
                    self.heap[pos] = parent
                    pos = parentpos
                    continue
                break
            self.heap[pos] = novoitem
            
            return itemderetorno
        return ultimolt
    
    #cria a heap com base na frequencia
    def criar_heap(self, frequencia):
        for chave in frequencia:
            no =  self.NoHeap(chave, frequencia[chave])
            
            #joga no final do heap
            self.heapPush(no)
        
    #cria a árvore de Huffman
    def merge_e_cria_codigo(self):
        while(len(self.heap) > 1):
            
            #retira os 2 primeiros elementos da árvore
            no1 =  self.heapPop()
            no2 = self.heapPop()
            
            merged = self.NoHeap(None, no1.freq + no2.freq)
            merged.esq = no1
            merged.dir = no2
            
            self.heapPush(merged)
            
        raiz = self.heapPop()
        cod_atual = ""
        self.cria_codigo_recursiva(raiz, cod_atual)
        
    #função recursiva para definir as posições na árvore de Huffman
    def cria_codigo_recursiva(self, no, cod_atual):
        if(no == None):
            return
        
        if(no.char != None):
            self.cod[no.char] = cod_atual
            self.mapeamento_reverso[cod_atual] = no.char
            
        self.cria_codigo_recursiva(no.esq, cod_atual + "0")
        self.cria_codigo_recursiva(no.dir, cod_atual + "1")
        
    #cria o texto codificado
    def pegar_texto_codificado(self, texto):
        texto_codificado = ""
        
        for char in texto:
            texto_codificado += self.cod[char]
        
        return texto_codificado
    
    #cria o padding no texto codificado(para ser decodificado depois)
    def pad_texto_codificado(self, texto_codificado):
        padding_extra = 8 - len(texto_codificado) % 8
        
        for i in range(padding_extra):
            texto_codificado += "0"
            
        padded_info = "{0:08b}".format(padding_extra)
        texto_codificado = padded_info + texto_codificado
        
        return texto_codificado
        
    def pegar_array_de_byte(self, padded_texto_codificado):
        b = bytearray()
        
        for i in range(0, len(padded_texto_codificado), 8):
            byte = padded_texto_codificado[i:i+8]
            b.append(int(byte, 2))
            
        return b
    
    #função de compressão
    def comprimir(self):
        
        #pega o caminho do arquivo que vai ser comprimido
        entrada_caminho = self.caminho
        
        #saída do arquivo depois de comprimido
        saida_caminho = "ArquivosComprimidos/Comprimido_1.dvz"
        
        #abre os arquivos, o primeiro é o que vai ser comprimido,
        #o segundo é o arquivo comprimido.
        with open(entrada_caminho, 'r+') as arquivo, open(saida_caminho, 'wb') as saida:
            texto = arquivo.read()
            texto = texto.rstrip()
            
            #cria a fila de frequencia
            frequencia = self.criar_frequencia(texto)
            
            #cria a heap com a fila de frequencia
            self.criar_heap(frequencia)
            
            #cria a árvore de Huffman
            self.merge_e_cria_codigo()
            
            #codifica o texto
            texto_codificado = self.pegar_texto_codificado(texto)
            
            #coloca o padding no texto codificado(utilizado para descomprimir)
            paddded_texto_codificado = self.pad_texto_codificado(texto_codificado)
            
            #pega o array de bytes
            b = self.pegar_array_de_byte(paddded_texto_codificado)
            
            #cria o arquivo codificado
            saida.write(bytes(b))
            
            print("Arquivo comprimido.")
            return saida_caminho
            
    #remove o padding do texto codificado
    def remover_padding(self, bit_string):
        padded_info = bit_string[:8]
        padding_extra = int(padded_info, 2)
        
        bit_string = bit_string[8:]
        texto_codificado = bit_string[:-1*padding_extra]
        
        return texto_codificado
        
    #decodifica o texto(após retirar o padding)
    def decodifica_texto(self, texto_codificado):
        cod_atual = ""
        texto_decodificado = ""
        
        for bit in texto_codificado:
            cod_atual += bit
            if(cod_atual in self.mapeamento_reverso):
                char = self.mapeamento_reverso[cod_atual]
                texto_decodificado += char
                cod_atual = ""
                
        return texto_decodificado
            
    #função que realiza a descompressão do arquivo
    def descompressao(self, input_path):
        
        #caminho onde o arquivo que será descomprimido irá ficar
        saida_caminho = "ArquivosComprimidos/Descomprimido_1.txt"
        
        #abre os arquivos, o primeiro é o que vai ser descomprimido,
        #o segundo é o arquivo descomprimido.
        with open(input_path, 'rb') as arquivo, open(saida_caminho, 'w') as saida:
            bit_string = ""
            
            byte = arquivo.read(1)
            
            while(len(byte) > 0):
                byte = ord(byte)
                bits = bin(byte)[2:].rjust(8, '0')
                bit_string += bits
                byte = arquivo.read(1)
                
            #remove o padding do arquivo para decodificar o texto
            texto_codificado = self.remover_padding(bit_string)
            
            #decodifica o texto passando o texto codificado sem o padding
            texto_decodificado = self.decodifica_texto(texto_codificado)
            
            #escreve o texto decodificado no arquivo descomprimido
            saida.write(texto_decodificado)
            
            #mensagem de confirmação
            print("Arquivo descomprimido no seguinte caminho:")
            
            return saida_caminho
        
#variável que recebe o caminho do arquivo à ser comprimido
caminho = "ArquivosCompressor/Compressor_1.txt"

#inicializa a estrutura com o caminho do arquivo à ser comprimido
huff = Huffman(caminho)

#inicia a compressão
huff.comprimir()

#precisa informar o caminho do arquivo comprimido para realizar a descompressão
caminho_saida = huff.descompressao("ArquivosComprimidos/Comprimido_1.dvz")

print (caminho_saida)