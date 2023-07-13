class BaseDeDados():
    def __init__(self):
        self.dados = {}

        pass
    def inserirCliente(self, id, nome):
        if "clientes" not in self.dados:
            self.dados["Clientes"] = {id:nome}
        else:
            self.dados["Clientes"].update({id:nome})
    
    def listar_dados(self):
        for nome,id in self.dados["Clientes"].items():
            print(nome,id)

    def apagarclinete(self):
        del self.dados["Clientes"][id]