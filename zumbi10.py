n = int(raw_input("insira o n:  "))

a, b = 1,1
k = 1

while k<= n-2 :
	a,b = b, a+b
	k = k+1
	
print("Fibonati na posicao %d = %d" %(n,b))