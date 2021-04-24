import csv
import os
import tkinter as tk
from tkinter import filedialog

if __name__ == '__main__':
    tk.Tk().withdraw()
    path_to_csv = filedialog.askopenfilename()

    if os.path.getsize(path_to_csv) == 0:
        input('File is empty. Press any key to exit')
        exit(0)

    with open(path_to_csv, 'r') as f:
        reader = csv.reader(f)

        print(f'*** First  line ***\n{next(reader)}')
        print(f'*** Second line ***\n{next(reader)}')

        input()
