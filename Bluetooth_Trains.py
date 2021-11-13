#!/usr/bin/env python3
import RPi.GPIO as GPIO
from bluedot import BlueDot
from Pin import PIN
from Train import Train

class trains():
    def __init__(self):
        self.train_1 = Train( PIN.MOTOR_TRAIN_1_ENABLE, PIN.FORWARD_TRAIN_1_PIN, PIN.BACKWARD_TRAIN_1_PIN)
        self.train_2 = Train( PIN.MOTOR_TRAIN_2_ENABLE, PIN.FORWARD_TRAIN_2_PIN, PIN.BACKWARD_TRAIN_2_PIN)
    
    def run(self):
        print ("Press Ctrl+C to end the program...")
        
        bd=BlueDot(cols=3, rows=3)
        bd.square = True
        bd[1,0].visible = False
        bd[1,1].visible = False
        bd[1,2].visible = False
        bd[0,1].color = "red"
        bd[2,1].color = "red"
        
        while True:
            bd[0,0].when_pressed = self.train_1.increase_speed
            bd[0,1].when_pressed = self.train_1.stop
            bd[0,2].when_pressed = self.train_1.decrease_speed
            
            bd[2,0].when_pressed = self.train_2.increase_speed
            bd[2,1].when_pressed = self.train_2.stop
            bd[2,2].when_pressed = self.train_2.decrease_speed
            
    def destroy(self):
        self.train_1.destroy()
        self.train_2.destroy()
        GPIO.cleanup()          

if __name__ == '__main__': 
    myTrains=trains()
    try:
        myTrains.run()
    except KeyboardInterrupt:
        myTrains.destroy()

