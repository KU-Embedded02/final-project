import curses
import os
import RPi.GPIO as GPIO

pwm=''
adc=0
servoPin = 20

def init():
    global pwm
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin, GPIO.OUT)
    pwm = GPIO.PWM(servoPin, 100)
    pwm.start(0)
    
def moveServo(adc):
    global pwm
    print(float(adc)/10.0+2.5)
    pwm.ChangeDutyCycle(float(adc)/10.0+2.5)
    
def main(win):
    global adc
    init()
    win.nodelay(True)
    key=""
    while 1:          
        try:                 
            key = win.getkey()  
            if str(key) == 'KEY_UP':
                if adc!=180:
                    adc=adc+10
                    moveServo(adc1)
            if str(key) == "KEY_DOWN":
                if adc!=0:
                    adc=adc-10
                    moveServo(adc)
            if key == os.linesep:
                break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)