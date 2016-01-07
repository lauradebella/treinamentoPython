#tabuada ate determinado elemento

t=1
n = int(raw_input("Insira a tabuada maxima: "))
while t<=n :
	print("Tabuada de %d" %t)
	aux = 1
	while aux<=10 :
		print("%d x %d = %d" %(t, aux, aux*t))
		aux = aux+1
	t = t +1