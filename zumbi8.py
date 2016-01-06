#fatorial de n

produto =1
x = int(raw_input("Insira um numero para calcular o fat: "))

while x>=1 :
	produto = x*produto
	x=x-1

print("Fatorial = %d" %produto) 