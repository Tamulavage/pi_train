#!/usr/bin/env python3
import RPi.GPIO as GPIO
import time

class Train:
    def __init__(self, enable_pin, forward_pin, backward_pin):
        self.enable_pin = enable_pin
        self.forward_pin = forward_pin
        self.backward_pin = backward_pin
        self.duty = None

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.enable_pin, GPIO.OUT)
        GPIO.setup(self.forward_pin, GPIO.OUT)
        GPIO.setup(self.backward_pin, GPIO.OUT)

        self.forward = GPIO.PWM(self.forward_pin, 500)
        self.backward = GPIO.PWM(self.backward_pin, 500)
        self.forward.start(0)
        self.backward.start(0)

        GPIO.output(self.enable_pin, GPIO.LOW)

    def new_speed(self, duty):
        if(duty >= 0):
            self.forward.ChangeDutyCycle(duty)
            self.backward.ChangeDutyCycle(0)
        elif(duty < 0):
            self.forward.ChangeDutyCycle(0)
            self.backward.ChangeDutyCycle(abs(duty))

    def increase_speed(self):
        if(self.duty < 100):
            self.duty = self.duty + 10
        else:
            self.duty = 100
        self.new_speed(self.duty)

    def decrease_speed(self):
        if(self.duty > -100):
            self.duty = self.duty - 10
        else:
            self.duty = -100
        self.new_speed(self.duty)

    def stop(self):
        while self.duty!=0:
            if(self.duty>0):
                self.decrease_speed()
                time.sleep(.1)
            elif(self.duty<0):
                self.increase_speed()
                time.sleep(.1)
            else:
                break

    def destroy(self):
        self.stop()
        
        self.forward.stop()
        self.backward.stop()
        
        GPIO.output(self.enable_pin, GPIO.LOW) 
