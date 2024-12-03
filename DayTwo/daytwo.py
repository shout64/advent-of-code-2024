import lists
import pandas as pd

# Safe reports
# Are all numbers increasing or decreasing
# Is difference between 1-3

file = open(r"C:\Users\Devin\Development\github\advent-of-code-2024\DayTwo\lists.txt")

data = file.read()
report_list = [l.split(" ") for l in data.split("\n") if l]

num_of_safe_reports = 0
# parse 5 characters as one report

for i in report_list:
    last_number = 0
    report_safe = True
    increasing = False
    decreasing = False

    for j in i:
        if (j != i[0]):
            if int(j) < last_number:
                increasing = True
            elif int(j) > last_number:
                decreasing = True

        if increasing and decreasing:
            report_safe = False

        difference = abs(int(j) - last_number)
        if (j != i[0]) and (difference not in [1, 2, 3]):
            report_safe = False

        last_number = int(j)

    # print(f"Row {i} is Report Safe = {report_safe}")
    if report_safe == True:
        num_of_safe_reports += 1

        


print(f"Number of safe reports: {num_of_safe_reports}")
