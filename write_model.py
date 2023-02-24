# pour l'usage de ce code se referer au ReadMe de ce projet 
import gc
import m5stickc_lcd
import speech_model
from machine import I2S, PWM, Pin, reset
from time import sleep

#LE PIN ASSOCIE AU VIBREUR POUR BRANCHEMENT M5STICK C PLUS
vibrator = Pin(25, Pin.OUT)
  
# Utilisation du protocole I2S du m5stick c plus 
mic = I2S(I2S.NUM0, ws=Pin(0), sdin=Pin(34), mode=I2S.MASTER_PDW,
    dataformat=I2S.B16, channelformat=I2S.ONLY_RIGHT,
    samplerate=16000, dmacount=16, dmalen=256)
lcd = m5stickc_lcd.ST7735()
# initialisation frequence
buffer = bytearray(7168)
label = ''
label_index = -1

def select_label(pin):
    global label_index
    label_index = (label_index + 1) % len(speech_model.labels)
    lcd.fill(0)
    lcd.text(speech_model.labels[label_index], 10, 30, 0xffff)
    lcd.show() 

Pin(39, Pin.IN).irq(handler=select_label, trigger=Pin.IRQ_FALLING)
gc.collect()

while True:
    mic.readinto(buffer)
    l, prob = speech_model.predict(buffer)
    gc.collect()
    if l == '[OTHER]' or prob <= 70:
        continue
    label = l
    speech_model.snapshot()
    if label == 'LILI': # SI ON DETECTE L ETIQUETTE LILI donc on active le vibreur 
        vibrator.value(1)
        sleep(0.5) # On fait un sleep de 0.5 secondes 
    #if label == '[OTHER]'
    #vibrator.value(1)
    vibrator.value(0)    
    lcd.fill(0) # tester si la reconnaissance est ok sans le vibreur mais en affichant sur l ecran
    lcd.text(label, 10, 30, 0xffff)
    lcd.text(str(prob), 10, 50, 0xffff)
    lcd.show()

mic.deinit()
