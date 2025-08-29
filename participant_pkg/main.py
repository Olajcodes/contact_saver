import csv
from file_ops import load_participants
from file_ops import save_participant
from pathlib import Path

workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

participant_dict = {}

def participant_details(): 
    # file_ops.load_participants      # Load participants if any any when app starts
    while True:
                    # Collecting and Validating name input.
        while True:
            try:
                name = input("Kindly enter your name: ")
                if name == "" :
                    print("Name can't be empty! You must provide your name.")
                elif name.isalpha() == False:
                    raise ValueError("Only Alphabets required.")
                else:
                    participant_dict["name"] = name
                    break
            except ValueError as e:
                print("Oops!", e)

        #  Collecting and Validating Age
        while True:
            try:
                age = int(input("Kindly enter your age: "))
                if age < 0:
                    print("Age cannot be negative.")          
                elif (age <=13 or age >= 60):
                    print("Sorry, You are not eligible to participate for this program!")
                else:
                    participant_dict["age"] = age
                    break
            except ValueError:
                print("Oops! That's not a valid age.\nYou can only provide positive numbers.")
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


save_participant(csv_file, participant_dict)
load_participants(csv_file)


