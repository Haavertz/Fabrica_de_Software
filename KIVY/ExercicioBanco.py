import mysql.connector

class ExercicioBanco:
    def __init__(self):
        self.banco1 = mysql.connector.connect(
            user='gleison', password='12345',
            host='10.28.1.129', database="kivyaplication"
        )
        if self.banco1.is_connected():
            database_info = self.banco1.get_server_info()
            print(f"Conectado ao Banco de Dados = {database_info}")
            
        self.cursor = self.banco1.cursor()

    def insert_values(self, nome, cpf, senha, gmail):
        today = "insert into cadastro (nome, cpf, senha, gmail) values (%s, %s, %s, %s)"
        values = (nome, cpf, senha, gmail)

        self.cursor.execute(today, values)
        self.banco1.commit()
        print(self.cursor.rowcount, "registro(s) inserido(s).")

    def select_values(self):
        select = "select * from cadastro;"
        self.cursor.execute(select)
        
        resultados = self.cursor.fetchall()
        for resultado in resultados:
            print(resultado)
            
    def exclude_values(self, id):
        delete_query = "delete from cadastro where id_cadastro = %s;"
        delete_data = (id,)

        self.cursor.execute(delete_query, delete_data)
        self.banco1.commit()

    def fechar_conexao(self):
        if self.banco1.is_connected():
            self.banco1.close()
            print("Conexão encerrada")
            print("-=" * 20)



