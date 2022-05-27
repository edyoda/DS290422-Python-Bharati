import re

txt = "rain in Spain"
#Check if the string starts with "The":
x = re.findall("\AThe", txt)
print(x)


txt = "The rain in Spain"
#Check if "ain" is present at the beginning of a WORD:
x = re.findall(r"\brai", txt)
print(x)


txt = "The ainr in Spain"
#Check if "ain" is present, but NOT at the beginning of a word:
x = re.findall(r"\Bain", txt)
print(x)


txt = "The rain in Spain 10"
#Check if the string contains any digits (numbers from 0-9):
x = re.findall("\d", txt)
print(x)

txt = "The rain in Spain 10"
#Check if the string doesnot contains any digits (numbers from 0-9):
x = re.findall("\D", txt)
print(x)


txt = "The rain in Spain"
#Return a match at every white-space character:
x = re.findall("\s", txt)
print(x)


txt = "The rain in Spain"
#Return a match at every character and excludes space:
x = re.findall("\S", txt)
print(x)


txt = "The rain in Spain 123 __  @@@@@"
#Return a match at every word character (characters from a to Z, digits from 0-9, and the underscore _ character):
x = re.findall("\w", txt)
print(x)


txt = "The rain in Spain @@@@@"
#Return a match at every NON word character (characters NOT between a and Z. Like "!", "?" white-space etc.):
x = re.findall("\W", txt)
print(x)


txt = "The rain in Spain"
#Check if the string ends with "Spain":
x = re.findall("Spain\Z", txt)
print(x)