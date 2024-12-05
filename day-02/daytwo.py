file = open("lists.txt", "r")
data = file.read()
report_list = [l.split(" ") for l in data.split("\n") if l]

num_of_safe_reports = 0

def analyze_reports(report):
    for i in range(len(report)-1):
        a, b = report[i], report[i+1]
        if not 1 <= abs(a-b) <= 3:
            return False
        
        if i == len(report)-2:
            continue

        c = report[i+2]

        if not a < b < c and not a > b > c:
            return False
    return "Safe"



for i in range(len(report_list)):
    str_numbers = report_list[i].copy()
    numbers = [int(item) for item in str_numbers]
    result = analyze_reports(numbers)
    if result == "Safe":
        num_of_safe_reports += 1
    else:
        for n in range(len(numbers)):
            if analyze_reports(numbers[:n] + numbers[n+1:]) == "Safe":
                num_of_safe_reports += 1
                break

print(f"TOTAL Number of safe reports: {num_of_safe_reports}")
# Part 1 answer was 624
# Part 2 answer was 658