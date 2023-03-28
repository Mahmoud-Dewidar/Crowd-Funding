from os import name

from .Operations import *
import json
import re
import datetime

r = "\033[31m"
r1 = "\033[0m"
g = "\033[32m"
g1 = "\033[0m"


def displayMenu():
    while True:
        print("\nPlease select an option:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")
        if choice == "1":
            register()
        elif choice == "2":
            user = login()
            if user:
                while True:
                    print("\nPlease select an option:")
                    print("1. Create a project")
                    print("2. View all projects")
                    print("3. Edit a project")
                    print("4. Delete a project")
                    print("5. Search for a project by date")
                    print("6. Logout")
                    choice = input("Enter your choice (1-6): ")

                    if choice == "1":
                        create_project(user)
                    elif choice == "2":
                        view_all_projects()
                    elif choice == "3":
                        edit_project(user)
                    elif choice == "4":
                        delete_project(user)
                    elif choice == "5":
                        search_project_by_date()
                    elif choice == "6":
                        break
                    else:
                        print(f"{r}Invalid choice! Please select a valid option.{r1}")
        elif choice == "3":
            print(f"{g}Thank you for using our app!{g1}")
            break
        else:
            print(f"{r}Invalid choice! Please select a valid option.{r1}")
