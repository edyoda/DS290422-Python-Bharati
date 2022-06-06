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
# txt="29-10-2022"
# # data=re.findall("^[01-31]{2}[-]{1}[01-12]{2}[-]{1}[1-9]{1}[0-9]{3}$", txt)
# data = re.findall("^[1-3]{1}[0-9]{1}[-]{1}[0-1][0-2][-]{1}[1-9]{1}[0-9]{3}$",txt)
# if data:
#     print("match")
# else:
#     print("No match")



# bharati@gmail.com
# atleast 1 upper letter, 1 lower letter, 1 digit, 1 special character , length - 8


# a="10-12-2002"                       # for date
# b=re.search("(^([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])(-)(0[1-9]|1[0-2])(-)[0-9]{4}$)",a)
# y=b.group()
# print(y)


# import re

# date="29-02-2004"
# x=re.findall("\d{2}[-]{1}\d{2}[-]{1}\d{4}$",date)
# if x:
#     y=re.split("-",date)
#     y[0]=int(y[0])
#     y[1]=int(y[1])
#     y[2]=int(y[2])
#     if y[1]<=12 and y[1]>0:
#         if y[1]==1 or y[1]==3 or y[1]==5 or y[1]==7 or y[1]==8 or y[1]==10 or y[1]==12:
#             if y[0]>=1 and y[0]<32:
#                 print("Valid date")
#             else:
#                 print("Invalid date")
#         if y[1]==4 or y[1]==6 or y[1]==9 or y[1]==11:
#             if y[0]>=1 and y[0]<31:
#                 print("Valid date")
#             else:
#                 print("Invalid date") 
#         if y[1]==2 and y[2]%4==0:
#             if y[0]>=1 and y[0]<30:
#                 print("Valid date")
#             else:
#                 print("Invalid date")
#         if y[1]==2 and y[2]%4!=0:
#             if y[0]>=1 and y[0]<29:
#                 print("Valid date")
#             else:
#                 print("Invalid date")       
# else:
#     print("Invalid date")

# import re
# password="Abc2340$$"
# status=False
# x=re.findall("[a-z]",password)

# if x:
#     x=re.findall("[A-Z]",password)
#     if x:
#         x=re.findall("[\d]",password)
#         if x:
#             x=re.findall('[\W]',password)
#             if x:
#                 if len(password)>=8:
#                     print("Valid password")
#                     status=True

# if status==False:
#     print("Not a valid password")


# import re
# date=input("enter date:")
# all = re.findall(r"([0-2]\d|3[01])-(0\d|1[0-2])-([0-9]{4})", date)
# if all:
#     print("date is valid")
# else:
#     print("date is not valid")

# import re
# def gmail():
#     given_id = input("enter your gmail id :")


#     regex = "^([a-zA-Z0-9_.-]+)@([gmail]+)([\.])([com]+)"
#     conditions = re.compile(regex)
#     checked = re.search(conditions,given_id)
#     if checked:
#         print("email id updated sucessfully !!!")
#     else:
#         print("please enter a valid gmail id !!")
# if __name__ == "__main__":
#     gmail()

  
# def new_password():
#     password = input("Enter the Password : ")
#     regex = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!#%*?&]{8,16}$"
#     conditions = re.compile(regex)                
#     checked = re.search(conditions, password)
#     if checked:
#         print("New Password is Updated.")
#     else:
#         print("Please Enter A valid password. !!")
  
     
# if __name__ == '__main__':
#     new_password() 

# import re
# email = "Sw_mandal123@gmail.com"
# regex =re.compile("^[A-z]+[\._]?[0-9]+[@]\w+[.]\w{2,3}$")
# data = regex.search(email)
# if data:
#     print("it is a match")
# else:
#     print("it is not a match")

# import re
# def gmail():
#     given_id = input("enter your gmail id :")


#     regex = "^([a-zA-Z0-9_.-]+)@([a-zA-Z]+)([\.])([a-zA-Z]+)"
#     conditions = re.compile(regex)
#     checked = re.search(conditions,given_id)
#     if checked:
#         print("email id updated sucessfully !!!")
#     else:
#         print("please enter a valid gmail id !!")
# if __name__ == "__main__":
#     gmail()


import re
mobile_no ="918009675955"
regex=re.compile("^[91][1-9]{1}[0-9]{9}")
data = regex.search(mobile_no)
print(data)
if data:
    print("it is a match")
else:
    print("it is not a match") 
