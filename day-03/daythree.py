# Open file
input = open("input.txt")
data = input.read()

result = 0

def find_muls(data):
    all_muls = []
    numbers = []
    string_num = ""
    start_index = 0
    more_muls = True

    start = data.find("mul(", start_index)
    sample_string = data[start:]
    for char in sample_string:
        if char.isdigit():
            string_num += char
        elif char == ")":
            break #Prolly not right
        else:
            if string_num != "":
                numbers.append(int(string_num))
                string_num = ""

    #Probably check for invalid characters or start next loop
    all_muls.append(sample_string)
    start_index = end

    print(all_muls)
    
find_muls(data)

numbers = []
string_num = ""

# TODO: Write function to look through data, pull each mul and add to result. Break if contains invalid characters.

# for char in sample_string:
#     if char.isdigit():
#         string_num += char
#     else:
#         if string_num != "":
#             numbers.append(int(string_num))
#             string_num = ""
