
conta = int(raw_input("Valor da conta: "))
dinheiro = int(raw_input("Dinheiro: "))

troco = conta - dinheiro
cq = 0
vt = 0
dz = 0
cn = 0
ds = 0
um = 0

while troco != 0:
	if troco >= 50:
		cq+=1
		troco -= 50
	elif troco >= 20:
		vt+=1
		troco -= 20
	elif troco >= 10:
		dz+= 1
		troco -= 10
	elif troco >= 5:
		cn+=1
		troco-=5
	elif troco >= 2:
		ds+=1
		troco -=2
	else:
		um+=1
		troco-=1


print ("Melhor troco possivel:")
print ("%d notas de 50, %d notas de 20, %d notas de 10 , %d notas de 5, %d notas de 2 e %d notas de 1" %(cq, vt, dz,cn, ds, um))


