import pyautogui as py 
import random
import time 

time.sleep(5)

mensage = ["Bom Dia", "Boa Tarde", "Boa Noite"]

for i in range(10):
    msg = random.choice(mensage)
    py.write(msg)
    py.press("enter")