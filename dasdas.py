import enum 
# criando enumerações usando classe
class Animal(enum.Enum):
    cachorro = 1
    gato = 2
    leao= 3
 
# Comparação usando"is"
if Animal.cachorro is Animal.gato:
    print("Cão e gato são os mesmos animais")
else:
    print("Cão e gato são animais diferentes")
 
# Comparação usando "!="
if Animal.leao != Animal.gato:
    print("Leões e gatos são diferentes")
else:
    print("Leões e gatos são iguais")
