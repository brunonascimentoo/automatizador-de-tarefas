import pyautogui as pgui
import pandas as pd
import time

timer = time

left_click = pgui.leftClick #click na tela
hotkey = pgui.hotkey #clica uma combição de teclas ex: ctrl + c 
move_to = pgui.moveTo # move o mouse para local indicado
pause = pgui.PAUSE = 0.5 # pause de x segundos antes de executar algum comando
write = pgui.typewrite # escreve texto
press = pgui.press # pressiona tecla

#Inicio abre crud no navegador
press('win')
write('automatizador')
press('enter')
timer.sleep(5)
move_to(x=640, y=368)
left_click()
press('enter')
pause
move_to(x=417, y=322)
left_click()
press('enter')

#ler base de dados
table = pd.read_excel('base_de_dados/base_dados.xlsx')

timer.sleep(2)

#iterar sobre base de dados
for i, row in table.iterrows():
    move_to(x=953, y=338)
    left_click()
    pause  

    move_to(x=560, y=354)
    left_click()
    pause

    name = row[0]
    last_name = row[1]
    date_of_birth = row[2]
    education = row[3]
    
    # Escrevendo os dados
    write(name)
    press('tab')
    write(last_name)
    press('tab')
    write(date_of_birth)
    press('tab')
    write(education)
    move_to(x=1501, y=550)
    left_click()
    press('enter')
                   
