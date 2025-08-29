
# Importing necessary packages
import csv
from pathlib import Path


workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"


headernames = ["Name", "Age", "  Phone Number", "Track"]

#  Function to append participant details to a CSV file
def save_participant(csv_file, participant_dict):

    if csv_file.exists():
        with open(csv_file, "a", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headernames)
            writer.writerows(participant_dict)

    else:
         with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headernames)
            writer.writeheader()
            writer.writerows(participant_dict)
    

def load_participants(csv_file):
    if csv_file.exists():
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.reader(f)

        for row_number, row in enumerate(reader):
            if row_number == 0:
                print(f"Headers: {' | '.join(row)}")
                print("-" * 40)
            else: 
                name, age, phone_no, track = row
                print(f"{name} ({age} years) {phone_no} {track}")
    else:
        print("No record of participants found!")
