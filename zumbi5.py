v = int(raw_input('Insira a velocidade do veiculo : '))
if v>110:
	v-=110;
	m=v*5;
	print('O veiculo foi multado em  %d reais!' %m)
else:
	print('O veiculo nao foi multado ')