import csv
from pathlib import Path


workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"


headernames = ["Name", "Age", "  Phone Number", "Track"]

#  Function to append participant details to a CSV file
def save_participant(csv_file, participant_dict):

    #Checking if file exist
    if csv_file.exists():
        with open(csv_file, "r+", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headernames)
            writer.writerows(participant_dict)

    else:
         with open(csv_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headernames)
            writer.writeheader()
            writer.writerows(participant_dict)