
#Numa eleição existem três candidatos. Faça um programa que peça o numero total de eleitores.
#Peça para cada eleitor votar e ao final mostrar o numero de votos cada canditado

nomb = int(input("Quantos quandidatos desejam VOTAR? "))
vinni = 0 
duardin = 0
robertin = 0
for nomba in range(nomb):
     print ("\n","1 - ROBERTIN DU PROGRAMA \n 2 - VINNICIUS CAÇADOR DE RATO \n 3 - DUARDIN O GNOMIO \n 4 - BREAK")
     number = int(input("DIGITE O CANDITADO QUE DESEJA VOTAR: "))
     if number == 1:
          robertin = robertin + 1
     elif number == 2:
          vinni = vinni + 1
     elif number == 3:
          duardin = duardin + 1
     else:
          print ("Numero informado não e valido.")
          continue
total = vinni+robertin+duardin
print ("Eleitor Duardin:",duardin)
print ("Eleitor Vinnicius:",vinni)
print ("Eleitor Robertin:",robertin)
print ("Total:", total)