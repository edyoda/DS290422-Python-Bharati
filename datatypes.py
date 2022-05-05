"""
Datatype

1. Datatype represents the kind of value.
2. Variables can hold values, and every value has a data-type. 
3. Python is a dynamically typed language; hence we do not need to define the type of the variable while declaring it. 
4. The interpreter implicitly binds the value with its type.
"""

"""
Datatype

int
float
complex
bool
str
list
tuple
set
dict
None
"""


# int datatype
num = 20
print(type(num))


# float datatype
num_1 = 56.7
print(type(num_1))


# str datatype
name = "Edyoda"
print(type(name))


# bool datatype
female = True
print(type(female))


# complex datatype
complex = 3+2j
print(type(complex))


# list datatype
# list - [] , mutable , allows duplicate elements
student_names = ["Harsh","Omkar","Deepshikha","Nikunj"]
print(student_names)                   # to fetch all the elements
student_names[3] = "Shubham"           # to fetch the element on the bases of index
print(student_names)
print(type(student_names))
print(student_names)
print(student_names[3],student_names[0])

# lst = [1,2,2,4,5,7,2,2,2,2,2,35,7,898,"1.Bharati","A",7.8]
# print(lst)


# tuple datatype
# tuple - () , immutable, allows duplicate elements
student_names = ("Harsh","Omkar","Deepshikha","Nikunj","Deepshikha")
print(student_names)
print(student_names[1])


# set datatype
# set - {} , mutable , non-indexed
set_example = {1,2,5,6,5,5,5,1,7,8,9,9,6}
print(set_example)


# dict datatype
# dict - {key:pair} , mutable, non-indexed, it stores data in key and value format
names = {"Rajkumar":"Bharati",2:"Hritik",3:"Ram",4:"Bharati"}
print(names[2])
names[5] = "Meraj"
print(names)
names[3] = "Laxman"
print(names)


# None datatype
name = None
print(name)
print(type(name))