
n = int(raw_input("Insira um numero: "))

i = 2

while n > 1:
	if n % i == 0:
		n/=i
		print(" %d " %i )
	else:
		i+=1
