input = open("input.txt")
data = input.read()

result = 0

start = data.find("mul(")
end = (data[1:].find(")")) + 2

print(data[start:end])

# TODO: Find how to pull numbers out of string, maybe using "re" library.
# TODO: Write function to look through data, pull each mul and add to result. Break if contains invalid characters.
