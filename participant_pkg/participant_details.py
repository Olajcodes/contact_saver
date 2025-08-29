import csv
from pathlib import Path

from participant_pkg import file_ops
workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

participant_dict = {}



def participant_details():
    while True:
        # Collecting and Validating Phone number
        while True:
            try:
                phone_no = input("Kindly input your phone number (Country code not accepted): ")
                if phone_no.startswith("+"):
                    print("Invalid entry. No country code please.")
                elif len(phone_no) != 11:
                    print("Your phone number must be exactly 11 digits. Try again.")
                else:
                    participant_dict["phone_no"] = phone_no
                    break
            except ValueError:
                print("You can only input numbers")
            except TypeError:
                print("It can only check for length of strings and not integers")

        #  Collecting and Validating Track input
        while True:
            try:
                track = input("Kindly enter your track: ")
                if track.isalpha() == False:
                    raise ValueError("Must only be Alphabets")
                else:
                    participant_dict["track"] = track
                    break
            except ValueError as e:
                print("Oops!", e)
        print("\nRegistration Successful\n") 
 
        #  Getting to exit the program
        print("To exit the program, follow the instruction below:")
        choice_exit = int(input("Kindly type 0 to exit the program  or 1 to continue: ")) 
        if choice_exit == 0:
            break 
        else:
            print("\n<--- Next Participant --->\n")
            continue

participant_details()
