# Polyphorism
# single entity and many forms

# 2 types of polyphorism
# 1. compile time polyphorism (overloading) - this is not supported in python
# 2. runtime polyphorism (overridding)

# # 1. Compile time Polyphorism
# # same name methods with different parameters and on bases of that different behaviours - this is not supported in python
# # even if we have n number of same name method, it will only consider the latest method
# class animal:
#     def dog(self,bone,pedigree):
#         print("Salivation")

#     def dog(self,cat):
#         print("Barks")

# animal_obj = animal()
# animal_obj.dog(1)

# 2. runtime polyphorism (overridding)
# it can only happen in inheritance
# whenever a method of our parent class is not according to what we want, then we override it
# rules of overridings are
    # 1. It should have same name as parent class method name
    # 2. It should have same no. of parameters and same datatype of parameters as that of parent class

class old_tv:
    def color(self):
        print("Black and White")

    def video(self):
        print("480p")

    def audio(self):
        print("mono")


class new_tv(old_tv):
    def color(self):
        print("Color TV")
    
    def disttv(self):
        print("DishTV")

new_tv_obj = new_tv()
new_tv_obj.color()
    