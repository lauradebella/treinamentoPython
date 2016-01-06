#palindromo e funcoes para strings 

p = raw_input("Insira a palavra ")

if p == p[::-1]:
	print ("E palindromo ")
else:
	print ("Nao e palindromo")


##strings sao imutaveis para serem rapidas

p = '@lalala_'+p[:]
print p

t = len(p)
print ("%d " %t)

# funcoes interessantes 
# p.startswith('l')
# p.endswith('')
# p.lower()    p.upper()
# 

if p.lower() in '@lalala_a @lalala_o @lalala_i @lalala_e @lalala_u ':
	print("A palavra inicial so continha vogais")

print
print
print("tigres : ")
s = 'um tigre, dois tigres, tres tigres'
n = s.find('tigre')
print n 
print s.replace('tigre', 'gato')
print s

print s.split()
print s.split(',')

print
print
times = ['Galo', 'Cruzeiro']
print '>>'.join(times)








 