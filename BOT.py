import pyautogui
import RGB
import time
import Setting as Healing

#diretorios dos arquivos a serem checados
pathFullHealth = 'picture/health.png'
pathFullMana = 'picture/mana.png'
pathHealthNow = 'Healing/health.png'
pathManaNow = 'Healing/mana.png'

#porcentagem para usar o heal
percentHigh = 95
percentMedium = 40
percentLow = 20

#Hotkey
HTK_High = 'F12'
HTK_Medium = 'F1'
HTK_Low = 'F1'
HTK_Mana = 'F5'

#Checa se o processo está aberto
while Healing.getTibiaActive():

#Captura imagem da tela para comparar
  Healing.checkImgToCapture('healthLow', 'health')
  Healing.checkImgToCapture('manaLow', 'mana')

#Coletar quantidae de pixels das imagens
  healthFull = RGB.getPixelsInImage(pathFullHealth).getPixelsHealth()
  getHealth = RGB.getPixelsInImage(pathHealthNow).getPixelsHealth() 
  manaFull = RGB.getPixelsInImage(pathFullMana).getPixelsMana()
  getMana = RGB.getPixelsInImage(pathManaNow).getPixelsMana()
  HealthPercent = Healing.percentage(percentLow, healthFull)

  if getHealth < healthFull:
    if getHealth <= Healing.percentage(percentLow, healthFull):
      pyautogui.hotkey(HTK_Low)
      print('Health Percent: ' + str(getHealth) + '%')
      #print('Low')
    elif getHealth <= Healing.percentage(percentMedium, healthFull):
      pyautogui.hotkey(HTK_Medium)
      print('Health Percent: ' + str(getHealth) + '%')
      #print('Medium')
    elif getHealth <= Healing.percentage(percentHigh, healthFull):
      pyautogui.hotkey(HTK_High)
      if getMana <= Healing.percentage(percentMedium, manaFull):
        pyautogui.hotkey(HTK_Mana)
        print('Mana Percent: ' + str(getMana)+ '%')
      print('Health Percent: ' + str(getHealth) + '%')
      #print('High')
      