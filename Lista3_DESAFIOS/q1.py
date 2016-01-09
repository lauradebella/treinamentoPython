n = int(raw_input('Insira um numero: '))
i = 1
flag = 0

if n > 6:
	while(i+1 < n):
		if (i * (i+1) * (i+2)) == n:
			print("E triangular !!")
			flag = 1
			break
		i += 1

elif n < 6 or flag == 0:
	print ("Nao e triangular!")
