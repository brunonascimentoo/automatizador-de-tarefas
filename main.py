#abrir arquivo crud
#ler base de dados
#cadastrar itens
#repetir processo

import pyautogui as pgui
import pandas as pd
import time


timer = time

left_click = pgui.leftClick #click na tela
hotkey = pgui.hotkey #clica uma combição de teclas ex: ctrl + c 
move_to = pgui.moveTo # move o mouse para local indicado
pause = pgui.PAUSE = 0.5 # pause de x segundos antes de executar algum comando
write = pgui.write # escreve texto
press = pgui.press # pressiona tecla

#Inicio abre crud no navegador
press('win')
write('automatizador')
press('enter')
timer.sleep(5)
move_to(640, 368)
left_click(x=640, y=368)
press('enter')
left_click(x=640, y=368)
press('enter')

#ler base de dados
table = pd.read_excel('base_de_dados/base_dados.xlsx')
print(table)

timer.sleep(2)
left_click(x=963, y=359)
pause
left_click(x=510, y=357)
name = write('nome')
press('tab')
last_name = write('last_name')
press('tab')
date_of_birth = write('26/11/1996')
press('tab')
training = write('training')
move_to(x=1476, y=553)
left_click()
