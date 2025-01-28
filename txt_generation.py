from main import console_gameboard, user_gameboard
import os
import shutil
import sys

# Hidden folder (Linux/macOS or WSL on Windows)
hidden_folder = './.console'

# Create the hidden folder if it doesn't exist
if not os.path.exists(hidden_folder):
    os.makedirs(hidden_folder)

#Dictionary with gameboards
gameboards = {"console_gameboard" : console_gameboard, "user_gameboard" : user_gameboard}

#Function to generate txt file from the gameboard
def txt_generation(value, filename):
    with open('gameboard.txt', 'r') as file:
        lines = file.readlines()
    
    with open(filename, 'w') as output_file:
        for i, line in enumerate(lines):
            if i == 0:
                output_file.write(line)
            else:
                parts = line.split('|')
                updated_row = '|'.join([parts[0]] + [str(value[i-1][j]) if value[i-1][j] != 0 else " " for j in range(10)] + ['']) + '\n'
                output_file.write(updated_row)
    
    if filename == "console_gameboard.txt":
        hidden_file_path = os.path.join(hidden_folder, filename)
        shutil.move(filename, hidden_file_path)
    
    if filename == "user_gameboard.txt":
        os.system(f"notepad.exe {filename}")

for key, value in gameboards.items():
    filename = f"{key}.txt"
    txt_generation(value, filename)