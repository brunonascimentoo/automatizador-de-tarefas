#Usar código auxiliar para saber posição da tela
import time
import pyautogui as pgui

time_wait = time
time_wait.sleep(3)

screen_position = pgui.position #saber posição da tela
print(screen_position())