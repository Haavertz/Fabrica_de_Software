
#Utilização do input!

name = input (str("Qual seu nome? \n"))
print ("Seu nome é: ", name)


idade = input ("Digite sua idade: ")
print(type(idade))

'''float = Real
int = Inteiro 
str = String
bool = booleans'''


salario = int(input("Digite seu Salario: "))
imposto = float(input("Qual o valor do seu imposto: "))
total = salario + imposto
print (total)

#Placeholder = funcionalidade de %

'''inteiro == %d
string == %s
bool == %b
float == %f'''

a = 100
b = 200.5
c = "Gleison"

print ("O valor de A é: %d e o valor de B é: %.1f e o seu nome é: %s" %(a,b,c)) 

# Bom, %f é uma variavel do tipo float, quando eu puxar uma variavel ela tem que ser do tipo float (real), desta maneira tem de estar em ordem a qual variavel ira puxar
# dentro dos parenteses (). ex: %d (int = inteiro) e após o termino das "" colocarei (a = 100 -> inteiro), tem que ser do tipo inteiro pra adentrar ao %d caso não seja,
# dependendo do que tem dentro da variavel ele imprime. 

