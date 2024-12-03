# Find Safe reports
# Are all numbers increasing or decreasing
# Is difference between 1-3

file = open(r"C:\Users\Devin\Development\github\advent-of-code-2024\DayTwo\lists.txt")

data = file.read()
report_list = [l.split(" ") for l in data.split("\n") if l]


# parse 5 characters as one report

def analyze_reports(reports):
    num_of_safe_reports = 0
    last_number = 0
    report_safe = True
    increasing = False
    decreasing = False
    index = 0

    for j in reports:
        if (index != 0):
            if int(j) < last_number:
                decreasing = True
                # print("Decreasing: ", decreasing)
            elif int(j) > last_number:
                increasing = True
                # print("Increasing: ", decreasing)

        if increasing == True and decreasing == True:
            report_safe = False

        difference = abs(int(j) - last_number)
        if (index != 0) and (difference not in [1, 2, 3]):
            report_safe = False

        last_number = int(j)
        index += 1

    if report_safe == True:
        num_of_safe_reports += 1

    return num_of_safe_reports

for i in range(len(report_list)):
    safies = analyze_reports(report_list[i])

    print(safies)

