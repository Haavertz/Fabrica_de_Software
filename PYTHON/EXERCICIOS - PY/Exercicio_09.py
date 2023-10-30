class Organizar_Tabuleiro:
    def __init__(self):
        self.Initial(0)

    def Initial(self, line="|_|"):
        if line == "|_|":
            return None
        else:
            for i in range(0, 9):
                for j in range(0, 9):
                    if i == 0 and j == 0:
                        print(" +", "-" * 25, "+")
                    print("", line, end=" ")

                    if j == 8:
                        print("", i, end="")
                        print(end="\n")

                    if i == 8 and j == 8:
                        alfabeto = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
                        for describe in alfabeto:
                            print("", describe, end=" ")

                        print("\n", "+", "-" * 25, "+", end="")
                        print("\n")


                 


Organizar_Tabuleiro()
