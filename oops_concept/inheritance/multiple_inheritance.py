# Multiple Inheritance
# means multiple parent classes and single child class




class c_lang:

    def __init__(self):
        print("C lang Constructor")

    def c(self):
        print("C Language")

    def feature(self):
        print("Procedural Feature")

class cpp_lang:

    def __init__(self):
        print("CPP lang Constructor")

    def cpp(self):
        print("CPP Language")

    def feature(self):
        print("OOPs Feature")

class python_lang(cpp_lang,c_lang): 

    def __init__(self):
        # super().__init__()
        cpp_lang.__init__(self)
        c_lang.__init__(self)
        print("Python Constructor")

    def python(self):
        print("Python Language")

    def feature(self):
        # super().feature() # super means object of parent class
        cpp_lang.feature(self)
        c_lang.feature(self)
        print("Opps and procedural method")


python_lang_obj = python_lang()
# python_lang_obj.c()
python_lang_obj.cpp()
python_lang_obj.python()
python_lang_obj.feature()


print(python_lang.__mro__) # Method Resolution Order
print(python_lang.mro())


# If some class is not extending any class, then bydefault is extends object class (pre-define class)
