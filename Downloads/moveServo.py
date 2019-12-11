import curses
import os
import RPi.GPIO as GPIO

pwm1=''
adc1=180
servoPin1 = 6
pwm2=''
adc2=0
servoPin2 = 26
pwm3=''
adc3=180
servoPin3 = 13
pwm4=''
adc4=0
servoPin4 = 19

pwm5 = ''
adc5 = 90
servoPin5 = 5

def init():
    global pwm1
    global pwm2
    global pwm3
    global pwm4
    global pwm5
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin1, GPIO.OUT)
    GPIO.setup(servoPin2, GPIO.OUT)
    GPIO.setup(servoPin3, GPIO.OUT)
    GPIO.setup(servoPin4, GPIO.OUT)
    GPIO.setup(servoPin5, GPIO.OUT)
    pwm1 = GPIO.PWM(servoPin1, 100)
    pwm2 = GPIO.PWM(servoPin2, 100)
    pwm3 = GPIO.PWM(servoPin3, 100)
    pwm4 = GPIO.PWM(servoPin4, 100)
    pwm5= GPIO.PWM(servoPin5, 100)
    pwm1.start(20.5)
    pwm2.start(2.5)
    pwm3.start(20.5)
    pwm4.start(2.5)
    pwm5.start(11.5)
    
def moveServoUD(adc1, adc2):
    global pwm1
    global pwm2
    print(float(adc1)/10.0+2.5, float(adc2)/10.0+2.5)
    pwm1.ChangeDutyCycle(float(adc1)/10.0+2.5)
    pwm2.ChangeDutyCycle(float(adc2)/10.0+2.5)

def moveServoLR(adc3, adc4):
    global pwm3
    global pwm4
    print(float(adc3)/10.0+2.5, float(adc4)/10.0+2.5)
    pwm3.ChangeDutyCycle(float(adc3)/10.0+2.5)
    pwm4.ChangeDutyCycle(float(adc4)/10.0+2.5)
    
def moveServoFB(adc5):
    global pwm5
    print(float(adc5)/10.0+2.5)
    pwm5.ChangeDutyCycle(float(adc5)/10.0+2.5)
    
def main(win):
    global adc1
    global adc2
    global adc3
    global adc4
    global adc5
    init()
    win.nodelay(True)
    key=""
    while 1:          
        try:                 
            key = win.getkey()
            if str(key) == 'KEY_UP':
                if adc1!=0:
                    adc1=adc1-5
                    adc2 = adc2+5
                    moveServoUD(adc1, adc2)
            if str(key) == "KEY_DOWN":
                if adc1!=180:
                    adc1=adc1+5
                    adc2=adc2-5
                    moveServoUD(adc1,adc2)
            if str(key) == 'KEY_LEFT':
                if adc3!=180:
                    adc3=adc3+5
                    adc4 = adc4-5
                    moveServoLR(adc3, adc4)
            if str(key) == 'KEY_RIGHT':
                if adc3!=0:
                    adc3=adc3-5
                    adc4 = adc4+5
                    moveServoLR(adc3, adc4)
            if key == 'w':
                if adc5 <180:
                    adc5 = adc5 + 5
                    moveServoFB(adc5)
            if key == 's':
                if adc5 >0:
                    adc5 = adc5 -5
                    moveServoFB(adc5)
            if key == os.linesep:
                break           
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)
