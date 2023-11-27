import mysql.connector

class BancoDS():
    def __init__(self) -> None:
        try:
            self.banco = mysql.connector.connect(
                user='gleison', password='12345',
                host='10.28.1.129', database="tentativa_banco"
            )
            self.cursor = self.banco.cursor()
        except mysql.connector.Error as err:
            print(f"Erro de conexão: {err}")

    def list_values(self):
        try:
            valueText = "select * from cadastro;"
            self.cursor.execute(valueText)
            lista = self.cursor.fetchall()
            for self.result in lista:
                pass
        except mysql.connector.Error as err:
            print(f"Erro ao executar a consulta: {err}")
        finally:
            self.fechar_bd()

    def fechar_bd(self):
        try:
            self.cursor.close()
            self.banco.close()
        except Exception as e:
            print(f"Erro ao fechar o banco: {e}")

# Exemplo de uso
if __name__ == "__main__":
    banco = BancoDS()
    banco.list_values()
