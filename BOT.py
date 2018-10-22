import pyautogui
import RGB
import time
import Setting as Healing

#diretorios dos arquivos a serem checados
pathFullHealth = 'picture\\health.png'
pathHealthNow = 'Healing\\health.png'
pathFullMana = 'picture\\mana.png'
pathManaNow = 'Healing\\mana.png'

#porcentagem para usar o heal
percentHigh = 95
percentMedium = 70
percentLow = 50

#Hotkey
HTK_High = 'F10'
HTK_Medium = 'F11'
HTK_Low = 'F12'

#Checa se o processo está aberto
while Healing.getTibiaActive():

#Captura imagem da tela para comparar
  Healing.checkImgToCapture('health', 'health')
  Healing.checkImgToCapture('mana', 'mana')

#Coletar quantidae de pixels das imagens
  healthFull = RGB.getPixelsInImage(pathFullHealth).getPixelsHealth()
  getHealth = RGB.getPixelsInImage(pathHealthNow).getPixelsHealth() 
  manaFull = RGB.getPixelsInImage(pathFullMana).getPixelsMana()
  getMana = RGB.getPixelsInImage(pathManaNow).getPixelsMana()

  if getHealth <= Healing.percentage(percentLow, healthFull):
    pyautogui.hotkey(HTK_Low)
    #print('Low')
  elif getHealth <= Healing.percentage(percentMedium, healthFull):
    pyautogui.hotkey(HTK_Medium)
    #print('Medium')
  elif getHealth <= Healing.percentage(percentHigh, healthFull):
    pyautogui.hotkey(HTK_High)
    #print('High')