
import csv
#  Function to append participant details to a CSV file
def save_participant(csv_file, participant_dict):
    with open(csv_file, "r+", newline="", encoding="utf-8") as f:
        line1 = f.readline()
        header = []
        for (key, value) in participant_dict.items():
            header.append(key)
        formatted_header = ",".join(header)
        
        if (f"{formatted_header}\n" not in line1):
            f.writelines(f"{formatted_header}\n")

        for (key, value) in participant_dict.items():
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
