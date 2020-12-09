import random
import time

def sort (array):
    for index in range(0, len(array)): #for para ver ver todo o array
        min_index = index

        for right in range(index + 1, len(array)): #for para para ver os items da direita
            if array[right] < array[min_index]: #verifica se o item é menor
                min_index = right     #faz a troca do menor item
        array[index], array[min_index] = array[min_index], array[index] #faz a troca dos elementos
    

array = list(range(0,100))
random.shuffle (array)
antes = time.time()
sort (array)
depois = time.time()
total = (depois-antes)

#print(array)
print("O tempo total foi: ",total,"ms" )