# Open file
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
        print(f"Start: {start}")
        sample_string = data[start:]
        print(f"String: {sample_string}")
        if start == -1:
            more_muls = False
            print(f"Result: {result}")
            break
        for char in sample_string:
            if char.isdigit():
                string_num += char
                print("Found digit: ", string_num)
            elif char == ",":
                numbers.append(int(string_num))
                print("Found full number: ", string_num)
                string_num = ""
            elif char == ")":
                numbers.append(int(string_num))
                if len(numbers) == 2:
                    mult_number = numbers[0] * numbers[1]
                    print(f"Success! {mult_number} added to result.")
                    result += mult_number
                    print(f"Running result: {result}\n")
                    start_index = start + 4
                    numbers = []
                    string_num = ""
                    break
            elif len(string_num) > 0 or len(numbers) > 0:
                print(f"NOT MUL VALUE: {char}\n")
                string_num = ""
                numbers = []
                start_index = start + 4
                break
        
    
find_muls(data)
# First answer: 192767529