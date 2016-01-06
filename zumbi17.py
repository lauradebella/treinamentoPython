#mes de aniversario 

dia, mes, ano = raw_input("Data (dd/mm/aaaa): ").split("/")
meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho', 'julho','agosto', 'setembro', 'outubro', 'novembro', 'dexembro']

print("Voce nasceu em %s " %meses[int(mes)-1])