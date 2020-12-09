import random
import time

def partition(array, inicio, fim): #funcao de particicao
    pivo = array[fim] #definicao do pivo, sempre ultima posição
    i = inicio #define o i como variavel de inicio
    for j in range(inicio, fim): #for para pegar o array inteiro
        if array[j] <= pivo: #compara com o pivo
            array[j], array[i] = array[i], array[j] # troca as posições do array
            i+=1 #avança uma casa pra direita
    array[i], array[fim] = array[fim], array[i] #troca as posições
    return i #retorna i 



def quicksort (array, inicio=0, fim=None): #define a funcao de do quicksort
    if fim is None: 
        fim = len(array)-1 #pega o array inteiro, pois começa no 0
    if inicio < fim: 
        p = partition(array, inicio, fim)
        quicksort(array, inicio, p-1)
        quicksort(array, p+1, fim)




array = list(range(0,1000))
random.shuffle (array)
antes = time.time()
quicksort(array)
depois = time.time()
total = (depois-antes)

print(array)
print("O tempo total foi: ",total,"ms" )