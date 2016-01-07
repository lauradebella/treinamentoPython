#manipulando um vetor de inteiros

n = int(raw_input("Digite o numero de elementos do vetor: "))
v=[]
i = 0
while i<n:
	x = i+1
	aux = int(raw_input("Insira o %d-esimo elemento:  " %x))
	v.append(aux)
	i=i+1

#verificando o ultimo elemento
print ("Ultimo elemento : ")
print v[-1]

#imprimindo a ordem inversa
i=n-1
while i>=0:
	#print i 
	print v[i]
	i = i-1

x = 3

soma = 0
#percorrendo a lista, olhando cada elemento da lista
for x in v:
	#do something
	print("Temos %d na lista!!" %x)
	soma+=x

print ("soma dos elementos da lista = %d" %soma)

#for x in reversed(v)
#for x in sorted(v)

import copy 
import random 
#bibliotecas

nova = copy.deepcopy(v)

print random.sample(nova, 3)