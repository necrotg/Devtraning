import random #importa lib de misturar vetor
import time #importa lib do tempo

def sort (array):#funcao de ordenacao
    for p in range(0, len(array)):
        current_element = array[p] #guarda o elemento atual do array

        while p > 0 and array[p-1] > current_element: # enquanto o elemento for de tras for maior que elemento atual ele continua
            array[p] = array[p-1] #faz a troca dos elementos
            p-= 1 #diminui um no indicie 

        array[p] = current_element

array = list(range(0,2000))
random.shuffle (array)
antes = time.time()
sort(array)
depois = time.time()
total = (depois-antes)

#print(array)
print("O tempo total foi: ",total,"ms" )