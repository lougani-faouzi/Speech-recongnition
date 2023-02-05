import gc
import m5stickc_lcd
import speech_model
from machine import I2S, PWM, Pin, reset
from time import sleep

vibrator = Pin(25, Pin.OUT)
  
# Use the M5StickC built-in microphone.
mic = I2S(I2S.NUM0, ws=Pin(0), sdin=Pin(34), mode=I2S.MASTER_PDW,
    dataformat=I2S.B16, channelformat=I2S.ONLY_RIGHT,
    samplerate=16000, dmacount=16, dmalen=256)
lcd = m5stickc_lcd.ST7735()
# M5StickC is capable of running one model inference every 224ms.
# 7168 / (16000 * 2) = 0.224
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
    if label == 'LILI': # Replace with your own label.
        vibrator.value(1)
        sleep(0.5)
    vibrator.value(0)    
    lcd.fill(0)
    lcd.text(label, 10, 30, 0xffff)
    lcd.text(str(prob), 10, 50, 0xffff)
    lcd.show()

mic.deinit()
