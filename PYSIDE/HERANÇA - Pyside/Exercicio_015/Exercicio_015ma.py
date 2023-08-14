


class soma():
    total = []
    def __init__(self, number1, number2, cont):
        total = number1, number2
        for i in range(cont):
            if i != 0:
                print("=-"*20)
            for j in range(i):
                total = number1 * number2
                print(f"{total}")
                
                
c1 = soma(22,30,2)
c2 = soma(10,10,2)
