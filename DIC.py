import json
from difflib import get_close_matches
data = json.load(open("data.json"))


def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:  # if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data:  # in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        YN = input("Did You Mean %s instead? Enter y if Yes or n if No.(y/n) :" % get_close_matches(word, data.keys())[0])
        if YN == "y":
            return data[get_close_matches(word, data.keys())[0]]
        elif YN == "n":
            return "This Word Dosen't Exist."
        else:
            return "Invalid Reply."
    else:
        return "This Word Dosen't Exist."


word = input("Enter Word : ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
