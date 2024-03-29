import RPi.GPIO as GPIO
import time

SPICLK = 11
SPIMISO = 9
SPIMOSI = 10
SPICS = 8
servoPin = 21

photo_ch = 0
agc=0
pwm=0

def init():
    global pwm
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(SPIMOSI, GPIO.OUT)
    GPIO.setup(SPIMISO, GPIO.IN)
    GPIO.setup(SPICLK, GPIO.OUT)
    GPIO.setup(SPICS, GPIO.OUT)
    GPIO.setup(servoPin, GPIO.OUT)
    pwm = GPIO.PWM(servoPin, 100)
    pwm.start(2.0)

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)	
    GPIO.output(clockpin, False)  
    GPIO.output(cspin, False)     
    commandout = adcnum
    commandout |= 0x18  
    commandout <<= 3    
    for i in range(5):
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
    
    adcout = 0
    for i in range(12):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        
        if (GPIO.input(misopin)):
            adcout |= 0x1
            
    GPIO.output(cspin, True)
    adcout >>= 1
    return adcout

def moveServo(adcout):
    global pwm
    global agc
    print(20.46-adcout/50.0)
    pwm.ChangeDutyCycle(20.46-adcout/50.0)
    
if __name__=="__main__":
    try:
        init()
        while True:
            acd = readadc(photo_ch, SPICLK, SPIMOSI, SPIMISO, SPICS)
            moveServo(acd)
            time.sleep(0.1)
    except KeyboardInterrupt:
        pwm.stop()
        GPIO.cleanup()
            