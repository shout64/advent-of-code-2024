import lists
import pandas as pd

# Safe reports
# Are numbers increasing
# Is difference between 1-3

df = pd.read_csv(r"C:\Users\Devin\Development\github\advent-of-code-2024\DayTwo\lists.txt", sep=" ", header= None)


# parse 5 characters as one report
# def are_reports_safe(reports):
#     more_reports = True

#     while more_reports:

print(df.to_string)