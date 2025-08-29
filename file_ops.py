
# Importing necessary packages
import csv
from pathlib import Path


workspace = Path("workspace")
workspace.mkdir(exist_ok= True)
csv_file = workspace / "contacts.csv"


headernames = ["Name", "Age", "  Phone Number", "Track"]

#  Function to append participant details to a CSV file
def save_participant(csv_file, participant_dict):
    with open(csv_file, "r+", newline="", encoding="utf-8") as f:       # open the csv file
        line1 = f.readline()        # read the first line of the file
        header = []                 # Created a list of headers
        for (key, value) in participant_dict.items():           # iterated the items in the dictionary
            header.append(key)      # append each key to the header
        formatted_header = ",".join(header)     # Join all the headers, separating them by commas
        
        if (f"{formatted_header}\n" not in line1):      #  This creates a new header if it hasn't previously existed
            f.writelines(f"{formatted_header}\n")       

        for (key, value) in participant_dict.items():     # This iterates each item (key and value) in the dictionary of participant details 
            f.write(f"{value}, ")       # This appends the content for the value
        f.write("\n")               # This priints each kay and value in a new line
         




