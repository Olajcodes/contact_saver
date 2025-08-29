
import csv
#  Function to append participant details to a CSV file
def load_participants(csv_file):
    with open(csv_file, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        
fieldnames = ["Name", "Age", "  Phone Number", "Track"]
def save_participant(csv_file, participant_dict):
    with open(csv_file, "a+", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(participant_dict)


    return load_participants
