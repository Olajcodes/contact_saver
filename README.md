# Contact Saver

## Project Description
Contact Saver is a Python-based application that allows users to store and retrieve contact information efficiently. It collects user input, saves participant details to a CSV file, and loads saved records when needed. The project uses the `pathlib` library for handling file paths and ensures data persistence in a simple, structured format.

---

## How to Run the Program

### Option 1: Creating the program yourself
1. Create a folder named `participant_pkg`.
2. Inside it, add an empty `__init__.py` file.
3. Create a helper module named `file_ops.py`.
4. In `file_ops.py`, define:
   - `save_participant(path, participant_dict)`: Appends participant details to a CSV file (creates the file with a header if it does not exist).
   - `load_participants(path)`: Reads participants from the CSV file and returns them as a list of dictionaries.
5. Outside `participant_pkg`, create `main.py` to run the application.
6. Run:
   ```bash
   python main.py

### Option 2: Manual Setup
1. git clone https://github.com/Olajcodes/contact_saver
2. cd contact_saver
3. python main.py

## Contributors

- Abioye Olajide – Handled user input validation, error handling, and merging of final code.

- Adeoye Mary – Developed the user input collection logic.

- Osisami Michael – Implemented the save_participant function for saving data.

- Adelegan Deborah – Implemented the load_participant function for retrieving saved data.