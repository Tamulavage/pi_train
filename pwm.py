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
        
        while True:
            direction = input("direction?:")
            
            if(direction =='f'):
                go_forward()
            
            elif(direction == 'b'):
                go_backward()

            else:
                print("Unknown command...")
                GPIO.output(MotorEnable, GPIO.LOW) # motor stop
     

def faster(duty):
    duty=duty+10
    if(duty<100):
        return duty
    else:
        return 100

def slower(duty):
    duty=duty-10
    if(duty>0):
        return duty
    else:
        return 0

def slow_stop(duty, dir):
    while duty!=0:
        duty = slower(duty)
        time.sleep(.1)
        if(dir=='f'):
            front(duty)
        elif(dir=='b'):
            back(duty)

def go_forward():
    print('forward')
    duty = 30
    while True:
        speed = input(" (i) increase or (d) to decrease speed (any) key to switch directions")

        if(speed=='i'):
            duty = faster(duty)
        elif(speed == 'd'):
            duty = slower(duty)
        else:
            print('Unknown speed request - full STOP- ready to switch')
            slow_stop(duty, 'f')
            break
        
        front(duty)

def go_backward():

    print('backward')
    duty = 30
    
    while True:
        speed = input(" (i) increase or (d) to decrease speed (any) key to switch directions")

        if(speed=='i'):
            duty = faster(duty)
        elif(speed == 'd'):
            duty = slower(duty)
        else:
            print('Unknown speed request - full STOP - ready to switch')
            slow_stop(duty, 'b')
            break
        
        back(duty)
            
    
def destroy():
        forward.stop()
        backward.stop()
        
        GPIO.output(MotorEnable, GPIO.LOW) # motor stop
        GPIO.cleanup()                     # Release resource
        
def front(duty):
        print('forward  % ' + duty )
        GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
        forward.ChangeDutyCycle(duty)
        backward.ChangeDutyCycle(0)
        
def back(duty):
        print('back  % ' + duty )
        GPIO.output(MotorEnable, GPIO.HIGH) # motor driver enable
        forward.ChangeDutyCycle(0)
        backward.ChangeDutyCycle(duty)
        
if __name__ == '__main__':     # Program start from here
        setup()
        try:
                loop()
        except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
                destroy()

