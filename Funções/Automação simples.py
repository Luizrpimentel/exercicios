" Automação simples que fiz para abrir o WPP WEB e mandar mensagens repetidas para a primeira conversa"

import pyautogui as pg
import webbrowser as wb
import time

def automocao():
    wb.open('https://web.whatsapp.com/')
    time.sleep(10)
    pg.click(140, 247) # ponto da 1 conversa
    time.sleep(3)
    pg.click(607, 700) # ponto da 1 conversa

    for enviar in range(500):
        pg.write('OI MUANOITE')
        pg.press('enter')

    return enviar

print(automocao())
