#!/usr/bin/env python
# -*- coding: utf8 -*-
#
#    Copyright 2014,2018 Mario Gomez <mario.gomez@teubi.co>
#
#    This file is part of MFRC522-Python
#    MFRC522-Python is a simple Python implementation for
#    the MFRC522 NFC Card Reader for the Raspberry Pi.
#
#    MFRC522-Python is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    MFRC522-Python is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with MFRC522-Python.  If not, see <http://www.gnu.org/licenses/>.
#
import os
# os.chdir("/home/pi/rfid/MFRC522/")
import RPi.GPIO as GPIO
import MFRC522_edit_1
import MFRC522_edit_2
import signal
import argparse
import json
from sevenSeg import SevenSegment
import subprocess
import time


def getTeam(uid_dict, uid):
    return uid_dict[uid]

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("-a", "--add", action="store_true", help= "adds uids to txt file.")
    parser.add_argument("-r", "--remove", action="store_true", help="remove uids from txt file.")
    parser.add_argument("-s", "--start_game", action="store_true", help="start a game.")

    args = parser.parse_args()

    Score = 0
    R = 0
    B = 0
    continue_reading = True

    uid_file = open("/home/pi/rfid/MFRC522/uid_dict", "r")
    uid_dict = json.load(uid_file)
    uid_file.close()

    # Create an object of the class MFRC522
    MIFAREReader1 = MFRC522_edit_1.MFRC522()
    MIFAREReader2 = MFRC522_edit_2.MFRC522()

    display = SevenSegment.SevenSegment()
    display.begin()
    display.set_colon(True)

    while continue_reading:
        if args.start_game:
            # Scan for cards    
            (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)
            (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
            
            
            # Get the UID of the card
            (status1,uid1) = MIFAREReader1.MFRC522_Anticoll()
            (status2,uid2) = MIFAREReader2.MFRC522_Anticoll()
            
            if status1 == MIFAREReader1.MI_OK:
                # start = time.time()
                # print("Start: ", start)
                team = getTeam(uid_dict, str(uid1[0] + uid1[1] + uid1[2] + uid1[3]))
                #print("Team:", team)
                if team == "red":
                    R += 1
                if team == "blue":
                    B += 1
                    
                Score = str(R) + "." + str(B)
                
                if B != 21 and R != 21:
                    display.set_colon(True)
                    if B < 10:
                        display.set_digit(2, 0)
                        display.set_digit(3, B)

                    if R < 10:
                        display.set_digit(0, 0)
                        display.set_digit(1, R)
                    
                    if B >= 10:
                        display.set_digit(2, int(str(B)[0]))
                        display.set_digit(3, int(str(B)[1]))
                    
                    if R >= 10:
                        display.set_digit(0, int(str(R)[0]))
                        display.set_digit(1, int(str(R)[1]))
                
                if B == 21:
                    display.set_colon(False)
                    display.set_digit(0, 0)
                    display.set_digit(1, 2)
                    display.set_digit(2, 5)
                    display.set_digit(3, 5)
                    B = 0
                    
                    
                
                if B > 21:
                    B = 15
                    display.set_colon(True)
                    display.set_digit(2, int(str(B)[0]))
                    display.set_digit(3, int(str(B)[1]))
                
                if R == 21:
                    display.set_colon(False)
                    display.set_digit(0, 2)
                    display.set_digit(1, 5)
                    display.set_digit(2, 5)
                    display.set_digit(3, 0)
                    R = 0
                    
                
                if R > 21:
                    R = 15
                    display.set_colon(True)
                    display.set_digit(0, int(str(R)[0]))
                    display.set_digit(1, int(str(R)[1]))
                
                display.write_display()
                end = time.time()
                # print("End: ", end)
                print("Score:", Score)
                GPIO.cleanup()
                time.sleep(1.5)
                
            
            
            if status2 == MIFAREReader2.MI_OK:
                # start = time.time()
                # print("Start: ", start)
                team = getTeam(uid_dict, str(uid2[0] + uid2[1] + uid2[2] + uid2[3]))
                #print("Team:", team)
                if team == "red":
                    R += 3
                if team == "blue":
                    B += 3
                    
                Score = str(R) + "." + str(B)
            
                if B != 21 and R != 21:
                    display.set_colon(True)
                    if B < 10:
                        display.set_digit(2, 0)
                        display.set_digit(3, B)

                    if R < 10:
                        display.set_digit(0, 0)
                        display.set_digit(1, R)
                    
                    if B >= 10:
                        display.set_digit(2, int(str(B)[0]))
                        display.set_digit(3, int(str(B)[1]))
                    
                    if R >= 10:
                        display.set_digit(0, int(str(R)[0]))
                        display.set_digit(1, int(str(R)[1]))
                        
                if B == 21:
                    display.set_colon(False)
                    display.set_digit(0, 0)
                    display.set_digit(1, 2)
                    display.set_digit(2, 5)
                    display.set_digit(3, 5)
                    B = 0
                    
                if B > 21:
                    B = 15
                    display.set_colon(True)
                    display.set_digit(2, int(str(B)[0]))
                    display.set_digit(3, int(str(B)[1]))
                
                if R == 21:
                    display.set_colon(False)
                    display.set_digit(0, 2)
                    display.set_digit(1, 5)
                    display.set_digit(2, 5)
                    display.set_digit(3, 0)
                    R = 0
                    
                if R > 21:
                    R = 15
                    display.set_colon(True)
                    display.set_digit(0, int(str(R)[0]))
                    display.set_digit(1, int(str(R)[1]))
                
                display.write_display()
                end = time.time()
                # print("End: ", end)
                print("Score:", Score)
                GPIO.cleanup()
                time.sleep(1.5)
            
            GPIO.cleanup()
                    
        if args.remove:
            print("List of Registered UIDs:")
            for each in uid_dict.items():
                print(each)
            uid_key = input("Enter the key to remove: ")
            try:
                del uid_dict[uid_key]
            except KeyError:
                # Avoids the KeyError: None statement
                pass
            print("New List of Registered UIDs: " + str(uid_dict))
        
        if args.add:
            # Scan for cards    
            (status1,TagType1) = MIFAREReader1.MFRC522_Request(MIFAREReader1.PICC_REQIDL)
            (status2,TagType2) = MIFAREReader2.MFRC522_Request(MIFAREReader2.PICC_REQIDL)
            
            
            # Get the UID of the card
            (status1,uid1) = MIFAREReader1.MFRC522_Anticoll()
            (status2,uid2) = MIFAREReader2.MFRC522_Anticoll()
                
            if status1 == MIFAREReader1.MI_OK:
                print ("RFID1 : Card read UID: %s,%s,%s,%s" % (uid1[0], uid1[1], uid1[2], uid1[3]))
                print("New UID: ", str(uid1[0] + uid1[1] + uid1[2] + uid1[3]))
                if str(uid1[0] + uid1[1] + uid1[2] + uid1[3]) in uid_dict:
                    print("UID " + str(uid1[0] + uid1[1] + uid1[2] + uid1[3]) +  " is already Registered.")
                color = input("Enter color: ")
                uid_dict[str(uid1[0] + uid1[1] + uid1[2] + uid1[3])] = color
                print("New List of Registered UIDs: " + str(uid_dict))
            
            if status2 == MIFAREReader2.MI_OK:
                print ("RFID2 : Card read UID: %s,%s,%s,%s" % (uid2[0], uid2[1], uid2[2], uid2[3]))
                if str(uid2[0] + uid2[1] + uid2[2] + uid2[3]) in uid_dict:
                    print("UID " + str(uid2[0] + uid2[1] + uid2[2] + uid2[3]) + " is already Registered.")
                color = input("Enter color: ")
                uid_dict[str(uid2[0] + uid2[1] + uid2[2] + uid2[3])] = color
                print("New List of Registered UIDs: " + str(uid_dict))
    
if __name__ == "__main__":
    main()

    
    
        
    
    
        
    
        

        
        
