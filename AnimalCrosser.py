"""
Author: Alyshba Ahmed
Date: 4.27.2023
Purpose: Animal Crossing Villagers.
"""

import csv


def bday():
    """
    converts user birthday input (MM/DD/YYYY) format to the (DD-MMM) database format.
    """
    user = input('What is your birthday? (Please enter in (MM/DD/YY) format.) ')
    bdayString = ''
    if user[0] == '0':
        user = user[1:]
    bdayString = user[2:4] + '-'
    if int(user[0]) == 1:
        bdayString += 'Jan'
    if int(user[0]) == 2:
        bdayString += 'Feb'
    if int(user[0]) == 3:
        bdayString += 'Mar'
    if int(user[0]) == 4:
        bdayString += 'Apr'
    if int(user[0]) == 5:
        bdayString += 'May'
    if int(user[0]) == 6:
        bdayString += 'Jun'
    if int(user[0]) == 7:
        bdayString += 'Jul'
    if int(user[0]) == 8:
        bdayString += 'Aug'
    if int(user[0]) == 9:
        bdayString += 'Sep'
    if int(user[0]) == 10:
        bdayString += 'Oct'
    if int(user[0]) == 11:
        bdayString += 'Nov'
    if int(user[0]) == 12:
        bdayString += 'Dec'
    return(bdayString)

def askBirthday():
    """
    finds the villager that a user is like based on their birthday.
    """
    with open('data.csv', 'r') as inputFile:
        villager= csv.DictReader(inputFile)
        rows = [row for row in villager]
        n = bday()
        n = n[1:]
        similarTo = []
        for row in rows:
            gender = ''
            if row['Gender'] == 'Female':
                gender += 'she'
            else:
                gender += 'he'
            if row['Birthday'] == n:
                z = list(row.values())[0]
                print(f"You're {z}'s birthday twin! This {row['Style 1']} and {row['Personality']} villager is a {row['Species']} and {gender} is interested in {row['Hobby']}.")

askBirthday()
