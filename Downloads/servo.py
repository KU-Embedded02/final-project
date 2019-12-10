import RPi.GPIO as gpio
import time
import curses
import os

adc1=0
adc2=0
class Servo():
    
    def __init__(self, servoPin):
        self.servoPin = servoPin
        gpio.setwarnings(False)
        gpio.setmode(gpio.BCM)
        gpio.setup(self.servoPin, gpio.OUT)
        
    def start(self, pwmFreq):
        self.pwmFreq = int(pwmFreq)
        self.pwm = gpio.PWM(self.servoPin, self.pwmFreq)
        self.pwm.start(50)
        
    def goto(self, angle):
        self.duty = angle/15
        self.pwm.ChangeDutyCycle(self.duty)
        time.sleep(0.05)
        
    def sweep(self,startAngle,endAngle,stepDelay): #Angles in multiples of 15 degrees
        self.sAngle = startAngle/15
        self.eAngle = endAngle/15
        self.delay = stepDelay
        for i in range(int(self.sAngle),int(self.eAngle)):
            self.pwm.ChangeDutyCycle(i)
            time.sleep(self.delay)
        for j in range(int(self.eAngle),int(self.sAngle),-1):
            self.pwm.ChangeDutyCycle(j)
            time.sleep(self.delay)

if __name__=="__main__":
    servo1 = Servo(20)
    servo1.start(60)
    servo2 = Servo(21)
    servo2.start(60)
    servo1.sweep(60, 120, 0.05)
    servo2.sweep(60, 120, 0.05)
    
