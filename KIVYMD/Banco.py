import mysql.connector

class MyBD():
    def __init__(self) -> None:
        self.banco = mysql.connector.connect(user='gleison', password='12345',
                              host='10.28.1.129', database="bd")
        
        self.cursor = self.banco.cursor()

        if self.banco.is_connected():
            database_info = self.banco.get_server_info()
            print(f"Conectado ao Banco de dados = {database_info}") 
        
        
    def list_values(self):
        valueText = "select * from menu;"
        self.cursor.execute(valueText)
        lista = self.cursor.fetchall()        
        self.banco.commit()
        
        for self.list in lista:
            pass
        
    def fechar_bd(self):
        
        self.cursor.close()
        self.banco.close()
        print("Banco Fechado")
      
