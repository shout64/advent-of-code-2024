# Find Safe reports
# Are all numbers increasing or decreasing
# Is difference between 1-3

file = open(r"C:\Users\Devin\Development\github\advent-of-code-2024\DayTwo\lists.txt")
data = file.read()
report_list = [l.split(" ") for l in data.split("\n") if l]

num_of_safe_reports = 0

def analyze_reports(reports):
    last_number = 0
    report_safe = True
    increasing = False
    decreasing = False
    decrease_count = 0
    index = 0

    for j in reports:
        if (index != 0):
            if int(j) < last_number:
                decreasing = True
                decrease_count += 1
                decrease_index = index - 1
                # print("Decreasing: ", decreasing, ". Decrease index: ", decrease_index)
            elif int(j) > last_number:
                increasing = True
                increase_index = index
                # print("Increasing: ", increasing, ". Increase index: ", increase_index)

        if increasing == True and decreasing == True:
            report_safe = False
            if decrease_count >= 2:
                index = increase_index
            elif increase_index > decrease_index:
                index = decrease_index
            else:
                index = increase_index
            break

        difference = abs(int(j) - last_number)
        if (index != 0) and (difference not in [1, 2, 3]):
            report_safe = False
            break

        last_number = int(j)
        index += 1

    if report_safe == True:
        return "Safe"
    else:
        return index


for i in range(len(report_list)):
    print(i + 1)
    print(report_list[i])
    result = analyze_reports(report_list[i])
    if result != "Safe":
        second_list = report_list[i].copy()
        third_list = report_list[i].copy()
        second_list.pop(int(result))
        third_list.pop(result-1)
        print("Second List: ", second_list)
        print("Third List: ", third_list)
        second_attempt = analyze_reports(second_list)
        third_attempt = analyze_reports(third_list)
        if second_attempt != "Safe":
            print(f"2nd Pass FAIL: \n{second_list}")
        elif second_attempt == "Safe":
            print(f"2nd Pass Safe: \n{second_list}")
            num_of_safe_reports += 1
            
        
        if second_attempt != "Safe" and third_attempt != "Safe":
            print(f"3rd Pass FAIL: \n{third_list}")
        elif second_attempt != "Safe" and third_attempt == "Safe":
            print(f"3rd Pass Safe: \n{third_list}")
            num_of_safe_reports += 1
    elif result == "Safe":
        print(f"1st Pass Safe: \n{report_list[i]}")
        num_of_safe_reports += 1

    print(f"Number of safe reports: {num_of_safe_reports}\n")

print(f"TOTAL Number of safe reports: {num_of_safe_reports}")
# 647 too low. 648 too low. 668 and 657 also not right. 
# Answer is 710. How do?
# Part 1 answer was 624
