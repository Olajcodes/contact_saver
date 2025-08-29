
import csv
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

        for (key, value) in participant_dict.items():     # This iterates each item (key and value) in the dictionary of paerticipant details 
            f.write(f"{value}, ")
        f.write("\n")
         


 # print(line1 == 'name', "age", "phone_no", "track \n")
        # writer = csv.writer(f)
        
#     participant_dict.append()
    
# def load_participants(csv_file):
#     with open(csv_file, "r", encoding="utf-8") as f:
#         reader = csv.reader(f)
        
# fieldnames = ["Name", "Age", "  Phone Number", "Track"]
# def save_participant(csv_file, participant_dict):
#     with open(csv_file, "a+", newline="", encoding="utf-8") as f:
#         writer = csv.DictWriter(f, fieldnames=fieldnames)
#         writer.writeheader()
#         writer.writerows(participant_dict)


    # return load_participants
