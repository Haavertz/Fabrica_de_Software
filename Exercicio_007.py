#Concatenação = Junção das strings (print)

a = "Gleison"
b = "Morais"
print ("Prezado "+a+" "+b+"" ". Olá!")

#Replicação de Strings

print (2*"Gleison\n") #pedir para escrever a string com determinado numero de vezes

print ("+" + 10 *"-" + "+")
print (("|" + " "*10 + "|\n") * 5, end="")
print ("+" + 10 *"-" + "+")

nome = input("Qual seu nome: ")
valor = int(input("Quantas veses você deseja repetir esse nome? "))

print (valor* ("%s \n" %(nome)))