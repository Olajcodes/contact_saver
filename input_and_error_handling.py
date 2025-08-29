
# from participant_pkg import file_ops

import csv
from pathlib import Path
file = Path.cwd()
workspace = file/Path("task11/participant_pkg/workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"

participant_dict = {}



def participant_details():
    # load_participants()    
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