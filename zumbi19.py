#modulos 

import random 
#dir random mostra os modulos de random

print random.randint(1, 100)

print random.choice(['Laura', 'Gilmar', 'Vitor'])

lista = ['Laura', 'Gilmar', 'Vitor']
random.shuffle(lista)
print lista