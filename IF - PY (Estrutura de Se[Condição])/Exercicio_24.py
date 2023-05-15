sexo = input("Digite o Genero(M - F): ")
sexo = sexo.upper() #Transformar a letra em maiscula com o upper e depois passar pra condição

if sexo=="M":
    print("Masculino")
elif sexo=="F":
    print ("Feminino")
else:
    print ("Não binario // transformers!")