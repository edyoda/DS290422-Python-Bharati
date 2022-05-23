# # one way
# alph_list = []
# ascii_list = []

# for i in range(97,123):
#     alph_list.append(chr(i)) #a b c will convert your into char
#     ascii_list.append(i)

# # print(alph_list)
# # print(ascii_list)

# dict1 = {}
# dict1.update(zip(alph_list,ascii_list))
# print(dict1)

# # another way
# ascii ={}
# for i in range(ord("a"),(ord("z")+1)):
#     ascii[chr(i)]=i
# print(ascii)

# asciidict=dict()
# alphaletter=range(97,123)
# print(alphaletter)
# for n in alphaletter:
#     asciidict[chr(n)]= n
    
# print(asciidict)

str1=input("enter your string:")
og = str1
result=""
for i in str1:
    result=i+result
str2=result

if str1 == str2:
    print("Palindrome string")
else:
    print("Not palindrome")

