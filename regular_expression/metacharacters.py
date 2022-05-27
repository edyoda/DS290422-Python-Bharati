import re

# Metacharacters

data = "hii"
result = re.findall("[a-z]",data) # expression,data
print(result)

data = "Hii"
result = re.findall("[A-z]",data) # expression,data
print(result)

txt = "The rain in Spain"
#Find all lower case characters alphabetically between "a" and "m":
x = re.findall("[a-m]", txt)
print(x)

txt = "That will be dollars"
#Find all digit characters:
x = re.findall("\d", txt)
print(x)

txt = "hello planet"
#Search for a sequence that starts with "he", followed by two (any) characters, and an "o":
x = re.findall("he..o", txt)
print(x)

txt = "hell planet"
#Check if the string starts with 'hello':
x = re.findall("^hello", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")


txt = "hello planet"
#Check if the string ends with 'planet':
x = re.findall("planet$", txt)
if x:
  print("Yes, the string ends with 'planet'")
else:
  print("No match")


txt = "heo planet"
#Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":
x = re.findall("he.*o", txt)
print(x)

txt = "heo planet"
#Search for a sequence that starts with "he", followed by 1 or more  (any) characters, and an "o":
x = re.findall("he.+o", txt)
print(x)

txt = "heo planet"
#Search for a sequence that starts with "he", followed by 0 or 1  (any) character, and an "o":
x = re.findall("he.?o", txt)
print(x)
#This time we got no match, because there were not zero, not one, but two characters between "he" and the "o"


txt = "helllllo planet"
#Search for a sequence that starts with "he", followed excactly 2 (any) characters, and an "o":
x = re.findall("he.{5}o", txt)
print(x)


txt = "The rain in Spain falls mainly in the plain!"
#Check if the string contains either "falls" or "stays":
x = re.findall("falls|stays|plain", txt)
print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")


