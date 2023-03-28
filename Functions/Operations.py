import json
import re
import datetime
from .Helpers import *

r = "\033[31m"
r1 = "\033[0m"
g = "\033[32m"
g1 = "\033[0m"
users_file = "DataFiles\\users.json"
projects_file = "DataFiles\\projects.json"


# User Authentication
def register():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    email = input("Enter your email: ")
    while not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        email = input(f"{r}Invalid email.{r1} Please enter your email: ")
    while True:
        password = input("Enter your password: ")
        confirm_password = input("Confirm your password: ")
        if password == confirm_password:
            break
        else:
            print(f"{r}Passwords do not match. Please try again.{r1}")
    phone_number = input("Enter your mobile phone number: ")

    # Validate phone number
    while not is_valid_phone_number(phone_number):
        print(f'''{r}Invalid phone number! Please enter a valid Egyptian phone number.{r1}''')
        phone_number = input("Enter your mobile phone number: ")

    # Check if email already exists in the database
    users = load_json_data(users_file)
    for user in users:
        if user["email"] == email:
            print(f"{r}Email already exists! Please try again with a different email.{r1}")
            return

    # Add user to database
    user = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "password": password,
        "phone_number": phone_number
    }
    users.append(user)
    save_json_data(users_file, users)
    print(f"{g}User registered successfully!{g1}")


def login():
    email = input("Enter your email: ")
    password = input("Enter your password: ")

    # Check if email and password match with any user in the database
    users = load_json_data(users_file)
    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"{g}User logged in successfully!{g1}")
            return user

    print(f"{r}Incorrect email or password! Please try again.{r1}")
    return None


def create_project(user):
    title = input("Enter the project title: ")
    details = input("Enter the project details: ")
    total_target = float(input("Enter the project total target amount: "))

    start_date = input("Enter the project start date (yyyy-mm-dd): ")
    while not is_valid_date(start_date):
        print(f"{r}Invalid date format! Please enter the date in the correct format.{r1}")
        start_date = input("Enter the project start date (yyyy-mm-dd): ")

    end_date = input("Enter the project end date (yyyy-mm-dd): ")
    while not is_valid_date(end_date):
        print(f"{r}Invalid date format! Please enter the date in the correct format.{r1}")
        end_date = input("Enter the project end date (yyyy-mm-dd): ")

    project = {
        "title": title,
        "details": details,
        "total_target": total_target,
        "start_date": start_date,
        "end_date": end_date,
        "owner_email": user["email"],
        "current_amount": 0
    }

    projects = load_json_data(projects_file)
    projects.append(project)
    save_json_data(projects_file, projects)
    print(f"{g}Project created successfully!{g1}")


def view_all_projects():
    projects = load_json_data(projects_file)
    print("All projects:")
    for project in projects:
        print(
            f"{project['title']}: {project['details']} {g}|{g1} Total target: {project['total_target']} EGP {g}|{g1} Current amount: {project['current_amount']} EGP {g}|{g1} Start date: {project['start_date']} {g}|{g1} End date: {project['end_date']}.")


def edit_project(user):
    projects = load_json_data(projects_file)
    user_projects = []
    for project in projects:
        if project["owner_email"] == user["email"]:
            user_projects.append(project)
            print(f"{len(user_projects)}. {project['title']}")

    if not user_projects:
        print(f"{r}You don't have any projects yet!{r1}")
        return

    # Ask user to select a project to edit
    project_index = int(input("Enter the number of the project you want to edit: "))
    while project_index < 1 or project_index > len(user_projects):
        print(f"{r}Invalid project number! Please enter a valid project number.{r1}")
        project_index = int(input("Enter the number of the project you want to edit: "))

    # Edit project details
    project = user_projects[project_index - 1]
    print("Edit project details (leave blank to keep the current value):")
    title = input(f"Title ({project['title']}): ") or project["title"]
    details = input(f"Details ({project['details']}): ") or project["details"]
    total_target = float(input(f"Total target ({project['total_target']}): ") or project["total_target"])

    start_date = input(f"Start date ({project['start_date']}): ") or project["start_date"]
    while not is_valid_date(start_date):
        print(f"{r}Invalid date format! Please enter the date in the correct format.{r1}")
        start_date = input(f"Start date ({project['start_date']}): ") or project["start_date"]

    end_date = input(f"End date ({project['end_date']}): ") or project["end_date"]
    while not is_valid_date(end_date):
        print(f"{r}Invalid date format! Please enter the date in the correct format.{r1}")
        end_date = input(f"End date ({project['end_date']}): ") or project["end_date"]

    # Update project in database
    project["title"] = title
    project["details"] = details
    project["total_target"] = total_target
    project["start_date"] = start_date
    project["end_date"] = end_date

    save_json_data(projects_file, projects)
    print(f"{g}Project updated successfully!{g1}")


def delete_project(user):
    projects = load_json_data(projects_file)
    user_projects = []
    for project in projects:
        if project["owner_email"] == user["email"]:
            user_projects.append(project)
            print(f"{len(user_projects)}. {project['title']}")

    if not user_projects:
        print(f"{r}You don't have any projects yet!{r1}")
        return

    # Ask user to select a project to delete
    project_index = int(input("Enter the number of the project you want to delete: "))
    while project_index < 1 or project_index > len(user_projects):
        print(f"{r}Invalid project number! Please enter a valid project number.{r1}")
        project_index = int(input("Enter the number of the project you want to delete: "))

    # Delete project from database
    project = user_projects[project_index - 1]
    projects.remove(project)
    save_json_data(projects_file, projects)
    print(f"{g}Project deleted successfully!{g1}")


def search_project_by_date():
    projects = load_json_data(projects_file)
    date = input("Enter the date (in YYYY-MM-DD format) to search for projects: ")
    while not is_valid_date(date):
        print(f"{r}Invalid date format! Please enter the date in the correct format.{r1}")
        date = input("Enter the date (in YYYY-MM-DD format) to search for projects: ")

    found_projects = []
    for project in projects:
        if project["start_date"] <= date <= project["end_date"]:
            found_projects.append(project)

    if not found_projects:
        print(f"{r}No projects found!{r1}")
    else:
        print(f"{g}Found projects:{g1}")
        for project in found_projects:
            print(
                f"{project['title']}: {project['details']} {g}|{g1} Total target: {project['total_target']} EGP {g}|{g1} Current amount: {project['current_amount']} EGP {g}|{g1} Start date: {project['start_date']} {g}|{g1} End date: {project['end_date']}.")
