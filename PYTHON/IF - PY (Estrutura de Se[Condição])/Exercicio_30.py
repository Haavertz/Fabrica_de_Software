turno=input("Qual turno você estuda? (M-V-N)")
turno = turno.upper()
if (turno == 'M'):
    print ("Bom dia!")
elif (turno == 'V'):
    print ("Boa tarde!")
elif (turno == 'N'):
    print ("Boa noite!")
else:
    print("Valor invalido!")
