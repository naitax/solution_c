import json

a_file = open("convert_to_txt.txt", "r")
yourResult = [line.split(',') for line in a_file.readlines()]
print(json.dumps(yourResult))

#converts text from txt file to json dictonary
