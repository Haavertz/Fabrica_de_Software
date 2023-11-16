import mysql.connector

class MyBD():
    def __init__(self) -> None:
        self.banco = mysql.connector.connect(user='gleison', password='12345',
                              host='10.28.1.129', database="menucadastro")
        
        self.cursor = self.banco.cursor()

        if self.banco.is_connected():
            database_info = self.banco.get_server_info()
            print(f"Conectado ao Banco de dados = {database_info}")
            
    def insert_values(self, nome, sobrenome, cpf, email, telefone, endereco, data_nascimento, complemento, cep, senha):
        valueText = f"insert into cadastro (nome, sobrenome, cpf, email, telefone, endereco, data_nascimento, complemento, cep, senha) values ('{nome}','{sobrenome}','{cpf}','{email}','{telefone}','{endereco}','{data_nascimento}','{complemento}','{cep}','{senha}');"
        self.cursor.execute(valueText)        
        self.banco.commit()
     
        
    def select_values(self, user_id):
        select = f"select * from cadastro where id = {user_id};"
        self.cursor.execute(select)
        resultados = self.cursor.fetchall()
        for self.resultado in resultados:
            print(self.resultado)
        
    def list_values(self):
        valueText = "select * from cadastro;"
        self.cursor.execute(valueText)
        lista = self.cursor.fetchall()        
        self.banco.commit()
        
        for list in lista:
            pass
        
        print(f"Numero total de registros retornados: {self.cursor.rowcount}")
        
    def exclude_values(self, id):
        valueText = f"delete from cadastro where id = {id};"
        self.cursor.execute(valueText)
        self.banco.commit()
        print("ID EXCLUIDO")

    def fechar_bd(self):
        
        self.cursor.close()
        self.banco.close()
        print("Banco Fechado")
      
# insert_values("Ronaldo","Fenomeno","987654322","ronaldinho@gmail.com","67981827644", "Rua do Ronaldo", "19/02/2003","1012","79097021","321")      
# MyBD().list_values()

