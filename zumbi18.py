#funcoes 



def epar(x):
	return x%2==0

for i in range(10) : print (epar(i))




def fat(x):
	f = 1
	while x>=1:
		f=f*x
		x=x-1
	return f


for i in range(5) : print (fat(i))


print("Variaveis locais e globais")
a = 1
def muda():
	global a 
	a = 7

print a
muda()
print a	