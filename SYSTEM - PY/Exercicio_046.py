import os
while True:
    
    print("*",70*"-","*")
    print("|",70*" ","|")
    print(("|"+13*" "+"Seja Bem Vindo a Calculadora feita para você!!"+13*" "+"|"))
    print("|",70*" ","|")
    print("*",70*"-","*")

    print()
    print("* ",68*"="," *\n")
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"A.Q"+7*" "+"|"+7*" "+"R.Q"+8*" "+"|"+8*" "+"/"+8*" "+"|"+8*" "+"*"+8*" "+"|")) 
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"V.C"+7*" "+"|"+8*" "+"9"+9*" "+"|"+8*" "+"+"+8*" "+"|"+8*" "+"-"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2) 
    print("* ",68*"-"," *")
    
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+7*" "+"M.4"+7*" "+"|"+8*" "+"6"+9*" "+"|"+8*" "+"7"+8*" "+"|"+8*" "+"8"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+8*" "+"F"+8*" "+"|"+8*" "+"3"+9*" "+"|"+8*" "+"4"+8*" "+"|"+8*" "+"5"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"-"," *")

    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print(("|"+8*" "+"E"+8*" "+"|"+8*" "+"0"+9*" "+"|"+8*" "+"1"+8*" "+"|"+8*" "+"2"+8*" "+"|"))
    print(("|"+17*" "+"|"+" "+17*" "+"|"+17*" "+"|"+17*" "+"|\n")*2)
    print("* ",68*"="," *")

    print()

    print("* ",80*"="," *")
    caracter = (input("Escolha uma operação especial\n \
    Aviso:Apos escolher esta operaçâo desconsidere a escolha de numeros.\n \
    Operações permitidas: \nM.4 - Media de 4 números\nV.C - Volume de um cubo\nF - Fatorial\n" 
    "E - Exponenciaçâo\nA.Q - Area de um quadrado\nR.Q - raio de um quadrado\nDigite '0' para operações basicas\nEscolha:"))
    print("* ",80*"="," *")
    caracter = caracter.upper()
    print(caracter)
    print()

    print("* ",68*"="," *")
    print("|"+"Caso tenha escolhido uma das operações especias desconcidere isso"+35*" ") 
    print("|"+36*" "+35*" ") 
    num1 = int(input("|"+" Digite o primeiro numero:      "+" "))
    caracte = input("|"+" Digite a operação que deseja:  "+" ")
    num2 = int(input("|"+" Digite o segundo numero:       "+" "))
    print("|"+36*" "+35*" ") 
    print("* ",68*"="," *")

    print()

    if caracte == '+':   #Adição
        soma = (num1+num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "*30+f"{num1} + {num2} = {soma}"+32*" "+"|")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    
    elif caracte == '-': #Subtraçâo
        soma = (num1-num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "*30+f"{num1} - {num2} = {soma}"+32*" "+"|")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        

    elif caracte == '*': #Multiplicaçâo
        soma = (num1*num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "*30+f"{num1} * {num2} = {soma}"+32*" "+"|")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    elif caracte == '/': #Divisâo
        soma = (num1/num2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "*30+f"{num1} / {num2} = {soma}"+32*" "+"|")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")

        #Operações difente do comum

    elif caracter == 'E': # Exponenciaçâo
        n1 = int(input("Digite o primeiro numero: "))
        n2 = int(input("Digite o primeiro numero: "))
        soma = (n1 ** n2)
        
        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "*30+f"{n1} ** {n2} = {soma}"+32*" "+"|")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    elif caracter == 'F':  # Fatorial
        fato = int(input("Digite um numero para fotorar: "))
        cont = 1
        som = 1
        while cont <= fato:
            som = som * cont
            cont = cont + 1
            # aqui tem que mostrar o calulo 
            print("* ",68*"="," *")
            print("|"+36*" "+35*" "+"|")  
            print(" "*30+f"{fato} = {som}")
            print("|"+36*" "+35*" "+"|")  
            print("* ",68*"="," *")
        
    elif caracter == 'R.Q':  # Raiz quadrada
        num4 = int(input("Digite o numero: "))
        soma1 = (num4**0.5)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"{num1} = {soma}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    elif caracter == 'A.Q':  # Area de um quadrado
        nu1 = int(input("Digite o primeiro numero: "))
        nu2 = int(input("Digite o primeiro numero: "))
        som = (nu1*nu2)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"'lado'{nu1} * 'lado'{nu2} = {som}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    elif caracter == 'V.C':  # Volume de um cubo
        a = float(input("Digite a altura do cubo:"))
        soma5 = (a*a*a)

        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print(" "*30+f"A altura é {a} e o volume é {soma5}")
        print("|"+36*" "+35*" "+"|")  
        print("* ",68*"="," *")
        
    elif caracter == 'M.4':  # Media de 4 numeros
        nota1 = float(input("Primeira nota: "))
        nota2 = float(input("Segunda nota: "))
        nota3 = float(input("Terceira nota: "))
        nota4 = float(input("Quarta nota:  "))
        soma = ((nota1+nota2+nota3+nota4)/4)
        txt = [nota1,nota2,nota3,nota4]
        soma1 = sum(txt)
        txt1 = len(txt)
        print(soma1)
        print(txt1,"ola")
        # aqui tem que mostrar o calulo 
        print("* ",68*"="," *")
        print("|"+36*" "+35*" "+"|")  
        print("|"+" "+f" as suas notas foram {nota1}, {nota2}, {nota3}, {nota4} é a sua media foi : {soma}",end=" ")
        print(" |")  
        print("|"+36*" "+35*" "+"|") 
        print("* ",68*"="," *")
        

    os.system('pause')
    os.system('cls')