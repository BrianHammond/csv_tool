from class_csv import *
import os

menu = ("""
1. Start      
2. Write a new text file (will overwrite existing file)
0. Exit  
""")

while True:
    print(menu)
    choice = int(input("Enter Choice: "))

    match choice:
        case 0 :
            break

        case 1:
            folder = input("folder: ")
            file = input("file: ") + ".csv"

            if not os.path.isdir(folder):
                print(f"{folder} not found, creating folder")
                os.makedirs(folder)

            Initialize(folder, file).initialize()

        case 2:
            folder = input("folder: ")
            file = input("file: ") + ".csv"
            name = input("name: ")
            title = input("title: ")
            department = input("department: ")
            Append(folder, file, name, title, department).append()
    
        case _:
            print ("pick a valid option")