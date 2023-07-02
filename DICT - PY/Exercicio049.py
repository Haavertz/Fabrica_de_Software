
#Faça um dicionario com as 5 pessoas mais perto de você, tendo o nome como chave e a idade como valor.

'''dicio = {"jose":12, "joao":22, "paulo" : 18, "larissa" : 17, "finn" : 13}
print (dicio)'''

'''print ('==========================================================================================================================================')'''

'''semana = {}
semana = {'domingo':[],'segunda' : 'Ederson', 'terça' : 'Mauricio','Quarta' : 'Ederson','Quinta' : 'Mauricio','Sexta' : 'Ederson','Sábado' : []}
print (semana)'''

'''print ('==========================================================================================================================================')'''
agenda = {}
while True:
    cadastro = int(input("dada:"))
    if cadastro == 1:
        nome = input("Digite o nome para cadastrar no cpf: ")
        idade = input("Digite sua idade para cadastrar no cpf: ")
        telefone = input("Digite seu telefone para cadastrar no cpf: ")
        cpf = input("Digite seu telefone para cadastrar no cpf: ")
        agenda[cpf]={'nome':nome, 'idade':idade, 'telefone':telefone}
    elif cadastro == 0:
        break
print (agenda)