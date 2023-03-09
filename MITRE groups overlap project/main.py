# Must work with Python version 3.9 or higher
import pandas as pd
import requests
from bs4 import BeautifulSoup
import json
import os


def compare_groups(group1, group2, url1, url2):
    """ The function gets 2 group names and their addresses and makes a comparison between them trying to identify
     identical techniques """
    first_table = pd.read_html(url1)
    response1 = requests.get(url1)
    content1 = response1.content
    soup1 = BeautifulSoup(content1, 'html.parser')
    title1 = soup1.title.string
    comma_pos = title1.find(',')
    if comma_pos != -1:
        title1 = title1[:comma_pos]

    second_table = pd.read_html(url2)
    response2 = requests.get(url2)
    content2 = response2.content
    soup2 = BeautifulSoup(content2, 'html.parser')
    title2 = soup2.title.string
    comma_pos = title2.find(',')
    if comma_pos != -1:
        title2 = title2[:comma_pos]

    try:
        for table in first_table:
            if "Use" in table.columns:
                table_1 = table
                break
    except KeyError:
        print("Error: Table not found")
        exit()

    try:
        for table in second_table:
            if "Use" in table.columns:
                table_2 = table
                break
    except KeyError:
        print("Error: Table not found")
        exit()

    technique_1 = table_1["Name"].tolist()

    technique_2 = table_2["Name"].tolist()

    count = 0
    similar_techniques = []

    for obj in technique_1:
        if obj in technique_2:
            similar_techniques.append(obj)
            count += 1

    with open(f"reports/{group1}_{group2}_comp.txt", 'w') as file:
        if len(technique_1) <= len(technique_2):
            avg = (count / len(technique_1) * 100).__round__(2)
            file.write(
                f"{title1} group and {title2} group are similar in {avg}%\n\n")
            print(
                f"{title1} group and {title2} group are similar in {avg}%\n\n")
        else:
            avg = (count / len(technique_2) * 100).__round__(2)
            file.write(
                f"{title1} group and {title2} group are similar in {avg}%\n\n")
            print(
                f"{title1} group and {title2} group are similar in {avg}%\n\n")
        if avg >= 85:
            with open("similar groups/similar_groups.txt", 'a') as f1:
                f1.write(f"{title1} - {title2} has {avg}% similarity\n")

        file.write(f"{title1} Techniques:\n")
        file.write("\n".join(technique_1))
        file.write("\n\n")
        print(f"{title1} Techniques:\n")
        print("\n".join(technique_1))
        print("\n\n")
        file.write(f"{title2} Techniques:\n")
        file.write("\n".join(technique_2))
        file.write("\n\n")
        print(f"{title2} Techniques:\n")
        print("\n".join(technique_2))
        print("\n\n")
        file.write(f"The similar techniques are:\n")
        file.write("\n".join(similar_techniques))
        print(f"The similar techniques are:\n")
        print("\n".join(similar_techniques))


chose = input('''Menu :
option 1 : choose 2 groups and it compares between them only.
option 2 : compares all the groups
please enter your choose: ''')


with open('Groups.txt', 'r') as f:
    contents = json.load(f)

try:
    os.mkdir("reports")
    print("file opened")
except FileExistsError:
    print("file already exists")

try:
    os.mkdir("similar groups")
    print("file opened")
except FileExistsError:
    print("file already exists")

with open("similar groups/similar_groups.txt", 'w') as f2:
    print("file opened")

if chose == "1":
    firstGroup = input("Enter the name of group 1 : ").upper()
    secondGroup = input("Enter the name of group 2 : ").upper()

    try:
        firstAddress = contents[firstGroup]
    except KeyError:
        print("Error: Invalid input")
        exit()

    try:
        secondAddress = contents[secondGroup]
    except KeyError:
        print("Error: Invalid input")
        exit()

    print("Loading...")
    compare_groups(firstGroup, secondGroup, firstAddress, secondAddress)
    print("Finished!")

elif chose == "2":
    contents2 = contents.copy()
    print("Loading...")
    for firstGroup, firstAddress in contents.items():
        for secondGroup, secondAddress, in contents2.items():
            if firstGroup != secondGroup:
                compare_groups(firstGroup, secondGroup, firstAddress, secondAddress)
        del contents2[firstGroup]
    print("Finished!")

else:
    print("wrong choose!")



