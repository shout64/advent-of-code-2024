input = open("input.txt")
data = input.read()


def find_muls(data):
    result = 0
    numbers = []
    string_num = ""
    start_index = 0
    more_muls = True

    while more_muls == True:
        start = data.find("mul(", start_index)
        sample_string = data[start:]
        if start == -1:
            more_muls = False
            return result
        for char in sample_string:
            if char.isdigit():
                string_num += char
            elif char == ",":
                numbers.append(int(string_num))
                string_num = ""
            elif char == ")":
                numbers.append(int(string_num))
                if len(numbers) == 2:
                    mult_number = numbers[0] * numbers[1]
                    result += mult_number
                    start_index = start + 4
                    numbers = []
                    string_num = ""
                    break
            elif len(string_num) > 0 or len(numbers) > 0:
                string_num = ""
                numbers = []
                start_index = start + 4
                break
        

def find_conditional_muls(data):
    start_index = 0
    conditional_result = 0
    more_muls = True

    while more_muls == True:
        dont = data.find("don't()", start_index)
        if dont == -1:
            string = data[start_index:]
        else:
            string = data[start_index:dont]
        conditional_result += find_muls(string)
        start_index = data.find("do()", dont)
        if start_index == -1:
            more_muls = False



    print(f"Total conditional data: {conditional_result}")
    return conditional_result

print(f"Total Part 1 data: {find_muls(data)}")
find_conditional_muls(data)
