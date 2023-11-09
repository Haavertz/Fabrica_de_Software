import mysql.connector

class ConectandoBanco():
    def __init__(self) -> None:
        
        self.banco1 = mysql.connector.connect(user='gleison', password='12345',
                                    host='10.28.1.129', database="kivyaplication")

        if self.banco1.is_connected():
            database_info = self.banco1.get_server_info()
            print(f"Conectado ao Banco de dados = {database_info}")

        consulta_mysql = "select * from cadastro"
        self.cursor = self.banco1.cursor()
        self.cursor.execute(consulta_mysql)
        resultados_inuteis = self.cursor.fetchall()

        print(f"Numero total de registros retornados: {self.cursor.rowcount}")

    def insert_values(self, nome, cpf, senha, gmail):
        self.today = "INSERT INTO cadastro (nome, cpf, senha, gmail) VALUES (%s, %s, %s, %s)"
        self.values = (nome, cpf, senha, gmail)
    
        self.cursor.close()
        self.cursor = self.banco1.cursor()
        self.cursor.execute(self.today, self.values)
        self.banco1.commit()
        print(self.cursor.rowcount, "registro(s) inserido(s).")
        
    def exclude_values(self):
        pass

    def fechar_conexao(self):
        if self.banco1.is_connected():
            self.banco1.close()
            print("Conexão encerrada")
            print("-="*20)



