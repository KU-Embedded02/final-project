import curses
import os
import RPi.GPIO as GPIO

pwm1=''
adc1=0
servoPin1 = 21
pwm2=''
adc2=180
servoPin2 = 18

def init():
    global pwm1
    global pwm2
    GPIO.setwarnings(False)
    GPIO.cleanup()
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(servoPin1, GPIO.OUT)
    GPIO.setup(servoPin2, GPIO.OUT)
    pwm1 = GPIO.PWM(servoPin2, 100)
    pwm2 = GPIO.PWM(servoPin2, 100)
    pwm1.start(0)         #모터 위치를 0(끝)으로 초기화
    pwm2.start(20.5)     #모터 위치를 pwm1과 반대쪽 끝으로 초기화
    
def moveServo(adc1, adc2):
    global pwm1
    global pwm2
    print(float(adc1)/10.0+2.5, float(adc2)/10.0+2.5)) #바꿔줄 dutycycle 출력
    pwm1.ChangeDutyCycle(float(adc1)/10.0+2.5)  #모터 이동
    pwm2.ChangeDutyCycle(float(adc2)/10.0+2.5)  #모터 이동
    
def main(win):
    global adc1
    global adc2
    init()
    win.nodelay(True)
    key=""
    while 1:          
        try:                 
            key = win.getkey()  
            if str(key) == 'KEY_UP':  # 위 방향키를 누르면
                if adc1!=180:   # 모터가 끝에 위치하지 않았으면
                    adc1=adc1+10   
                    adc2=adc2-10
                    moveServo(adc1, adc2)  #모터 이동
            if str(key) == "KEY_DOWN":  # 아래 방향키를 누르면
                if adc1!=0:  # 모터가 아래 끝에 위치하지 않았으면
                    adc1=adc1-10
                    adc2=adc2+10
                    moveServo(adc1, adc2) # 모터 이동
        except Exception as e:
           # No input   
           pass         

curses.wrapper(main)
