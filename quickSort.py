import random
import time

def partition(array, inicio, fim):
    pivo = array[fim]
    i = inicio
    for j in range(inicio, fim):
        if array[j] <= pivo:
            array[j], array[i] = array[i], array[j]
            i+=1
    array[i], array[fim] = array[fim], array[i]
    return i



def quicksort (array, inicio=0, fim=None):
    if fim is None:
        fim = len(array)-1
    if inicio < fim:
        p = partition(array, inicio, fim)
        quicksort(array, inicio, p-1)
        quicksort(array, p+1, fim)

    
    

array = list(range(0,5000))
random.shuffle (array)
antes = time.time()
quicksort(array)
depois = time.time()
total = (depois-antes)

print(array)
print("O tempo total foi: ",total,"ms" )