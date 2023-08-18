class fatorial ():
    
    def __init__(self):  
        bah = 5
        a = self.inicio(bah)
        print (f"O fatorial de {bah} é igual a {a}")
    
    def inicio(self, a):    
        if a == 1:
            return 1
        else:
            return a * self.inicio(a - 1)
        
fatorial()

