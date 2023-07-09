
def valorPagamento(x,y):
    juros=(0.1*y)/100
    multa=(x*0.03)
    jurostotal=((x*juros)+multa)+x
    return jurostotal

prestações=[]
diasAtraso=[]
valorFinal=[]

while True:
    try:
        print("0. Sair/Mostrar")
        a=float(input("Digite o valor a ser pago pela prestação: "))
        b=int(input("Digite o número de dias de atraso: "))
    except ValueError:
        print("Erro! Digite somente números inteiros para os dias, e demais números para o valor da prestação.")
    except:
        print("Erro desconhecido.")
    else:
        if a==0:
            break
        elif a>0 and b>=0:
            prestações.append(a)
            diasAtraso.append(b)
            c=valorPagamento(a,b)
            valorFinal.append(c)
            continue
        else:
            print("Valor não adicionado por conter números negativos. Por favor, tente novamente.")
print("------------------------------- Relatório do Dia -------------------------------\nValores das Prestações em Ordem:")
for i in prestações:
    print("{:.2f}R$".format(i))
print("\nDias de Atraso em Ordem:")
for i in diasAtraso:
    print(i)
print("\nValores finais a serem pagados:")
for i in valorFinal:
    print("{:.2f}R$".format(i))
valorFinalTotal=sum(valorFinal)
print("Valor total somado: {:.2f}".format(valorFinalTotal))

#Programa que lê e faz calculo de juros e multa de diversos valores.