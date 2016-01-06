#embaralhando numeros aleatorios

def embaralha(s):
	import random 
	lista = list(s)
	random.shuffle(lista)
	return ' '.join(lista)

print embaralha('palavra')


#gerar lista com 100 inteiros aleatorios nao repetidos 
import random 
lista2 = []

for k in range(100):
	x = random.randint(10,100)
	if x not in lista2:
		lista2.append(x)
print lista2


#video 298