import re

# txt = "The rain in Portugal"
# x = re.search("Portugal", txt)
# print(x)


# Pincode
# txt = "601504" #023456
# regex = re.compile("^[1-9]{1}[0-9]{5}$")
# data = (regex.search(txt))
# print(data)
# if data:
#     print("It's a match")
# else:
#     print("It's not a match")


# # Pan Card No
# pan="BQIPG6245P"
# x=re.findall("^[A-Z]{5}\d{4}[A-Z]{1}$",pan) 
# if x:
#     print("Match")
# else:
#     print("Not a match")


# # Aadhar Card No 1
# aadhar="123456789123"
# x=re.findall("^[1-9]{1}[0-9]{11}$",aadhar) 
# if x:
#     print("Match")
# else:
#     print("Not a match")


# # Aadhar Card No 2
# aadhar="1234 1234 1234"
# x=re.findall("^[1-9]{1}[0-9]{3}[\s]{1}[0-9]{4}[\s]{1}[0-9]{4}",aadhar) 
# if x:
#     print("Match")
# else:
#     print("Not a match")


# 34-56-2022
txt="29-10-2022"
# data=re.findall("^[01-31]{2}[-]{1}[01-12]{2}[-]{1}[1-9]{1}[0-9]{3}$", txt)
data = re.findall("^[1-3]{1}[0-9]{1}[-]{1}[0-1][0-2][-]{1}[1-9]{1}[0-9]{3}$",txt)
if data:
    print("match")
else:
    print("No match")


txt = "29"
data = re.findall("[1-3]{1}[0-9]",txt)
print(data)



