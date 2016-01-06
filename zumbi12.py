# listas 

#listas de tipos diferentes 

l = ["teste", 1]
l.append("Oi")

print(l[1])
print(l[2])

l[1] = 10
print(l[1])

media = [5, 6, 7, 8, 9]
n=0
soma = 0
while n<=4:
	soma+=media[n]
	n=n+1

print("Media das notas %.1f" %(soma/5))	 