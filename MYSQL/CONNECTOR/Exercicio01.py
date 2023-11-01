import mysql.connector

banco = mysql.connector.connect(user='gleison', password='12345',
                              host='10.28.1.129', database="hub")


if banco.is_connected():
    database_info = banco.get_server_info()
    print(f"Conectado ao Banco de dados = {database_info}")
    
consulta_mysql = "select * from palestra"
cursor = banco.cursor()
cursor.execute(consulta_mysql)
linhas = cursor.fetchall()

print(f"Numero total de registros retornados: {cursor.rowcount}")

    
#COMANDOS DO MYSQL    
    
# comando = "insert into palestra(sala, nome_palestrante, nome_palestra, descricao_palestra, quantidade_vaga) value ('310','Rogerin Engenheiro','Engenharia de Software','Palestra Engenharia de Software no mercado atual',10);"
# comando = "update palestra set quantidade_vaga = 8 where sala = '308';"
# comando = "delete from palestra where sala = '309';"
# cursor.execute(comando)
# banco.commit()

for linha in linhas:
    
    print("-="*20)
    print(f"Id Sala = {linha[0]}")
    print(f"Nome Autor = {linha[1]}")
    print(f"Nome Paletra = {linha[2]}")
    print(f"Descrição Palestra = {linha[3]}")
    print(f"Quantidade = {linha[4]}")
    
if banco.is_connected():
    # cursor.close()
    banco.close()
    print("Conexão encerrada")
    print("-="*20)