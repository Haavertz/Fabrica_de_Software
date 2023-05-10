
nome = input("Qual o nome do aluno: ")
serie = input("Serie do aluno: ")
escola = input("Escola do aluno: ")
cidade = input("Qual a cidade do aluno: ")

#Calcular a media do aluno com input

nota1 = int(input("Qual o valor da primeira nota? "))
nota2 = int(input("Qual o valor da segunda nota? "))
nota3 = int(input("Qual o valor da terceira nota? "))
nota4 = int(input("Qual o valor da quarta nota? "))

result = (nota1 + nota2 + nota3 + nota4)/4

print ("Olá, %s da escola %s da cidade %s e da serie %s, calculamos sua media que é: %d" %(nome,escola,cidade,serie,result))