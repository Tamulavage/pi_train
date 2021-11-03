#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

MotorPin1   = 17
MotorPin2   = 27
MotorEnable = 18

def setup():
        global forward
        global backward
        GPIO.setmode(GPIO.BCM)          # Numbers GPIOs by BCM
        GPIO.setup(MotorPin1, GPIO.OUT)   # mode --- output
        GPIO.setup(MotorPin2, GPIO.OUT)
        GPIO.setup(MotorEnable, GPIO.OUT)
        
        forward=GPIO.PWM(MotorPin1,500)
        backward=GPIO.PWM(MotorPin2,500)
        forward.start(0)
        backward.start(0)

        GPIO.output(MotorEnable, GPIO.LOW) # motor stop

def loop():
        print ("Press Ctrl+C to end the program...")
        print ("(f) forward (b) back")
        duty = 50
        
        lastDirection = 'x'
        while True:
            direction = input("direction?:")
            
            if(direction =='f'):
                print('forward')
                if(lastDirection == 'f'):
                    front(100)
                elif(lastDirection == 'b'):
                    front(0)
                else:
                    front(50)
            
            elif(direction == 'b'):
                print('back')
                if(lastDirection == 'b'):
                    back(100)
                elif(lastDirection == 'f'):
                    back(0)
                else:
                    back(50)
                
            else:
                print("Unknown command...")
                GPIO.output(MotorEnable, GPIO.LOW) # motor stop
                
            lastDirection = direction

def destroy():
        forward.stop()
        backward.stop()
        
        GPIO.output(MotorEnable, GPIO.LOW) # motor stop
        GPIO.cleanup()                     # Release resource
        
def front(duty):
        GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
        print(duty)
        forward.ChangeDutyCycle(duty)
        backward.ChangeDutyCycle(0)
        
def back(duty):
        GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
        print(duty)
        forward.ChangeDutyCycle(0)
        backward.ChangeDutyCycle(duty)
        
if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

