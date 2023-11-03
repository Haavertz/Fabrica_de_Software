import time


alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","1","2","3","4","5","6","7","8","9"]

while True:
    res = ""
    palavra = input("Digite a letra que deseja($$ == Break): ") 

    if palavra != "$$":
        for relou in palavra:
            for caracter in alfabeto:
                print(f"{res}{caracter}")
                time.sleep(0.03)
                if relou.upper() == caracter.upper():
                    res += caracter
                    break
    else:
        break