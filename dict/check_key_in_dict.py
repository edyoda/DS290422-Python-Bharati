dict_demo = {"one":"Ram","two":"Laxman","three":"Sita"}

key = input("Enter key you want to check : ")


# dict = {'name': 'foo', 'age': 28}
# takeInput = input("Key here : ")
# if takeInput in dict.keys():
#     print("keys is here {}".format(takeInput))
# else:
#     print("not There")

dict={"one":"ram","two":"sita","three":"laxman"}
key=input("enter key you want to check")
for i in dict.keys():
    if i==key:
        print("Key present")
        break
else:
    print("Not present")
