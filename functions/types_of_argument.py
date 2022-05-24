# types of arguments

# 1. required / positional argument
# 2. default argument
# 3. keywords argument
# 4. variable-length argument
# 4.1. Arbitrary Positional arugument
# 4.2. Arbitrary Keyword argument

# # required / positional argument
# def add(no1,no2):
#     addition = no1+no2
#     return addition

# result = add(5,5)
# print("Result : ",result)

# # default argument
# def add(no1=90,no2=10):
#     addition = no1+no2
#     return addition

# result = add(6,7)
# print("Result : ",result)

# keywords argument
# def add(no1,no2=900):
#     print(no1,no2)
#     addition = no1+no2
#     return addition

# result = add(no1 = 20,no2 = 90)
# print("Result : ",result)

# # Variable-length argument - Arbitrary Positional argument
# # *args -> tuple

# def family_member_count(*name):
#     print(type(name))
#     print(name)
#     for i in name:
#         print(i,end="/")

# family_member_count(1,2,3,4,5,"Deep","Mohit",9.0,True,[1,2,4,5],(6,7,5))

# # Variable-length argument - Arbitrary Keyword argument
# # **kwargs -> dict (here kw means keywords not key)

def students(**student_data):
    print(type(student_data))
    for k,v in student_data.items():
        print(k,"  ",v)
    for i in student_data:
        print(i)
    for i in student_data.values():
        print(i)

students(one="Pankaj",two="Deep",three="Bharati")





