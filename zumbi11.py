#euclides

n1 = int(input("insira o primeiro numero : "))
n2 = int(input("Insira o segundo numero : "))

while n1%n2 != 0 :
	n1,n2 = n2,n1%n2

print ("O mdc dos dois numeros e %d" %n2)