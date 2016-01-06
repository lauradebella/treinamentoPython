min = int(raw_input('Insira os minutos utilizados:  '))

if min<200:
	p=0.2*min
elif min<400:
	p=0.18*min
elif min>800:
	p=0.08*min
else:
	p=0.15*min

print('Valor da conta : R$%.2f' %p )