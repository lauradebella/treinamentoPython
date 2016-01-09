n  = int(raw_input("Insira um numero: "))

i = 2
flag = True

if n>2:
	while (i < n):
		if n % i == 0:
			flag = False
			break
		i += 1


if flag is True or n==1 or n==2:
	print ("Primo")
else:
	print ("Nao primo")