#Calculator



while True:
    print ("="*10, "Calculator", "="*10)

    print ("1. Digite um numero para Multiplicador ")
    print ("2. Digite um numero para Subtração ")
    print ("3. Digite um numero para Adição ")
    print ("4. Digite um numero para Raiz Quadrado ")
    print ("5. Digite um numero para Área de um Quadrado ")
    print ("6. Digite um numero para Media de 4 numeros ")
    print ("7. Digite um numero para Fatorial ")
    print ("8. Digite um numero para Exponenciação ")
    print ("9. Digite um numero para Volume de um Cubo ")
    print ("10. Digite um numero para Divisao ")

    resu = int(input("Digite aqui o quê você quer: "))  
    if resu == 1:
        print ("="*10, "Multiplicação", "="*10)
        print ("Olá, bem vindo a Multiplicação")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c*d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Multiplicação - Fim", "="*10)
        continue
    elif resu == 2:
        print ("="*10, "Subtração", "="*10)
        print ("Olá, bem vindo a Subtração")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c-d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Subtração - Fim", "="*10)
        continue
    elif resu == 3:
        print ("="*10, "Adição", "="*10)
        print ("Olá, bem vindo a Adição")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c+d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Adição - Fim", "="*10)
        continue
    elif resu == 4:
        print ("="*10, "Raiz Quadrada", "="*10)
        print ("Olá, bem vindo a Raiz Quadrada")
        c = float(input("Digite um numero: "))
        b = c**0.05
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Raiz Quadrada - Fim", "="*10)
        continue
    elif resu == 5:
        print ("="*10, "Area de um Quadrado", "="*10)
        print ("Olá, bem vindo a Área de um Quadrado")
        c = float(input("Digite um numero: "))
        b = c*c
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Área de um Quadrado - Fim", "="*10)
        continue
    elif resu == 6:
        print ("="*10, "Aritmética", "="*10)
        print ("Olá, bem vindo a Aritmética")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        e = float(input("Digite um numero: "))
        f = float(input("Digite um numero: "))
        b = (c+d+e+f)/4
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Áritmética - Fim", "="*10)
        continue
    elif resu == 7:
        print ("="*10, "Fatorial", "="*10)
        print ("Olá, bem vindo a Fatorial")
        c = float(input("Digite um numero: "))
        result = 1
        contador = 1
        while contador <= c:

            result *= contador
            contador += 1
        print (result)
    elif resu == 8:
        print ("="*10, "Exponenciação", "="*10)
        print ("Olá, bem vindo a Exponenciação")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c**d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Exponenciação - Fim", "="*10)
        continue
    elif resu == 9:
        print ("="*10, "Volume de um Cubo", "="*10)
        print ("Olá, bem vindo a Volume de um Cubo")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c**2**1
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Volume de um Cubo - Fim", "="*10)
        continue
    elif resu == 10:
        print ("="*10, "Divisão", "="*10)
        print ("Olá, bem vindo a Divisão")
        c = float(input("Digite um numero: "))
        d = float(input("Digite um numero: "))
        b = c/d
        print ("Bom, o resultado dessa operação é: ",b)
        print ("="*10, "Fim - Divisão - Fim", "="*10)
        continue
    else: 
        break