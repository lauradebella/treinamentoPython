#contador de consoantes em um conjunto de letras

p = []
i = 1
print ("Insira 10 letras ")
while i<=10:
	p.append(raw_input())
	i+=1
i = 0
cont = 0
while i<= 9:
	if p[i] not in 'aeiou':
		cont+=1
	i+=1

print ("Existem %d consoantes" %cont)