#!/usr/bin/env python3
import RPi.GPIO as GPIO
from Pin import PIN
from Train import Train

class trains():
    def __init__(self):
        self.train_1 = Train( PIN.MOTOR_TRAIN_1_ENABLE, PIN.FORWARD_TRAIN_1_PIN, PIN.BACKWARD_TRAIN_1_PIN)

    def run(self):
        print ("Press Ctrl+C to end the program...")
        while True:
            action = input("direction?:")
            
            if(action =='f'):
                self.train_1.increase_speed()
            
            if(action =='d'):
                self.train_1.decrease_speed()

            if(action == 's'):
                self.train_1.stop()

    def destroy(self):
        self.train_1.destroy()
        # GPIO.cleanup()          

if __name__ == '__main__': 
        myTrains=trains()
        try:
            myTrains.run()
        except KeyboardInterrupt:
            myTrains.destroy()
