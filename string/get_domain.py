email = input("Enter your Email ID : ")

# domain = email.split('@')[1]
# print(domain)
# domain = domain.split('.')[0]
# print(domain)

# new_id = input("enter the mail id")
# print("the original id :",str(new_id))
# domain = new_id[new_id.index("@")+1:]
# print("the domain is :"+str(domain))

# start=email.index('@')
# end=email.index('.')
# domain = email[start+1:end]
# print(domain)



print("enter the email")
x=str(input())
l=""
for index,i in enumerate(x):
    if i=='@':
        l=x[index+1:len(x)]
        print(l)
    else:
        continue
j=l.split('.')
print(j[0])



