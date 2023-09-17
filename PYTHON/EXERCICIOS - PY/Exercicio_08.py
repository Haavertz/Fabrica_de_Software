
d = ""
cont = 0
loop = 2
while loop != 1:
    list = []
    nome = input("Digite seu nome de usuario(apenas 3 Caractere): ")
    idade = int(input("Digite o valor da sua idade entre (0 a 150): "))
    Salario = float(input("Digite o valor do seu salario ( > 0): "))
    Sexo = input("Sexo(F or M): ")
    Estado = input("Digite seu estado civil (c, s , v, d): ")
    list.append(nome)

    if len(list) < 3:
        if idade > 0 and idade < 150:
            if Salario > 0:
                print("!")
                if Sexo.upper == 'F' or Sexo.upper == 'M':
                    if Estado.upper == 'C' or Estado.upper == 'S' or Estado.upper == 'V' or Estado.upper == 'D':
                        print(f"Nome: {nome} \n Idade: {idade} \n Salario: {Salario} \n Sexo: {Sexo} \n Estado: {Estado}")
                    else:
                        break              
                else:
                    break
            else:
                break
        else:
            break
    else:
        break





    
    
        