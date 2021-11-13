#!/usr/bin/env python3
import RPi.GPIO as GPIO
from Pin import PIN
from Train import Train

class trains():
    def __init__(self):
        self.train_1 = Train( PIN.MOTOR_TRAIN_1_ENABLE, PIN.FORWARD_TRAIN_1_PIN, PIN.BACKWARD_TRAIN_1_PIN)
        self.train_2 = Train( PIN.MOTOR_TRAIN_2_ENABLE, PIN.FORWARD_TRAIN_2_PIN, PIN.BACKWARD_TRAIN_2_PIN)

    def run(self):
        print ("Press Ctrl+C to end the program...")
        print ("Train 1 (f) faster speed, (d) decrease speed, (s) stop. ")
        print ("Train 2 (j) faster speed, (k) decrease speed, (l) stop. ")
        while True:
            action = input("Speed ? ..")
            
            if(action =='f'):
                self.train_1.increase_speed()
            
            if(action =='d'):
                self.train_1.decrease_speed()

            if(action == 's'):
                self.train_1.stop()
                
            if(action =='j'):
                self.train_2.increase_speed()
            
            if(action =='k'):
                self.train_2.decrease_speed()

            if(action == 'l'):
                self.train_2.stop()                

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
