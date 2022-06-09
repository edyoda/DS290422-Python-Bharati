# Multiple Inheritance
# means multiple parent classes and single child class

class c_lang:
    def c(self):
        print("C Language")

    def feature(self):
        print("Procedural Feature")

class cpp_lang:
    def cpp(self):
        print("CPP Language")

    def feature(self):
        print("OOPs Feature")

class python_lang(cpp_lang,c_lang): 
    def python(self):
        print("Python Language")

    def feature(self):
        print("Both OOPs and Procedural Feature")

python_lang_obj = python_lang()
python_lang_obj.c()
python_lang_obj.cpp()
python_lang_obj.python()
python_lang_obj.feature()


print(python_lang.__mro__) # Method Resolution Order
print(python_lang.mro())


# If some class is not extending any class, then bydefault is extends object class (pre-define class)
