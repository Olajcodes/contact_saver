
# Importing necessary packages
import csv
from pathlib import Path


workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"


def save_participant(csv_file, participant_dict):
    names = list(participant_dict.keys())   # Extract header from the dictionary keys
    file_exists = csv_file.exists()
    with open(csv_file, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=names)
        if not file_exists:
            writer.writeheader()
        writer.writerow(participant_dict)
        

def load_participants(csv_file):
    participants = []   #Reading all participants from the CSV and returning them as a list of dictionary
    if csv_file.exists():
        with open(csv_file, "r", encoding="utf-8", newline="") as f:
            reader = csv.reader(f)
            for row_number, row in enumerate(reader):
                participants.append(row)
                if row_number == 0:  # Header row
                    print(f"\n{'\t|  '.join(row)}")
                    print("-" * 50)
                else:  # Data rows
                    name, age, phone_no, track = row
                    print(f"{name}\t|  {age}\t|  {phone_no}\t|  {track}")
    else:
        print("No record of participants found!")
    return participants
