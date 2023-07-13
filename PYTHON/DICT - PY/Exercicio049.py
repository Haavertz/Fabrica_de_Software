
#Faça um dicionario com as 5 pessoas mais perto de você, tendo o nome como chave e a idade como valor.

'''dicio = {"jose":12, "joao":22, "paulo" : 18, "larissa" : 17, "finn" : 13}
print (dicio)'''

'''print ('==========================================================================================================================================')'''

semana = {}
semana = {
          'segunda' : 'Ederson', 
          'terça' : 'Mauricio',
          'Quarta' : 'Ederson',
          'Quinta' : 'Mauricio',
          'Sexta' : 'Ederson',
          'Sábado' : [], 
          'domingo':[]
          }
print (semana)

'''print ('==========================================================================================================================================')'''
agenda = {}
cadastro = 1
while cadastro != 0:
    print("( 1 ) - Cadastro \n ( 0 ) - Sair/Mostrar \n")
    cadastro = int(input("Escolha: "))
    if cadastro == 1:
        nome = input("Digite o nome para cadastrar no cpf: ")
        idade = input("Digite sua idade para cadastrar no cpf: ")
        telefone = input("Digite seu telefone para cadastrar no cpf: ")
        cpf = input("Digite o numero do cpf: ")
        agenda[cpf]={
            'nome':nome, 
            'idade':idade, 
            'telefone':telefone}

print (agenda)
