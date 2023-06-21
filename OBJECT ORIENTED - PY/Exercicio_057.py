import os
def convertionHora (hora,minutos):
        if hora <= 12 and hora>=0:
             print(hora,":",minutos,"AM")
        elif hora > 12 and hora <=23:
             print(hora-12,":",minutos,"PM")
        else:
             print("Valor Inválido")
while True:
    try:
        hora = int(input("Digite as horas: "))
        minutos = int(input("DIgite os minutos: "))
    except:
        print("Valor Inválido")
    else:
        convertionHora(hora,minutos)