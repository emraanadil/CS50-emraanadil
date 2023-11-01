# program to get the grade level of text
from cs50 import get_string
# getting user input
text = get_string("Text: ")
# i nitializing variables:
letters = words = sentences = i = 0

# countgin the no of letters words and sentencs
while i < len(text):
    if text[i].isalpha():
        letters += 1
# counting words
    if i == 0 and text[i] != " " or i != 0 and text[i] == " ":
        words += 1
# counting sentences/
    if text[i] == "." or text[i] == "!" or text[i] == "?":
        sentences += 1
    i += 1

L = (letters / words) * 100
S = (sentences / words) * 100
index = round(0.0588 * L - 0.296 * S - 15.8)

# printing
if index < 1:
    print("Before Grade 1")
elif index >= 16:
    print("Grade 16+")
else:
    print(f"Grade {index}")

