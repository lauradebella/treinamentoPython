#imprime pares menores que 10 

x = 10
fim = int(input("Digite um numero maior que 10:  "))
while x<=fim :
	#apenas pares
	if x%2 == 0 :
		print(x)
	x+=1