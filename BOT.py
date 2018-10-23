import pyautogui
import RGB
import time
import Setting as Healing

#Write what version of Tibia ayou will use
Version = 'OT' # OT or RL

def autoHeal():

  if getHealth < healthFull:
    if getHealth <= Healing.percentage(percentLow, healthFull):
      pyautogui.hotkey(HTK_Low)
      #print('Low')
    elif getHealth <= Healing.percentage(percentMedium, healthFull):
      pyautogui.hotkey(HTK_Medium)
      #print('Medium')
    elif getHealth <= Healing.percentage(percentHigh, healthFull):
      pyautogui.hotkey(HTK_High)

def autoAttack():

  mousePos = pyautogui.position()
  blackAttack = pyautogui.locateCenterOnScreen('Cavebot/Auto Attack/blackTarget.png')
  redAttack = pyautogui.locateCenterOnScreen('Cavebot/Auto Attack/redTarget.png')
  
  if redAttack == None and blackAttack == None:
    return None
  elif redAttack == None and blackAttack != None:
    pyautogui.click(blackAttack[0], blackAttack[1])
    pyautogui.moveTo(mousePos[0], mousePos[1])


#diretorios dos arquivos a serem checados
pathFullHealth = 'picture/'+ Version +'/health.png'
pathFullMana = 'picture/'+ Version +'/mana.png'
pathHealthNow = 'Healing/'+ Version +'/health.png'
pathManaNow = 'Healing/'+ Version +'/mana.png'

#Hotkey
HTK_High = 'F12'
HTK_Medium = 'F11'
HTK_Low = 'F11'
HTK_Mana = 'F5'

#porcentagem para usar o heal
percentHigh = 95
percentMedium = 40
percentLow = 20

while Healing.getTibiaActive():

#Captura imagem da tela para comparar
  Healing.checkImgToCapture('healthLow', 'health', Version)
  Healing.checkImgToCapture('manaLow', 'mana', Version)
#Coletar quantidae de pixels das imagens
  healthFull = RGB.getPixelsInImage(pathFullHealth).getPixelsHealth()
  getHealth = RGB.getPixelsInImage(pathHealthNow).getPixelsHealth() 
  manaFull = RGB.getPixelsInImage(pathFullMana).getPixelsMana()
  getMana = RGB.getPixelsInImage(pathManaNow).getPixelsMana()
  HealthPercent = Healing.percentage(percentLow, healthFull)

  autoHeal()
  #autoAttack()














'''  a=pyautogui.size()
  print(a)
  print(a[0]/2.3,a[1]/3.5)
  pyautogui.moveTo(a[0]/2.3,a[1]/3.5)'''